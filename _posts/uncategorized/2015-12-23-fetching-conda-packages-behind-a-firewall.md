---
layout: post
title: Fetching Conda Packages Behind a Firewall
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

<!--
_WARNING: This is unsafe!_
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
pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org <package name>
{% endhighlight %}
<br><br>
Optionally, you can also specify the package version like this:
{% highlight python %}
pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org <package name>[=0.1.2]
{% endhighlight %}
<br><br>
Better yet, you can permanently set the trusted-host by adding the following to the $HOME/.pip/pip.conf file:
{% highlight python %}
[global]
trusted-host = pypi.python.org
               files.pythonhosted.org
               pypi.org
{% endhighlight %}
<br><br>
Alternatively, you can also temporarily disable SSL verification from the command line with:
<!--
{% highlight %}
PYTHONHTTPSVERIFY=0 pip install some_trusted_package_name
{% endhighlight %}
-->
<br><br>
Do not use this code!
