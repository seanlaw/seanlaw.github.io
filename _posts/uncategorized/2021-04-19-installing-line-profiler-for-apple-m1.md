---
layout: post
title: Installing line_profiler For the Apple M1 ARM-based Chips
---

Recently, I found the need to install `line_profiler` on my Apple M1 machine in order to profile some code in Jupyter. While `pip` appeared to successfully install the package without any errors, I encountered segmentation faults when I loaded the package. Instead, the solution was to install directly from source :
<br><br>
{% highlight shell %}
conda install -y -c conda-forge scikit-build cython
git clone https://github.com/pyutils/line_profiler.git
cd line_profiler && python setup.py install
{% endhighlight %}
<br><br>
Now, you should be able to use `line_profiler`!
