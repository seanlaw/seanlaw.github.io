---
layout: post
title: A Simple Restart Script
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

Let's say that you have a Python script (or other command), called run.py, that you'd like to run in the background on a Linux OS and then end the session:
<br><br>
{% highlight python %}
import time
while True:
    time.sleep(5)
    print("I'm awake!")
{% endhighlight %}
<br><br>
To prevent the session from timing out, one common way to avoid this is to use:
{% highlight bash %}
nohup ./run.sh &> LOG &
{% endhighlight %}
<br><br>
This will execute the command in the background and also write any output to a LOG file. However, if I come back months later and forget that it is still running and I execute this command again then I might end up having multiple processes running the same command. To avoid this, we can do a little better and ensure that we kill the existing process. This typically requires recording the PID of the original process:
{% highlight bash %}
cat PID | xargs kill -9 2>/dev/null
nohup ./run.sh &> LOG &
echo $! > PID
{% endhighlight %}
<br><br>
This simple little trick has come in handy many times and I hope you find it useful too!
