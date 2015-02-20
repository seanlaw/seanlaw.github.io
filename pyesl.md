---
layout: page
title: pyESL
tagline: Elements of Statistical Learning in Python
header: pyESL
group: navigation
---
{% include JB/setup %}

<p>
Inspired by Carl Vogel's <a href="http://slendermeans.org/pages/will-it-python.html">site</a>, pyESL chronicles my journey through "Elements of Statistical Learning" using Python.
</p>

{% assign posts = site.tags['pyesl'] | sort:"weight"%}
{% for post in posts %}
[{{ post.title }}]({{ post.url  }})
{% endfor %}
