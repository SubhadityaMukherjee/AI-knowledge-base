---
title: Multi Head Attention
---

# Multi Head Attention
- Multiple attention instances, each focusing on a different part of the input
- $$MultiHead(Q,K,V) = Concat(head_1, head_2, …., head_h)W^O$$
	- $$head_i = Attention(QW_i^Q, KW_i^K , VW_i^V)$$
- W is learnable projections for attention params
- ![[Pasted image 20220307183058.png]]






















