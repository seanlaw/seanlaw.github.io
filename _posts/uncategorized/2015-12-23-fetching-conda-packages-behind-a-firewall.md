---
layout: post
title: Fetching Conda Packages Behind a Firewall
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

One of the most annoying things is not being able to update software if you're behind a network firewall that requires SSL verification. You can turn this off in Anaconda via
<br><br>
{% highlight python %}
conda config --set ssl_verify no
{% endhighlight %}
<br><br>
and for pip via
<br><br>
{% highlight python %}
pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package name>
{% endhighlight %}
<br><br>
Optionally, you can also specify the package version like this:
{% highlight python %}
pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package name>[=0.1.2]
{% endhighlight %}
<br><br>
Better yet, you can permanently set the trusted-host by adding the following to the $HOME/.pip/pip.conf file:
{% highlight python %}
[global]
trusted-host = pypi.python.org
               files.pythonhosted.org
{% endhighlight %}

