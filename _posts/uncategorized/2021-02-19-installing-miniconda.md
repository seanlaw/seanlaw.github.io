---
layout: post
title: Installing Miniconda
---

When developing on a new VM, this is the basic setup that I like to build on top of:
<br><br>
{% highlight shell %}
#!/bin/bash

MINICONDADIR="$HOME/miniconda3"

rm -rf $MINICONDADIR
wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh -f -b -p $MINICONDADIR
$MINICONDADIR/bin/conda init
$MINICONDADIR/bin/conda update -y conda
$MINICONDADIR/bin/conda update -y --all
$MINICONDADIR/bin/conda install -y -c conda-forge mamba jupyterlab

if [[ `grep "alias python" $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo 'if [[ `which ipython | wc -l` -gt "0" ]]; then' >> $HOME/.bashrc
    echo '    alias python="ipython"' >> $HOME/.bashrc
    echo 'fi' >> $HOME/.bashrc
fi

if [[ `grep "alias ipynb" $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo 'if [[ `which jupyter-lab | wc -l` -gt "0" ]]; then' >> $HOME/.bashrc
    echo '    alias ipynb="jupyter-lab"' >> $HOME/.bashrc
    echo 'fi' >> $HOME/.bashrc
fi

if [[ `grep "alias rm" $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo 'alias rm="rm -i"' >> $HOME/.bashrc
fi

if [[ `grep "alias cp" $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo 'alias cp="cp -i"' >> $HOME/.bashrc
fi

if [[ `grep "alias vim" $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo 'alias vi="vim"' >> $HOME/.bashrc
fi

if [[ `grep "alias EDITOR" $HOME/.bashrc | wc -l` -lt "1" ]]; then
    echo 'export EDITOR="vim"' >> $HOME/.bashrc
fi

if [[ `grep syntax $HOME/.vimrc | wc -l` -lt "1" ]]; then
    echo "set viminfo=\'10,\"100,:20,%,n~/.viminfo" >> $HOME/.vimrc
    echo "" >> $HOME/.vimrc
    echo 'function! ResCur()' >> $HOME/.vimrc
    echo "    if line(\"'\\\"\") <= line(\"$\")" >> $HOME/.vimrc
    echo "        normal! g\`\"" >> $HOME/.vimrc
    echo '        return 1' >> $HOME/.vimrc
    echo '    endif' >> $HOME/.vimrc
    echo 'endfunction' >> $HOME/.vimrc
    echo "" >> $HOME/.vimrc
    echo 'augroup resCur' >> $HOME/.vimrc
    echo '    autocmd!' >> $HOME/.vimrc
    echo '    autocmd BufWinEnter * call ResCur()' >> $HOME/.vimrc
    echo 'augroup END' >> $HOME/.vimrc
    echo "" >> $HOME/.vimrc
    echo "set clipboard=unnamed" >> $HOME/.vimrc
    echo "set cindent" >> $HOME/.vimrc
    echo "set smartindent" >> $HOME/.vimrc
    echo "set autoindent" >> $HOME/.vimrc
    echo "set paste" >> $HOME/.vimrc
    echo "set ruler" >> $HOME/.vimrc
    echo "syntax on" >> $HOME/.vimrc
    echo "set tabstop=4" >> $HOME/.vimrc
    echo "set shiftwidth=4" >> $HOME/.vimrc
    echo "set expandtab" >> $HOME/.vimrc
fi

{% endhighlight %}
<br><br>
And then, after installing `miniconda`, I just need to exit and re-enter the VM
<br><br>
