---
layout: post
title: Python 2 Unicode Problem
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

The following Python error is one of the most annoying one's I've ever encountered:
<br><br>
{% highlight python%}
Traceback (most recent call last):
  File "./test.py", line 3, in <module>
    print out
UnicodeEncodeError: 'ascii' codec can't encode character u'\u2019' in position 0: ordinal not in range(128)
{% endhighlight %}
<br>
Essentially, you can't write unicode characters as string unless you've converted the text to a string first before printing it. A detailed explanation can be found in Kumar McMillan's wonderful talk titled <a href="http://farmdev.com/talks/unicode/">'Unicode in Python, Completely Demystified'</a>. To summarize, McMillan offers three useful yet simple rules:
<br><br>

1. Decode early (after reading from a file)
2. Unicode everywhere
3. Encode late (for writing to a file or printing to the screen)

<br>
As recommended by McMillan, one could create two utility functions:
<br><br>
{% highlight python%}
def to_unicode(obj, encoding='utf-8'):
    """
    Always convert any text read from a file into unicode

    http://farmdev.com/talks/unicode/
    """
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)

    return obj

def to_string(obj, encoding='utf-8'):
    """
    Convert unicode to string so that it can be written to a file
    """

    return obj.encode(encoding)
{% endhighlight %}
<br>
which can be used like this:
<br><br>
{% highlight python%}
text = u'\u2019'  # <E2><80><99> = right single quotation mark
out = to_unicode(text)
print to_string(out)
{% endhighlight %}
<br>
Happy Unicoding!
