---
layout: post
title: pyESL - Chapter 2.4 - Statistical Decision Theory
tagline: Elements of Statistical Learning in Python
published: true
tags: [pyesl]
weight: 2.4
---
<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->
Deriving the expected prediction error (EPE)
\\[
\begin{align} 
EPE(f) &= E(Y-f(X))^2 \\\
&= \int [y-f(x)]^2~Pr(dx,dy) \\\
&= \int [y-f(x)]^2~p(x,y)~dxdy \\\
&= \int_x \int_y [y-f(x)]^2~p(x,y)~dxdy \\\
&= \int_x \int_y [y-f(x)]^2p(x)~p(y|x)~dxdy \\\
&= \int_x \left(\int_y [y-f(x)]^2~p(y|x)~dy\right)~p(x)~dx \\\
&= \int_x \left(E_{Y|X}([Y-f(X)]^2|X = x)\right)~p(x)dx \\\
&= E_X \\\
\end{align}
\\]

