---
layout: post
title: Anaconda Environment
tagline:
---
<img class="img-left" align="left" src="{{ site.url }}/images/anaconda_logo_web.png">

I've been using Continuum's enterprise Python distribution package, Anaconda, for several months now and I love it. Recently, people have been asking about Python 2.7 vs Python 3.x and so I looked into how to switch between these environments using Anaconda.
<br><br>
In fact, it's quite straightforward and painless with Anaconda.
<br><br>
To set up a <b>new</b> environment with Python 3.4:
<!--more-->
<br><br>
{% highlight python%}
conda create -n py34 python=3.4 anaconda
{% endhighlight %}
<br><br>
Here, "py34" is a reference tag for later and "python=3.4 anaconda" are package specifications, which, according to the documentation, is the job of the SAT solver inside conda to find a consistent set of packages which satisfies these requirements. The above code will download all the new interpreter and all of the necessary dependencies to a separate directory.
<br><br>
To use ("activate") the newly created environment:
<br><br>
{% highlight python %}
source activate py34
{% endhighlight %}
<br><br>
Notice that we activate the reference tag "py34" that we chose above. Also, note that this new directory will be prepended to your path and the root Python directory will be removed (but Anaconda keeps track of all of this for you)
<br><br>
{% highlight python %}
bash-3.2$ python
Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41) 
{% endhighlight %}
<br><br>
And to stop using (deactivate) the environment:
<br><br>
{% highlight python %}
source deactivate  # or, in older versions of envs use `source deactivate py34`
{% endhighlight %}
<br><br>
It's that easy! When you call Python now, it should revert back to your root environment.
<br><br>
{% highlight python %}
bash-3.2$ python
Python 2.7.10 |Anaconda 2.2.0 (x86_64)| (default, May 28 2015, 17:04:42) 
{% endhighlight %}
<br><br>
Obviously, you can remove or delete an environment at any time by doing:
{% highlight python %}
bash-3.2$ conda remove --name py34 --all
{% endhighlight %}
<br><br>
Finally, to check what environments you have installed:
<br><br>
{% highlight python %}
conda env list
{% endhighlight %}
<br><br>
For more details, find the full set of features in the [conda docs](http://conda.pydata.org/docs/using/envs.html).
