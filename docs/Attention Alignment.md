---
title: Attention Alignment

tags: loss
date modified: Monday, October 10th 2022, 2:02:34 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [[Attention]] Alignment
- If there are sequences $x, y$
	- Encoder is any [[Recurrent]] with a forward state $$\overrightarrow h^{T}$$ and $$\overleftarrow h^{T}$$ for backward
	- Concat them represents the preceding and following word annotations
		- $$h_{i}= [\overrightarrow h_{i}^{T}; \overleftarrow h_{i}^{T}]$$, $i = 1, …, n$
		- Decoder has hidden state $s_{t}= f(s_{t-1}, y_{t-1}, c_{t})$ for the output word at position t for $t = 1, …, m$
			- Context vector $c_{t}$ is a sum of hidden states of the input seq, weighted by alignment scores
			- $$c_{t}= \Sigma_{i=1}^{n}\alpha_{t,i}h_{i}$$
			- How well the two words are aligned is given by
			- $$\alpha_{t,i} = align(y_{t}, x_{i})$$
			- Taking [[Softmax|softmax]]
				- $$\frac{exp(score(s_{t-1}, h_{i}))}{\Sigma_{i'-1}^{n}exp(score(s_{t-1}, h_{i}'))}$$
- $$f_{att}(h_{i}, s_{j}) = v_{a}^{T}tanh(W_{a}[h_{i};s_{j}])$$
- $v_{a}$ and $W_{a}$ are the learned [[Attention]] params
- $h$ is the hidden state for the encoder
- $s$ is the hidden state for the decoder
- Matrix of alignment
	- ![[assets/Pasted image 20220621170423.png]]
	- Final scores calculated with a [[Softmax]]

## Backlinks
> - [Additive [[Attention]]](Additive Attention.md)
>   - Uses a one layer feedforward network to calculate [[Attention Alignment]]
>
> - [Content Based [[Attention]]](Content Based Attention.md)
>   - [[Attention Alignment]] score $score(s_{t}, h_{i}) = cosine[s_{t}, h_{i}]$$
>
> - [Dot Product [[Attention]]](Dot Product Attention.md)
>   - A type of [[Attention Alignment]]
>
> - [Scaled [[Dot Product Attention]]](Scaled Dot Product Attention.md)
>   - [[Attention Alignment]] score $$\alpha_{t,i} = \frac{s_{t}^{T}h_{i}}{\sqrt{n}}$$
>
> - [Location Base [[Attention]]](Location Base Attention.md)
>   - [[Attention Alignment]] score $\alpha_{t,i} = softmax(W_{\alpha}s_{t})$

_Backlinks last generated 2022-10-04 13:01:19_
