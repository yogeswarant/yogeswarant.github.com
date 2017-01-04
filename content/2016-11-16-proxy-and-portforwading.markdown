---
title: Proxy and port forwarding
date: 2016-11-16 18:40:19 +0530
comments: true
author: Yogeswaran Thulasidoss
tags: haproxy, ssh, proxy, reverse-proxy
category:
slug: proxy_port_forwarding
---
This article is more like a case study on when to use proxies and when to just stick to simple port forwarder.  Also discusses in detail on what each of those is, and the tools falling under each category.

At office, we have our solution - basically a bunch of HTTP services, deployed on openstack which is not directly accessible from external network.  We were asked to use a [jump server](https://en.wikipedia.org/wiki/Jump_server) (a.k.a jump box/jump host) - a server in the middle which has access to both, private network of the solution and the external network.

For the using the services exposed by the stack we had to login to the jump server and make any HTTP requests for individual services.  It was too much of a burden to login to jump server to access API endpoints.  At the same time did not want to mess with the deployment scripts and expose all the instances to the external work.

Then got the idea of installing and configuring HAProxy which will behave like a tunnel to forward the traffic as such the the API endpoints as they are just HTTP services.

There were several teams using the same jump server and even they were having same stacks/same HTTP Services deployed within.  Therefore starting following the convention of using a prefix for each stack.  We had around 10 services getting exposed and all the services were prefixed with "1" in their port numbers.  It was easy to configure the test scripts to point to these services without much of a change.

I was happy about what I did and explained this to the team.  The actual fun started then.

One my colleague asked 
> "What is HAProxy", 

I replied 
> "It is a reverse proxy."  

Then he asked 
> "Why is that called so?  Is there anything called as forward proxy, if so, what is the difference between the two?"

Other asked 
> "How easy is it to configure HAProxy?"

And there was one more question, 
> "Is there a need to install HAProxy in this case, can't this not be solved using simple SSH port forwarder?"

And the last one was 
> "On which network layer does HAProxy operate?  Can it forward only HTTP Traffic?"

I decided to find answers to all these questions and this article is the result of that.

### How easy is it to configure HAProxy?

Configuring HAProxy (version 1.6.3) for this use case is simple.

In /etc/haproxy/haproxy.cfg, define a frontend and its corresponding backend.
```
frontend myservice
	bind 0.0.0.0:18888
	default_backend myservice

backend myservice
	balance roundrobin
	server myservice 192.168.224.143:8888 check
```

frontend says start listening on port 18888 on (0.0.0.0) all interfaces in this machine and forward it to backend service myservice which is actually listening in port 8888 on 192.168.224.143.

### What is reverse proxy?

Reverse proxy is a entity on the server side which will recieve all the requests on behalf of the server and forwards it to the actual server that is residing in the same network.

### What is the difference between forward proxy an reverse proxy?

It is only difference in perception i.e on whose behalf is this middle man is entering the picture.  
As we saw earlier, if the server itself brings something before it to act like a server on its behalf - that something is called reverse proxy.
If the client brings something in front of it to act like a client on its behalf while talking to the server - that something is called a forward proxy.

### SSH Port forwarding Vs HAProxy

The use case defined above is simple, in this case, load balancing functionality is not needed and it is just one-to-one mapping between the machines. Therefore, for this scenario ssh port forwarding suites the best.  One more advantage is that there is no extra installation needed, mostly all distributions comes bundled with ssh and servers run sshd.

### How to do port forwarding using ssh?

```
ssh -L [bind_address:]port:host:hostport

Specifies that the given port on the local (client) host is to be forwarded to the given host and port on
the remote side.  
```

```
ssh -R [bind_address:]port:host:hostport

Specifies that the given port on the remote (server) host is to be forwarded to the given host and port on the local 
side.  
```

For the use case discussed above, either of the two forms can be used.  

To use -L option we should first loggin into jump server and run the command below command,

```$ ssh -N -f -L 18888:192.168.224.143:8888 username@127.0.0.1```

**-R** option can be used from the local machine itself,

```$ ssh -N -f -R 18888:192.168.224.143:8888 username@jump_server_machine_ip```

**-N** option is meant to say do not execute any command(don't take me to the bash shell of the remote machine).

**-f** to run ssh in the background.

The man page of ssh is awesome, please refer to that for more details.


### On which network layer does HAProxy operate?  Can it forward only HTTP Traffic?

Tag line of HAProxy says that it is "TThe Reliable, High Performance TCP/HTTP Load Balancer".  Therefore we can understand that it can operate on both TCP as well as HTTP layer.  The reason why I say "as well as" is that, it can understand HTTP traffic perform routing based on URL which cannot be achieved when a simple port forwarder is used.  SSH port forward operates on TCP layer.

Happy hacking!!!

References:

*[http://unix.stackexchange.com/questions/115897/whats-ssh-port-forwarding-and-whats-the-difference-between-ssh-local-and-remot](http://unix.stackexchange.com/questions/115897/whats-ssh-port-forwarding-and-whats-the-difference-between-ssh-local-and-remot)*

*[http://stackoverflow.com/questions/224664/difference-between-proxy-server-and-reverse-proxy-server](http://stackoverflow.com/questions/224664/difference-between-proxy-server-and-reverse-proxy-server)*

*[http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/](http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/)*
