---
layout: post
title: Setting Values of a Sparse Matrix
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

Let's say that you have a sparse matrix:
<br><br>
{% highlight python %}
import numpy as np
from scipy.sparse import

x = csr_matrix(np.array([[1, 0, 2, 0, 3], 
                         [0, 4, 0, 5, 0]]))
print(x)
{% endhighlight %}
<br>
{% highlight python %}
<2x5 sparse matrix of type '<class 'numpy.int64'>'
    with 5 stored elements in Compressed Sparse Row format>
{% endhighlight %}
<br><br>
One of the most common things that you might want to do is to make a conditional selection from the matrix and then set those particular elements of the matrix to, say, zero. For example, we can take our matrix from above and set all elements that have a value that are less than three to zero. Naively, one could do:
<br><br>
{% highlight python %}
x[x < 3] = 0
{% endhighlight %}
<br><br>
This works and is fine for small matrices. However, you'll likely encounter a warning message such as the following:
<br><br>
{% highlight python %}
/home/miniconda3/lib/python3.6/site-packages/scipy/sparse/compressed.py:282: SparseEfficiencyWarning: Comparing a sparse matrix with a scalar greater than zero using < is inefficient, try using >= instead.
  warn(bad_scalar_msg, SparseEfficiencyWarning)
{% endhighlight %}
<br><br>
The problem here is that for large sparse matrices, the majority of the matrix is full of zeros and so the `<` comparison becomes highly inefficient. Instead, you really only want to perform your comparison only with the nonzero elements of the matrix. However, this takes a little more work and a few more lines of code to accomplish the same thing. Additionally, we want to avoid converting our sparse matrices into costly dense arrays.
<!--more-->
<br>
First, we'll create a nonzero mask that keeps track of all of the nonzero elements that are less than 3 and returns the indices relative to the set of nonzero indices (and not the sparse or dense arrays).
<br><br>
{% highlight python %}
nonzero_mask = np.array(x[x.nonzero()] < 3)[0]
{% endhighlight %}
<br><br>
Next, with the appropriate nonzero mask, we can obtain the corresponding row and column indices (for the sparse matrix) for all of the nonzero elements that are less than 3. 
<br><br>
{% highlight python %}
rows = x.nonzero()[0][nonzero_mask]
cols = x.nonzero()[1][nonzero_mask]
{% endhighlight %}
<br><br>
Finally, with the proper sparse matrix indices in hand (that correspond to elements that are less than 3), we can set those elements' value to zero:
<br><br>
{% highlight python %}
x[rows, cols] = 0

print(x.todense())
{% endhighlight %}
<br><br>
And our array will end up as we had expected
<br><br>
{% highlight python %}
[[0 0 0 0 3]
 [0 4 0 5 0]]
{% endhighlight %}
<br><br>
I hope this helps you when you are looking to manipulate your sparse matrix and leave a comment below!
