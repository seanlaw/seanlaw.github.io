---
layout: post
title: Pip Installing Wheels with Conda GCC/G++
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

I was trying to `pip install` a simple package that contained wheels that needed to be compiled with both GCC and G++. Of course, without using SUDO (i.e., `yum install gcc`) meant that I needed to rely on my good friend, Conda:
<br><br>
{% highlight python %}
conda install gcc_linux-64
conda install gxx_linux-64
{% endhighlight %}
<br><br>
Now, we aren't done yet! According to the <a href="https://conda.io/docs/user-guide/tasks/build-packages/compiler-tools.html">conda documentation</a>, the compilers are found in `/path/to/anaconda/bin` but the `gcc` and `g++`executables are prefixed with something like `x86_64-conda-cos6-linux-gnu-gcc`. So, we'll need to create some symbolic links to these executables:
<br><br>
{% highlight python %}
ln -s /path/to/anaconda/bin/x86_64-conda-cos6-linux-gnu-gcc /path/to/anaconda/bin/gcc
ln -s /path/to/anaconda/bin/x86_64-conda-cos6-linux-gnu-g++ /path/to/anaconda/bin/g++
{% endhighlight %}
<br><br>
Now, my pip install command is able to compile the wheel successfully! 
