---
layout: post
title: pyESL - Chapter 2.4 - Statistical Decision Theory
tagline: Elements of Statistical Learning in Python
published: false
tags: [pyesl]
weight: 2.4
---
<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

\\[
\begin{align} 
{RSS} &= (\textbf{Y} - \textbf{X}{\beta})^{T}(\textbf{Y} - \textbf{X}{\beta}) \\\
&= \textbf{Y}^{T}\textbf{Y} - \textbf{Y}^{T}\textbf{X}{\beta} - {\beta}^{T}\textbf{X}^{T}\textbf{Y} + {\beta}^{T}\textbf{X}^{T}\textbf{X}{\beta} \qquad \because\textbf{AB}^{T}=\textbf{B}^{T}\textbf{A}^{T} \\\
&= \textbf{Y}^{T}\textbf{Y} - 2\textbf{Y}^{T}\textbf{X}{\beta} + {\beta}^{T}\textbf{X}^{T}\textbf{X}{\beta} \qquad \because \textbf{Y}^{T}\textbf{X}{\beta} = \textbf{X}^{T}{\beta}^{T}\textbf{Y} \\\
\end{align}
\\]

