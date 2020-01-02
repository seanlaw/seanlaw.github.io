---
layout: post
title: Finding the Top or Bottom K Elements from a NumPy Array
---

If you have a NumPy array, you can use `np.argpartition` to find the indices of either the top k elements or the bottom k without having to sort the entire array first. To find the top k:
<br><br>
{% highlight python %}
idx = np.argpartition(x, -k)[-k:]  # Indices not sorted

idx[np.argsort(x[idx])][::-1]  # Indices sorted by value from largest to smallest
{% endhighlight %}
<br><br>
To find the bottom k:
{% highlight python %}
idx = np.argpartition(x, k)[:k]  # Indices not sorted

idx[np.argsort(x[idx])]  # Indices sorted by value from smallest to largest
{% endhighlight %}
<br><br>
