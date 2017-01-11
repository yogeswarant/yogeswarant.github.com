---
title: 2's complement - you beauty
date: 2016-12-19 18:40:19 +0530
comments: true
author: Yogeswaran Thulasidoss
tags: c, bits, 2's complement
category: c
slug: twos_complement
---
This is a short write-up two's complement, which, in my humble opinion is one of the great idea to which entire computer industry should be thankful to.

I remember, in my school days when computer science subject was taught without computer, there used to be problems to find binary equivalent of a number.

Binary equivalent of 5 is 0101. (Considering bit length of 4).

On top of this, there used to be problems to find the one's complement of it and two's complement of it.

One's complement of 0101 is 1010 (Simply inverting 1 to 0 and 0 to 1).

Two's complement of 0101 is 1010 + 1 which is equal to 1011.

I was not curious to ask what is the need for one's complement or two's complement.  And I also don't remember seeing a problem like, finding a binary equivalent of a negative number.

Recently, I wanted to write a C program to print the binary equivalent of a number.  I started with the same mentality of diving by 2 and saving the remainder - definitely a bad algorithm.

There were couple of learnings from this, 

1. Computer already operates in binary, in that case, why to convert it into human readable(decimal) and then find the binary.
2. Not all problems needs to be solved like the way human solves it, algorithms should leverage the machine's capabilities. 

Moreover this algorithm will not able to handle negative numbers.

Then quickly opened a Python shell and printed binary equivalent of 5 and -5.
```
Python 2.7.10 (default, Jul 30 2016, 18:31:42)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> bin(5)
'0b101'
>>> bin(-5)
'-0b101'
```

> Oh Python, never expected this from you.

Wrote the below function in C,
```c
int print_binary(int i)
{
	int bitlen = sizeof(i) * 8;
	int j;
	char *bin = calloc(1, bitlen);
	for(j = 0; j < bitlen; j++) {
		bin[j] = (i & 1) ? '1': '0';
		i >>= 1;	
	}
	for (j = bitlen - 1; j >= 0; j--) {
		printf("%c ", bin[j]);
	}
	free(bin);
	return 0;
}
```

Output will look as shown below when -5 is passed to this function
```
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 
```

Then, some old memory cells in my brain said,
> Negative numbers are stored as two's complement.

Started to look why should it be stored as two's complement, 
> Can't it be just one's complement? 

> like, -5 = 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0

or

> A notation where first bit signifies the sign and rest all bits are left unchanged? 

> like, -5 = 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1

### Lets take the first case when negative numbers are just one's complement,

> What is one's complement of 0?

It is 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

There would be two ways to represent 0, as +0 and -0.

> Which means, computers are redefining the number system or, we are defining a different number system for machines.

So, its definitely a bad idea to go with one's complement.

	Two's complement of 0 is 
	1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 + 1 
	which will result in all 0s. (Carry bit being ignored).


### The second case when the first bit signifies the sign and the rest all bits are left unchaged,
this looks more human readable form of binary.  To put in other words 

> More human readable form of machine readable format!!!

In this case there has to be a condition check everytime before performing any operation.  

Also, let's go a little deeper and see what would happen in the circuits of the processor.  There is circuit to add two bits, is there a way to subtract two bits as such???

In two's complement if we try to add -5 and 5.  (For simplicity lets work with bit length of 4)

	1011 (-5)
	+
	0101 (5)
	----
	0000 (0)

Cool. Isn't it?

After seeing all these, started admiring the beauty of two's complement.

Happy hacking!!!

References:
*[http://stackoverflow.com/questions/1125304/why-is-twos-complement-used-to-represent-negative-numbers](http://stackoverflow.com/questions/1125304/why-is-twos-complement-used-to-represent-negative-numbers)*
