---
layout: post
title: Convert a Pandas DataFrame to Numeric
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

Pandas has deprecated the use of `convert_object` to convert a dataframe into, say, float or datetime. Instead, for a series, one should use:
<br><br>
{% highlight python%}
df['A'] = df['A'].to_numeric()
{% endhighlight %}
<br>
or, for an entire dataframe:
<br><br>
{% highlight python%}
df = df.apply(to_numeric)
{% endhighlight %}
<br>
