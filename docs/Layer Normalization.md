---
title: Layer Normalization
tags: regularize
date modified: Thursday, August 11th 2022, 12:32:51 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Layer Normalization
- For RNNs etc
- Mean and variance calculated independantly for each element of the batch by aggregating over the [features](Features.md) dimensions.
- ![Pasted image 20220621163906](assets/Pasted%20image%2020220621163906.jpg) (Compared to [Batch Normalization](Batch%20Normalization.md))
- $$ \begin{align*}\\
&\mu_{\mathcal{B}} \leftarrow \frac{1}{m}\Sigma_{i=1}^{m}x_{i}\\
&\sigma^{2}_{\mathcal{B}} \leftarrow \frac{1}{m}\Sigma_{i=1}^{m}(x_{i}-\mu_{\mathcal{B}})^{2}\\
&\hat x_{i} \leftarrow \frac{x_{i}-\mu_{\mathcal{B}}}{\sqrt{\sigma^{2}_{\mathcal{B}} + \epsilon}}\\
&y_{i}= \gamma \hat x_{i}+ \beta
\end{align*}
$$

