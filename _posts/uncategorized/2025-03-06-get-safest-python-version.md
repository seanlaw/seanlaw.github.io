---
layout: post
title: Identify the Safest Python Version
---

There have been a numerous times when I would download and install Python using conda and known packages would fail to install because the Python version is too "new". Thus, I've found the need to quickly identify a reasonably recent, stable, and "safe" version of Python to use and this is the command that I came up with it:
<br><br>
{% highlight shell %}
#!/bin/bash

get_safe_python_version()
{
    SAFE_PYTHON=`curl --location https://devguide.python.org/versions | xmllint --html --xpath '//section[@id="supported-versions"]//table/tbody/tr[count(//section[@id="supported-versions"]//table/tbody/tr[td[.="security"]]/preceding-sibling::*)]/td[1]/p/text()' - 2>/dev/null`
}

get_safe_python_version
echo $SAFE_PYTHON
{% endhighlight %}
<br><br> 

Essentially, it scrapes the version table from "https://devguide.python.org/versions" and retrieves the penultimate security version (i.e., one version before the latest securty version).

As a bonus, you can also retrieve the minimum Python version or comptaible numpy/numba Python version using:
<br><br>
{% highlight shell %}
#!/bin/bash

get_min__python_version()
{
    MIN_PYTHON=`curl --location https://devguide.python.org/versions | xmllint --html --xpath '//section[@id="supported-versions"]//table/tbody/tr[last()]/td[1]/p/text()' - 2>/dev/null`
}

get_min_numba_numpy_version()
{
    NUM_PYTHON=`curl --location https://numba.readthedocs.io/en/stable/user/installing.html#version-support-information | xmllint --html --xpath '//div[@id="version-support-information"]//table/tbody/tr[1]/td[3]/p/text()' - 2>/dev/null | awk '{print $1}' | sed s/\.x//``
}

{% endhighlight %}
<br><br>

It's certainly nothing fancy (and, admittedly, rather ugly) but it works like a charm!
