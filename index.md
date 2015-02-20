---
layout: page
title: The Science of Data
tagline:  
---
{% include JB/setup %}

<ul class="posts" style="list-style-type: none; margin-left: 0px;">
  {% for post in site.posts %}
    <li>
      <h2>
      <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a>
      </h2>
      <br>
      <i class="posts">{{ post.date | date_to_string }}</i>
      <p>{{ post.excerpt }}</p>
      <br><br>
    </li>
  {% endfor %}
</ul>

