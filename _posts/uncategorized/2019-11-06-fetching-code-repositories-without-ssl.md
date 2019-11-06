---
layout: post
title: Fetching Code Repositories Without SSL
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

One of the most annoying things is not being able to clone a code repository from trusted sources such as Github or Bitbucket if you're behind a network firewall that requires SSL verification. Luckily, you can turn this off in Git via:
<br><br>
{% highlight bash %}
git config --global http.sslverify false
{% endhighlight %}
<br><br>
