---
layout: post
title: Fetching Conda Packages Behind a Firewall
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

One of the most annoying things is not being able to update software if you're behind a network firewall that requires SSL verification. You can turn this off in Anaconda via `conda config --set ssl_verify false --system`
