---
title: Fear of Git
date: 2017-03-31 08:37:00 +0530
comments: true
author: Yogeswaran Thulasidoss
tags: Git
category:
slug: fear_of_git
---

The intention of this article is not to explain how Git works.  It is just to explain how Git should be approached.

## The beginning

In 2010, I got introduced to Git. **Git** was a buzz word then. Just skimmed through its features and thought how could there be any other source control not having all these.  
> *I was saying to myself,
Git is the most obvious way any source control should work.  
But that was a pretty immature thought, because I did not know what is actually happening inside Git.*

Later, was working in Git with the so called basic commands.  I was able to manage with just few commands **git add**, **git commit**, **git pull**, **git push**.  To be honest, dint even use **git rebase** or **git merge** explicitly.  Having come from SVN background I thought those are for power users.

After a while, took a [codeschool](http://www.codeschool.com) course on basics of Git.  From what I remember, even they were using only these basic commands as part of their course.  So, never bothered to explore more after that.

Then I was put in a project whose source is maintained by a different team and we were asked to contribute to it by creating pull request.  This is the time I really understood that I don't know Git.  It was no more a linear workflow I was used to before.  In this project I faced all possible issues that might arise in parallel development.
> *Then started hating Git and thought how easy my life was when I was using SVN.*

> *Anytime before pushing my code into Git I used to google for atleast 10 minutes to find the commands to help in that situation.*

> *After each push, my aversion towards Git was increasing.  Was thinking why people are not using SVN which is much simpler.  Also thought, Git is meant for users like its author.*

## Basic merge operation

In SVN, when I wanted to merge my code with the latest in the repo I would do the following. I will have two folders.  One folder having source with my changes and the other folder just downloaded from the server.  Mostly will be using tool like Beyond Compare (running in trial version) to compare the difference and move the changes from **my changes folder** to **the latest code folder**.

> *The merge operation was fully manual but I was having the complete control and knew what will be the end result.*

I am not sure if I used SVN correctly, but this was the mentality with which I was approaching Git.  

> *Also, I was under the impression that source control tool would be dumb, meaning that it would only maintain whatever content we are giving under some revision. Merging the code would be the job of the user.*

Did not wanted Git to do the merge on its own because was worried how could a source control tool understand the semantics of the code.

This is the first paradigm shift that needs to happen when moving to Git.  We need to understand that we are not asking Git to arbitrarily merge two text files lying somewhere.  There is history associated with that file and we are consciously making a decision to add our changes on top of those changes.  

> *In case any tangential code was added by others and our changes were added on top of it, how can source control tool identify these?*

Valid question, but we'll end up in the same situation even if we merge it manually.  Definitely we will not be able to catch all these even when we merge using Beyond Compare.  

> *Obviously, the only way to solve this is to have unit tests which will make sure the merge has not broken anything.*

Though this sounds obvious it took a lot of time for me to understand this.

## Sequence of commands
There is no one-way or sequence of commands to help in all situation.  Each time the problem might be different and the command to use in that particular situation might be different.  This is one other thing very different compared to what I have been following in SVN.

There used to be instructions like **svn checkout**, add you changes and then **svn commit**.  We can blindly follow these two steps and get our things done in SVN.

In Git, I tried following a series of commands and ended up creating pull request with 94 commits but I had made only 2 commits on my own.

With Git, don't expect a sequence of commands to help in all situation.  Understand the requirement and decide on what commands to use in that situation.

## Variety of commands
Assuming that you are mentally prepared and clear about the merge and realized that there is no sequence of commands to help in all situations,

> *the variety of commands and its options makes Git, daunting.*

The only pill for this issue is to understand the internals of Git.

## Understanding the internals

I don't think we need to know what's happening behind the scenes in SVN to use SVN.

But lately understood that Git can only be tamed if we understand what's happening in the background.

When you are clear on how Git works then there is nothing as elegant as Git.

Even now I wont say that I know Git completely, but one thing is of sure, my fear of Git is gone after this basic understanding.

Happy hacking!!!
