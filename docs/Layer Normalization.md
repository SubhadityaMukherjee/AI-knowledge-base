---
title: Layer Normalization
tags: regularize
---

# Layer Normalization
- For RNNs etc
- Mean and variance calculated independantly for each element of the batch by aggregating over the [[Features|features]] dimensions.
- ![[assets/Pasted image 20220621163906.jpg]] (Compared to [[Batch Normalization]])
- $$ \begin{align*}\\
&\mu_{\mathcal{B}} \leftarrow \frac{1}{m}\Sigma_{i=1}^{m}x_{i}\\
&\sigma^{2}_{\mathcal{B}} \leftarrow \frac{1}{m}\Sigma_{i=1}^{m}(x_{i}-\mu_{\mathcal{B}})^{2}\\
&\hat x_{i} \leftarrow \frac{x_{i}-\mu_{\mathcal{B}}}{\sqrt{\sigma^{2}_{\mathcal{B}} + \epsilon}}\\
&y_{i}= \gamma \hat x_{i}+ \beta
\end{align*}
$$






















































## Backlinks

> - [ConvNeXt](ConvNeXt.md)
>   - [[GELU]] instead of [[Relu]] , a single activation for each block (the original [[Transformer]] module has just one activation after the MLP), fewer normalization [[Layers]], [[Batch Normalization]] substituted by [[Layer Normalization]] , and separate downsampling layer
>    
> - [Non [[Relational Inductive Bias]]](Non Relational Inductive Bias.md)
>   - [[Batch Normalization]] , [[Layer Normalization]] , [[Instance Normalization]]
>    
> - [Regularization](Regularization.md)
>   - [[Layer Normalization]]

_Backlinks last generated 2022-07-26 20:33:15_
