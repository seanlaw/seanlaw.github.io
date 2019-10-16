---
layout: post
title: Detecting File Encodings
---

There have been numerous times where I've tried read a CSV file into a Pandas DataFrame and it fails due to the file encoding. The best thing to do is to detect the file encoding by reading a few lines from the file and then passing that encoding to Pandas. The file encoding detection part can be done with the `chardet` package and below is a convenience function for grabbing the encoding for the first `n_lines`:
<br><br>
{% highlight python %}
from chardet.universaldetector import UniversalDetector

def get_encoding(fname, n_lines=50):
    detector = UniversalDetector()
    detector.reset()

    with open(fname, 'rb') as f:
        for i, row in enumerate(f):
            detector.feed(row)
            if i >= n_line-1 or detector.done: 
        break

     detector.close()

     return detector.result['encoding']
{% endhighlight %}
<br><br>
Then you can call this function  with a file name:
<br><br>
{% highlight python %}
encoding = get_encoding("file.csv")

df = pd.read_csv("file.csv", encoding=encoding)
{% endhighlight %}
<br><br>
I hope this help you too!
