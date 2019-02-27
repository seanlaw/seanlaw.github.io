---
layout: post
title: Compiling Facebook's StarSpace with Conda Boost
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

Recently, I was playing around with Facebook's <a href="https://github.com/facebookresearch/StarSpace">StarSpace</a>, a general-purpose neural model for efficient learning of entity embeddings for solving a wide variety of problems. According to the installation instructions, you need a C++11 compiler and the Boost library. I already had <a href="http://seanlaw.github.io/2019/01/17/pip-installing-wheels-with-conda-gcc/">GCC installed</a> and Boost was only a quick conda command away:
<br><br>
{% highlight python %}
conda install boost
{% endhighlight %}
<br><br>
The StarSpace Makefile is hardcoded to look for the Boost library in /usr/local/bin/boost_1_63_0/, which is a problem. But how should I modify the StarSpace Makefile so that it knew where to include the Boost library? After a little digging, I found the Boost files in `/path/to/anaconda/include`. So, all I had to do was modify the following line in the StarSpace Makefile:
<br><br>
{% highlight python %}
#BOOST_DIR = /usr/local/bin/boost_1_63_0/
BOOST_DIR = /path/to/anaconda/include/
{% endhighlight %}
<br><br>
Executed `make` on the command line and everything compiled nicely! Yay! 
