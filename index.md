---
layout: page
title: The Science of Data
tagline:  
---
{% include JB/setup %}

<ul class="posts">
  {% for post in site.posts %}
    <li>
      <h2>
      <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a>
      </h2>
      <br>
      <p class="greydate">{{ post.date | date: "%B %-d %Y" }}</p>
      <br>
      <p>{{ post.excerpt }}</p>
      <br><br>
    </li>
  {% endfor %}
</ul>

