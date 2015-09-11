---
layout: post
title: Using NumPy Argmin or Argmax Along with a Conditional
---

<img class="img-left" align="left" src="{{ site.url }}/images/numpy.jpeg">

It's no secret that I love my some Python! Yes, even more than Perl, my first love from my graduate school days. 
<br><br>
I've always found NumPy to be great for manipulating, analyzing, or transforming arrays containing large numerical data sets. It is both fast and efficient and it comes with a tonne of great functions.
<!--more-->
<br><br>
One of these functions is `numpy.argmin` (or its older sister, `numpy.argmax`)
<br><br>
{% highlight python%}
import numpy as np

a = np.array([[2.0, 12.1, 99.2],
              [1.0, 1.1, 1.2],
              [1.04, 1.05, 1.5],
              [4.1, 4.2, 0.2],
              [10.0, 11.0, 12.0],
              [3.9, 4.9, 4.99]
             ])

print np.argmin(a)
{% endhighlight %}
<br><br>
Naturally, this will flatten the entire 2D array and return the index (`11`) of the lowest global value (`0.2`)(Note that NumPy arrays start from zero). One could take this a step further with:
<br><br>
{% highlight python%}
print np.argmin(a, axis=1)
{% endhighlight %}
<br><br>
This will run through each row (`axis=1`)and return the index of the column with the lowest value. In this case:
<br><br>
{% highlight python%}
array([0, 0, 0, 2, 0, 0])
{% endhighlight %}
<br><br>
Now, here's where things can get a little tricky. What happens if I want to find the row with the smallest first column value but whose third column value is greater than 1.25?
<br><br>
{% highlight python%}
mask = (a[:, 2] > 1.25)
subset_idx = np.argmin(a[mask][:, 0])
parent_idx = np.arange(a.shape[0])[mask][subset_idx]
print("The row is {} (Note that it starts from zero)".format(parent_idx))
{% endhighlight %}
<br><br>
Here, the `mask` contains a boolean mask for all values in the third column. Then, `np.argmin(a[mask][:, 0])` applies that mask to the values in the first column and returns the index for the smallest value. However, the index corresponds to the subset of array `a` rather than to the indices of `a` itself. Luckily, line 4 remedies this by allowing us to recover the parent index (`parent_idx`) of array `a` and the rest is history!
<br><br>
This precise problem has come up so regularly in my NumPy use that it was worth sharing as I'm sure others have come across this exact problem. Enjoy!

