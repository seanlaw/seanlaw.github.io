---
layout: post
title: Ignoring Requests SSL Verification in Third Party Apps
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

_WARNING: This is unsafe!_

One of the most annoying things is not being able to perform an https request using a third party application (e.g., twine) if you're behind a network firewall that requires SSL verification. Luckily, you can turn this off by temporarily modifying the requests package. Open the `~/miniconda3/lib/python3.7/site-packages/requests/sessions.py` and, in the `Session` class, set
<br><br>
{% highlight python %}
#: SSL Verification default.
self.verify = False
{% endhighlight %}
<br><br>

Alternatively, directly from the command line, you might be able to tell the `ssl` Python module to temporarily disable SSL verification before running the Python program:
<br><br>
<!--
{% highlight %}
PYTHONHTTPSVERIFY=0 python your_script.py
{% endhighlight %}
<br><br>
-->

Note that this is a complete hack and not usually advised especially if the site that you are visiting is not trusted. This is only here for demonstration purposes. Do not use this code! 
