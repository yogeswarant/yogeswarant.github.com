---
title: Dockerfile CMD vs ENTRYPOINT
date: 2016-10-20 17:54:07 +0530
comments: true
author: Yogeswaran Thulasidoss
tags: docker, dockerfile, how it works
category:
slug: dockerfile_cmd_entrypoint
---
I had difficulty in understanding the difference between CMD and ENTRYPOINT in Dockerfile before I did the below experiment.  Hope this will help someone like me who cannot understand the difference from the [documentation](https://docs.docker.com/engine/reference/builder/) or [stackoverflow](http://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile).
<br></br>
Consider the below docker file
<pre>
[ythulasi@YTHULASI-M-C341 01.BusyboxWithCMD]$ cat Dockerfile
FROM busybox:latest
CMD ["cat", "/etc/passwd"]
</pre>

Let's build an image and call it **busy_cmd_image**
<pre>
[ythulasi@YTHULASI-M-C341 01.BusyboxWithCMD]$ docker build -t busy_cmd_image .
Sending build context to Docker daemon 2.048 kB
Step 1 : FROM busybox:latest
 ---> 2b8fd9751c4c
Step 2 : CMD cat /etc/passwd
 ---> Using cache
 ---> e4df0d0c0d67
Successfully built e4df0d0c0d67
</pre>

Now, we'll run the image and name the container **busy_cmd_container**
<pre>
[ythulasi@YTHULASI-M-C341 01.BusyboxWithCMD]$ docker run --name busy_cmd_container busy_cmd_image
root:x:0:0:root:/root:/bin/sh
daemon:x:1:1:daemon:/usr/sbin:/bin/false
bin:x:2:2:bin:/bin:/bin/false
sys:x:3:3:sys:/dev:/bin/false
sync:x:4:100:sync:/bin:/bin/sync
mail:x:8:8:mail:/var/spool/mail:/bin/false
www-data:x:33:33:www-data:/var/www:/bin/false
operator:x:37:37:Operator:/var:/bin/false
nobody:x:99:99:nobody:/home:/bin/false
</pre>

There is another docker file which has ENTRYPOINT.
<pre>
[ythulasi@YTHULASI-M-C341 02.BusyboxWithEntryPoint]$ cat Dockerfile
FROM busybox:latest
ENTRYPOINT ["cat", "/etc/passwd"]
</pre>

Let's build the image and name it **busy_entry_image**.
<pre>
[ythulasi@YTHULASI-M-C341 02.BusyboxWithEntryPoint]$ docker build -t busy_entry_image .
Sending build context to Docker daemon 2.048 kB
Step 1 : FROM busybox:latest
 ---> 2b8fd9751c4c
Step 2 : ENTRYPOINT cat /etc/passwd
 ---> Using cache
 ---> 4016bc22c516
Successfully built 4016bc22c516
</pre>

Now, when we run this image we'll get the same output like before.
<pre>
[ythulasi@YTHULASI-M-C341 02.BusyboxWithEntryPoint]$ docker run --name busy_entry_container busy_entry_image
root:x:0:0:root:/root:/bin/sh
daemon:x:1:1:daemon:/usr/sbin:/bin/false
bin:x:2:2:bin:/bin:/bin/false
sys:x:3:3:sys:/dev:/bin/false
sync:x:4:100:sync:/bin:/bin/sync
mail:x:8:8:mail:/var/spool/mail:/bin/false
www-data:x:33:33:www-data:/var/www:/bin/false
operator:x:37:37:Operator:/var:/bin/false
nobody:x:99:99:nobody:/home:/bin/false
</pre>

Let's come to the point now.
> Does it mean CMD and ENTRYPOINT are just different notations to perform the same activity?

> The answer is **NO**.

We'll first see why are they behaving the same way.

For that, let's inspect their containers to understand them better.

I am not a docker expert to interpret all the fields in the output.  But let's have a look at those fields which are significant for us.  

I have marked those in **<font color="red">red</font>**.

<pre>
[ythulasi@YTHULASI-M-C341 01.BusyboxWithCMD]$ docker inspect busy_cmd_container
[
    {
        "Id": "2e71127e337a437d02af82bf998d0507ab1bb037ddd85448eed504262bad0f22",
        "Created": "2016-10-21T03:36:54.315846464Z",
        <b><font color="red">"Path": "cat",
        "Args": [
            "/etc/passwd"
        ],</font></b>
        "State": {
            "Status": "exited",
            "Running": false,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2016-10-21T03:36:54.45640868Z",
            "FinishedAt": "2016-10-21T03:36:54.459113472Z"
        },
        "Image": "sha256:9aaf05fedcf6f4510f76281a33fcc6f1f16e63d406fa6ebe2f3b9218590d23b9",
        ...
]
</pre>
`Path` is set as "cat" and `Args` has just one value that is "/etc/passwd".

Let's also inspect the busy_entry_container,
<pre>
[ythulasi@YTHULASI-M-C341 02.BusyboxWithEntryPoint]$ docker inspect busy_entry_container
[
    {
        "Id": "99ae755c4c4422021bd28e8acd19fc061a97a1b3654e5d50f2ad5521e866bf3d",
        "Created": "2016-10-21T12:38:04.567062004Z",
        <b><font color="red">"Path": "cat",
        "Args": [
            "/etc/passwd"
        ],</font></b>
        "State": {
            "Status": "exited",
            "Running": false,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2016-10-21T12:38:04.690532676Z",
            "FinishedAt": "2016-10-21T12:38:04.693614887Z"
        },
        "Image": "sha256:22aa602beefdaee9ee54ee218d099817cfba48fbea38fb943c85fb141332fb63",
        ...
]
</pre>

In both the cases `Path` is "cat" and `Args` is "/etc/passwd".
This is reason for both the above images to give the same output when no command line parameter is passed.  

We found why both the images are giving the same output.  Now, let's run images by passing the command line arguments and see how it behaves.

<pre>
[ythulasi@YTHULASI-M-C341 01.BusyboxWithCMD]$ docker run --name busy_cmd_container_2 busy_cmd_image /etc/hosts
docker: Error response from daemon: oci runtime error: exec: "/etc/hosts": permission denied.
</pre>

When we inspect the container busy_cmd_container_2
<pre>
[
    {
        "Id": "95a99fb59cb293683719824c1d712d32658b314435743f028fe5c3335923a45f",
        "Created": "2016-10-21T12:26:25.400017698Z",
        <b><font color="red">"Path": "/etc/hosts",
        "Args": [],</font></b>
        "State": {
            "Status": "created",
            "Running": false,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 0,
            "ExitCode": 126,
            "Error": "oci runtime error: exec: \"/etc/hosts\": permission denied",
            "StartedAt": "0001-01-01T00:00:00Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:9aaf05fedcf6f4510f76281a33fcc6f1f16e63d406fa6ebe2f3b9218590d23b9",
        ...
]
</pre>

This shows that arguments passed in the command line overrides the default command(CMD) given in Dockerfile.  
In this case docker thinks that /etc/hosts is a command and tries to execute it.  As it is not a executable file, we are seeing permission denied error.

Let's try the same experiment on busy_entry_image image.
We'll run busy_entry_image image and pass /etc/hosts a command line argument and give a name busy_entry_container_2 to inspect it.

<pre>
[ythulasi@YTHULASI-M-C341 02.BusyboxWithEntryPoint]$ docker run --name busy_entry_container_2 busy_entry_image /etc/hosts
root:x:0:0:root:/root:/bin/sh
daemon:x:1:1:daemon:/usr/sbin:/bin/false
bin:x:2:2:bin:/bin:/bin/false
sys:x:3:3:sys:/dev:/bin/false
sync:x:4:100:sync:/bin:/bin/sync
mail:x:8:8:mail:/var/spool/mail:/bin/false
www-data:x:33:33:www-data:/var/www:/bin/false
operator:x:37:37:Operator:/var:/bin/false
nobody:x:99:99:nobody:/home:/bin/false
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.2	b4133689279d
</pre>
Cool!!! We can see contents of both /etc/passwd and /etc/hosts file getting printed.

Let's inspect this container,
<pre>
[ythulasi@YTHULASI-M-C341 02.BusyboxWithEntryPoint]$ docker inspect busy_entry_container_2
[
    {
        "Id": "7d0be615dac4624fda3e690485719a32921042a1f32ad738856cf0425eeb1f0b",
        "Created": "2016-10-21T12:41:21.194580336Z",
        <b><font color="red">"Path": "cat",
        "Args": [
            "/etc/passwd",
            "/etc/hosts"
        ],</font></b>
        "State": {
            "Status": "exited",
            "Running": false,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2016-10-21T12:41:21.327221171Z",
            "FinishedAt": "2016-10-21T12:41:21.339957393Z"
        },
        "Image": "sha256:22aa602beefdaee9ee54ee218d099817cfba48fbea38fb943c85fb141332fb63",
        ...
]
</pre>

In this case, the argument passed in command line is getting appended to the `Args` list but the `Path` is unchanged.

**This is the difference between CMD and ENTRYPOINT in a Dockerfile.**

`CMD` is meant to supply the default arguments while running the container.

`ENTRYPOINT` is meant to specify the executable that will be invoked when the container is run.

`CMD` and `ENTRYPOINT` can be used in conjuction.

Look at the Dockerfile which has both CMD and ENTRYPOINT.
<pre>
[ythulasi@YTHULASI-M-C341 03.BusyboxWithEntryAndCMD]$ cat Dockerfile
FROM busybox:latest
CMD ["/etc/passwd", "/etc/hosts"]
ENTRYPOINT ["cat"]
</pre>

Let's build an image out of it can call it as busy_cmd_entry_image
<pre>
[ythulasi@YTHULASI-M-C341 03.BusyboxWithEntryAndCMD]$ docker build -t busy_cmd_entry_image .
Sending build context to Docker daemon 2.048 kB
Step 1 : FROM busybox:latest
 ---> 2b8fd9751c4c
Step 2 : CMD /etc/passwd /etc/hosts
 ---> Running in 4d583424e639
 ---> f7a96ac1bf4c
Removing intermediate container 4d583424e639
Step 3 : ENTRYPOINT cat
 ---> Running in 057321f9e2a0
 ---> 8b6517ac039e
Removing intermediate container 057321f9e2a0
Successfully built 8b6517ac039e
</pre>

We'll run the image without any argument
<pre>
[ythulasi@YTHULASI-M-C341 03.BusyboxWithEntryAndCMD]$ docker run --name busy_cmd_entry_container busy_cmd_entry_image
root:x:0:0:root:/root:/bin/sh
daemon:x:1:1:daemon:/usr/sbin:/bin/false
bin:x:2:2:bin:/bin:/bin/false
sys:x:3:3:sys:/dev:/bin/false
sync:x:4:100:sync:/bin:/bin/sync
mail:x:8:8:mail:/var/spool/mail:/bin/false
www-data:x:33:33:www-data:/var/www:/bin/false
operator:x:37:37:Operator:/var:/bin/false
nobody:x:99:99:nobody:/home:/bin/false
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.2	7e549359bd1c
</pre>

Let's run it passing a command line argument
<pre>
[ythulasi@YTHULASI-M-C341 03.BusyboxWithEntryAndCMD]$ docker run --name busy_cmd_entry_container_2 busy_cmd_entry_image /etc/resolv.conf
nameserver 10.0.2.3
</pre>

**The onliner of this article is,
`ENTRYPOINT` is meant to provide the executable and `CMD` is to pass the default arguments to the executable.**

Happy hacking!!!
<br></br>
References:

*[http://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile](http://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile)*

*[https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)*
