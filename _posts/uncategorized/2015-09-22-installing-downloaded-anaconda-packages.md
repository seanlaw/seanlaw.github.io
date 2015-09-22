---
layout: post
title: Installing Downloaded Anaconda Python Packages
---

<img class="img-left" align="left" src="{{ site.url }}/images/anaconda_logo.png">

Continuum's Anaconda If you work in a secure network at your job then conda may not be able to hit the Anaconda repositories directly even if it's for accessing free packages. Additionally, it's not recommended to use pip over conda when installing new packages. However, installing new packages can be done manually by:

1. Downloading the package(s) (and its necessary dependencies) directly from the <a href="https://repo.continuum.io/pkgs">Continuum Repo</a>
2. And installing the tar.bz2 file using `conda install ./package_name.tar.bz2`
