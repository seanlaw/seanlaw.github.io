---
layout: post
title: Adding LaTeX Equations to Github Issues
---

Recently, I found the need to embed some LaTex equations in a Github issue and discovered that you can do this by using this HTML image tag along with the desired equation:
<br><br>
{% highlight shell %}
<img src="https://render.githubusercontent.com/render/math?math=a^{2} %2B b^{2} = c^{2}">
{% endhighlight %}
<br><br>
which should produce:
<br><br>
<img src="https://render.githubusercontent.com/render/math?math=a^{2} %2B b^{2} = c^{2}">
<br><br>
Now, you should be able to embed this anywhere!

Check out <a href="https://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b">this thread</a> to add additional formatting like superscript or fractions
