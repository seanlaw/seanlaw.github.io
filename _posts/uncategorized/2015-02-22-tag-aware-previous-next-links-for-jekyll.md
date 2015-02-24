---
layout: post
title: Tag Aware Previous/Next Links for Jekyll 
---
Creating and maintaining a vanilla Jekyll-Boostrap website is pretty straightforward. However, I couldn't find an obvious way to customize the previous/next links below each blog post so that:
<br><br>

    1. The links were aware of the tags listed in the front matter
    2. The method did not depend on plugin (since my site is being hosted on Github)

<br>
After tonnes of digging, I managed to piece together a Liquid-based solution (see my last post, to see how I add <a href="{{ page.previous.url }}">Liquid code in Jekyll</a>)!
<!--more-->
<br><br>
{% highlight html  %}{% raw %}
{% for tag in page.tags %}
  {% if tag == "pyesl"%}
    <ul>
      {% assign posts = site.tags['pyesl'] | sort:"weight" %}
      {% for post in posts %}
        {% if post.url == page.url %}
          {% assign last_inx = forloop.index0 | minus:1 %}
          {% if forloop.first == false %}
            <li class="prev"><a href="{{ BASE_PATH }}{{ posts[last_inx].url }}" title="{{ posts[last_inx].title }}">&larr; Previous</a></li>
          {% else %}
            <li class="prev disabled"><a>&larr; Previous</a></li>
          {% endif %}
          <li><a href="{{ BASE_PATH }}{{ site.JB.pyesl_path }}">PyESL</a></li>
          {% if forloop.last == false %}
            {% assign next_inx = forloop.index0 | plus:1 %}
            <li class="next"><a href="{{ BASE_PATH }}{{ posts[next_inx].url }}" title="{{ posts[next_inx].title }}">Next &rarr;</a></li>
          {% else %}
            <li class="next disabled"><a>Next &rarr;</a>
          {% endif %}
        {% endif %}
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}
{% endraw %}{% endhighlight %}
