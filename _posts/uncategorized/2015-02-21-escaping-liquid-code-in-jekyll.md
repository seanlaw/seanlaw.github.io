---
layout: post
title: Escaping Liquid Code in Jekyll 
---
To document some of my challenges in customizing this site, I've had to delve into Liquid code.  However, adding Liquid code tags in Jekyll can be quite tricky and painful. Luckily, some smart people have identified a couple of nice solutions <a href="http://www.sarathlal.com/escape-liquid-tag-in-jekyll-posts/">exists</a>. Below is the markdown code that I've adopted for use in future posts:
<br><br>
{% highlight html %}
{{ "{%" }} highlight html %}{{ "{%" }} raw %}
\\Place Liquid and HTML code here
{{ "{%" }} endraw %}{{ "{%" }} endhighlight %}
{% endhighlight %}
