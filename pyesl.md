---
layout: page
title: PyESL
tagline: Elements of Statistical Learning in Python
header: PyESL
group: navigation
---
{% include JB/setup %}

<p>
Inspired by Carl Vogel's <a href="http://slendermeans.org/pages/will-it-python.html">site</a>, PyESL chronicles my journey through "Elements of Statistical Learning" using Python.
</p>
<br>
{% assign posts = site.tags['pyesl'] | sort:"weight"%}
{% for post in posts %}
  <h3><a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></h3>
  <br><br>
{% endfor %}
