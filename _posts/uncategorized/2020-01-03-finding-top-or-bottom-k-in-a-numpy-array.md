---
layout: post
title: Finding the Top or Bottom K Elements from a NumPy Array
---

If you have a NumPy array, you can use `np.partition` to find the top k elements or the bottom k without having to sort the entire array first. To find the top k:
<br><br>
{% highlight python %}
top_k = np.partition(x, -k)[-k:]  # Results are not sorted

np.sort(tok_k)[::-1]  # Sorted from largest to smallest
{% endhighlight %}
<br><br>
To find the bottom k:
{% highlight python %}
bottom_k = np.partition(x, k)[:k]  # Results are not sorted

np.sort(bottom_k)  # Sorted from smallest to largest
{% endhighlight %}
<br><br>
Alternatively, you can use `np.argpartition` to find the **indices** of either the top k elements or the bottom k without having to sort the entire array first. To find the top k:
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
