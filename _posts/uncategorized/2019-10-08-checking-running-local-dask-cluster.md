---
layout: post
title: Checking if a Local Dask Cluster is Running
---

One thing that I find myself doing fairly often is spinning up a local Dask cluster, forgetting that it is running, and then starting it up again on a different port. This is here as a reminder that you can first `try` to connect to the cluster and, if it times out, then create the `LocalCluster` on the fly:
<br><br>
{% highlight python %}
from distributed import Client, LocalCluster

try:
    client = Client('tcp://localhost:8786', timeout='2s')
except OSError:
    cluster = LocalCluster(scheduler_port=8786)
    client = Client(cluster)
client.restart()
client
{% endhighlight %}
<br><br>
Since I always forget how to do this, I hope that others will find this helpful!
