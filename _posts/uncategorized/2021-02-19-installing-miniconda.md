---
layout: post
title: Installing Miniconda
---

When developing on a new VM, this is the basic setup that I like to build on top of:
<br><br>
{% highlight shell %}
#!/bin/bash

rm -rf $MINICONDADIR
wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh -f -b -p $MINICONDADIR
$MINICONDADIR/bin/conda init
$MINICONDADIR/bin/conda update -y conda
$MINICONDADIR/bin/conda update -y --all
$MINICONDADIR/bin/conda install -y -c conda-forge mamba jupyterlab

if [[ `grep python $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo "alias python="ipython" >> $HOME/.bashrc
fi

if [[ `grep ipynb $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo "alias ipynb="jupyter-lab" >> $HOME/.bashrc
fi

if [[ `grep rm $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo "alias rm="rm -i" >> $HOME/.bashrc
fi

if [[ `grep cp $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo "alias cp="cp -i" >> $HOME/.bashrc
fi

if [[ `grep vim $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo "alias vi="vim" >> $HOME/.bashrc
fi

if [[ `grep EDITOR $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo "export EDITOR="vim" >> $HOME/.bashrc
fi

if [[ `grep syntax $HOME/.vimrc | wc -l` -lt "1" ]]; then
    echo "syntax on" >> $HOME/.vimrc
    echo "filetype plugin indent on" >> $HOME/.vimrc
    echo "set tabstop=4" >> $HOME/.vimrc
    echo "set shiftwidth=4" >> $HOME/.vimrc
    echo "set expandtab" >> $HOME/.vimrc
fi

{% endhighlight %}
<br><br>
And then, after installing `miniconda`, I just need to exit and re-enter the VM
<br><br>
