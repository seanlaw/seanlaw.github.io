---
layout: post
title: Creating a Time-Dependent Sleep Function
---

I've been retrieving data from a database that is being accessed by many people and it is especially busy during the mornings. So, to avoid this congestion, I set a simple timer in my Python code that detects the (Eastern) time and sleeps for a minute until it is outside of the congested hours. Here's what it looks like:
<br><br>
{% highlight python %}
import datetime
import time
import pytz

# Sleep between 9a-11a Eastern Time
while 9 <= datetime.datetime.now(pytz.timezone('America/New_York')).time().hour < 11:
    time.sleep(60)
{% endhighlight %}
<br><br>
Things seemed fine when I ran the script locally and it would update the cron job as I had expected. So, I let it go on its merry way. A couple of weeks later and the site that I was monitoring goes down but I don't get any notifications. Again, running the above code directly from the command line worked perfectly but the cron job was not doing anything. Upon further inspection, the cron job was somehow looking for the `run_monitor.sh` script in the `home` directory. Then it dawned on me that the `pwd` was the problem. Since the cron job is being executed relative to the home directory, the `pwd` command within the script actually returns the home directory and not the location of the `run_monitor.sh` script. So, instead, we need the `$APPDIR` to point to the location of the `run_monitor.sh` script like this:
<br><br>
{% highlight bash %}
#!/bin/sh

APPDIR="$( cd "$( dirname "$0" )" && pwd )"
HTTP_RESPONSE=`curl -k -sL -w "%{http_code}" "http://www.google.com" -o /dev/null`

if [ ! $HTTP_RESPONSE -eq 200 ]; then
    # Replace this line to send a message to channel
    # Remove/add/update cron job to once every hour
    (crontab -l | grep -v "$APPDIR/run_monitor.sh"; echo "0 * * * * $APPDIR/run_monitor.sh") | sort - | uniq - | crontab -
else
    # Remove/add/update cron job to once every minute
    (crontab -l | grep -v "$APPDIR/run_monitor.sh"; echo "* * * * * $APPDIR/run_monitor.sh") | sort - | uniq - | crontab -
{% endhighlight %}
<br><br>
Problem solved! It's a subtle bug that was hard to detect/debug but became obvious only after I spent some time thinking about it. I hope to never encounter this again!
