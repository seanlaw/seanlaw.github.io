---
layout: post
title: Write and Read a NumPy Array 
---

The documentation for writing/reading a NumPy array to/from a file without pickling is a tad hard to follow. One may need to do this when dealing with large NumPy arrays. Below is some simple code for writing and reading a NumPy array to a temporary file:
<br><br>
{% highlight python %}
#!/usr/bin/env python

import numpy as np
import tempfile
import os

ftmp = tempfile.NamedTemporaryFile(delete=False)
fname = ftmp.name + ".npy"
inp = np.random.rand(100)
np.save(fname, inp, allow_pickle=False)
out = np.load(fname, allow_pickle=False)

print(out)

os.remove(fname)
{% endhighlight %}
<br><br>
Here, we leverage the `tempfile` module for dynamically creating our intermediate files and then deleting them only after the file is no longer needed. This is rather useful if you are using the `multiprocessing` module and your files are created within a subprocess. The key part to all of this is the necessity to append the `.npy` extension to the file name that is created by `tempfile` and also to turn off pickling (this will allow us to create files that are larger than 4GiB) in size.
<br><br>
