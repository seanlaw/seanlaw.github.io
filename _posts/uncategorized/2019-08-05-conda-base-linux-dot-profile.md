---
layout: post
title: Conda Base Ignores Linux .Profile
---

Recently, I reinstalled miniconda and allowed it to set up `conda init` on Mac OSX. From what I could tell, it:

1. Updates`.bash_profile` and checks to see if `conda.sh` exists and executes it
2. Otherwise, if 1. is False, then pre-pend the `miniconda3/bin` directory to `$PATH`
3. Add `. /Users/law978/miniconda3/etc/profile.d/conda.sh` to the `.profile` and remove references to pre-pend `miniconda3/bin` to `$PATH` 

Now, this seemed great but I noticed that all of the aliases that had been set in `.profile` were being ignored. In fact, it looks like `.profile` wasn't being sourced at all. When I looked inside of `.bash_profile`, I realized that the usual command to source the contents of `.profile` was missing:
<br><br>
{% highlight %}
if [ -f ~/.profile ]; then
   source ~/.profile
fi
{% endhighlight %}
<br><br>
Simply adding these three lines back to `.bash_profile` did the trick. So, now, all of my aliases are loaded when a new terminal is opened and `conda` is initialized according to plan.
