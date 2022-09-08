---
layout: post
title: Handling Special Characters In Your Proxy Password
---

In the past, I've discussed how not to <a href="http://seanlaw.github.io/2015/12/23/fetching-conda-packages-behind-a-firewall/"> fetch conda packages behind a firewall</a> and, instead, <a href="http://seanlaw.github.io/2021/11/07/updating-conda-with-proxy/">how to leverage your coporate proxy</a>. However, in any modern tech environment, you will likely be required to include special characters in your password that might cause your script to fail since special characters will need to be "URL encoded". This post builds upon our previous knowledge and provides a solution to this problem:
<br><br>
{% highlight shell %}
#!/bin/bash

urlencode(){
    # Encodes spaces and non-alphanumeric characters
    str=$@
    local length="${#str}"
    for (( i = 0; i < length; i++ )); do
        local c="${str:i:1}"
        case $c in
            [a-zA-Z0-9]) printf "$c" ;;
            *) printf '%%%02X' "'$c"
        esac
    done
}

proxy(){
    hostname="proxy.yourcompany.com"
    port="8080"
    user="$(whoami)"
    read -s password
    password="$(urlencode $password)"
    export http_proxy=http://$user:$password@$hostname:$port
    export https_proxy=http://$user:$password@$hostname:$port
    export HTTP_PROXY=http://$user:$password@$hostname:$port
    export HTTPS_PROXY=https://$user:$password@$hostname:$port
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
