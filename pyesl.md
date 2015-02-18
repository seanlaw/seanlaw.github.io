---
layout: page
title: pyESL
tagline: Elements of Statistical Learning in Python
header: pyESL
group: navigation
---
{% include JB/setup %}

"Elements of Statistical Learning"

{% assign posts = site.tags['pyesl'] | sort:"weight"%}
{% for post in posts %}
[{{ post.title }}]({{ post.url  }})
{% endfor %}
