---
title: Attention Alignment

tags: loss
---

# Attention Alignment
- $$f_{att}(h_{i}, s_{j}) = v_{a}^{T}tanh(W_{a}[h_{i};s_{j}])$$
- $v_{a}$ and $W_{a}$ are the learned [Attention](Attention.md) params
- $h$ is the hidden state for the encoder
- $s$ is the hidden state for the decoder
- Matrix of alignment
	- ![](assets/Pasted%20image%2020220621170423.png)
	- Final scores calculated with a [Softmax](Softmax.md)


## Backlinks

> - [Additive Attention](Additive Attention.md)
>   - Uses a one layer feedforward network to calculate [[Attention Alignment]]

_Backlinks last generated 2022-06-21 17:08:56_
