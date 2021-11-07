---
layout: post
title: Installing And Updating Conda With A Proxy
---

In the past, I've discussed how not to <a href="http://seanlaw.github.io/2015/12/23/fetching-conda-packages-behind-a-firewall/"> fetch conda packages behind a firewall</a>. In this post, let's assume that you are working behind a firewall in some corporate environment but your network administrator has given you access to a username/password-procted proxy:port that allows you to reach the "outside world":
<br><br>
{% highlight shell %}
http://<username>:<password>@proxy.yourcompany.com:8080
https://<username>:<password>@proxy.yourcompany.com:8080
{% endhighlight %}
<br><br>
Now, how do we download, install, and update `conda` but make sure that we direct our requests through our proxy? First, let's download `miniconda` through our proxy and then install it:
<br><br>
{% highlight shell %}
#!/bin/bash

prox(){
    export http_proxy=http://<username>:<password>@proxy.yourcompany.com:8080
    export https_proxy=http://<username>:<password>@proxy.yourcompany.com:8080
    export HTTP_PROXY=http://<username>:<password>@proxy.yourcompany.com:8080
    export HTTPS_PROXY=https://<username>:<password>@proxy.yourcompany.com:8080
}

proxy
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash ./Miniconda3-latest-MacOSX-x86_64.sh -f -b -p miniconda3
{% endhighlight %}
<br><br> 

With the proxy function above, you can now update conda and install other packages with:

<br><br>
{% highlight shell %}
proxy
conda update -y conda
conda update -y --all
conda install -y -c conda-forge stumpy numpy scipy numba
{% endhighlight %}
<br><br>

Now, you should be able to use the proxy and to install the software that you need to be productive!
