---
layout: post
title: Installing A Conda Environment
---

When developing [STUMPY](https://stumpy.readthedocs.io/en/latest/), I frequently and purposely delete my entire Python (conda) environment and start from scratch. This serves two purposes:

1. It ensures that I continue developing and testing using the latest dependencies
2. It helps to ensure that no new local dependencies have crept into STUMPY

However, every time I wipe out my environment (`rm -rf miniconda3/`, I have to try and remember what I need to re-install. Instead, it's far more efficient to document all of this in an `environment.yml` file:
<br><br>
{% highlight shell %}
channels:
  - conda-forge
  - defaults
dependencies:
  - numpy
  - scipy
  - numba
  - pandas
  - dask
  - distributed
  - coverage
  - flake8
  - flake8-docstrings
  - black
  - pytest-cov
  - jupyterlab
{% endhighlight %}
<br><br>
And then, after reinstalling `miniconda`, I just need to execute the following commands in the same directory as the `environment.yml` file
<br><br>
{% highlight shell %}
conda update -y conda
conda update -y --all
conda env update --file environment.yml
{% endhighlight %}
<br><br>
Note that this installs the desired packages in the base conda environment. To install this in a named environment, you'll need:
<br><br>
{% highlight shell %}
conda update -y conda
conda update -y --all
conda env update --name environment_name --file environment.yml
{% endhighlight %}
<br><br>
