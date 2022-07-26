---
title: Multi Head Attention
tags: architecture einsum 
---

# Multi Head [[Attention]]
- [ZihangDai et al., 2019](https://arxiv.org/abs/1901.02860)
- which computes self-[[Attention|attention]] over the inputs, then adds back the residual and layer normalizes everything. The [[Attention|attention]] head can be split into multiple segments, hence the name _multi-head_
- Multiple [[Attention|attention]] instances, each focusing on a different part of the input
- Words can mean different things in context
	- If using [[Self Attention]], then this just gets summed up. Which is not very nice
	- Several [[Attention|attention]] heads -> different output vectors
	- Concatenate them and pass through a linear transform -> dimension back to k
- $$MultiHead(Q,K,V) = Concat(head_1, head_2, …., head_h)W^O$$
	- $$head_i = Attention(QW_i^Q, KW_i^K , VW_i^V)$$
- W is learnable projections for [[Attention|attention]] params
- ![[assets/Pasted image 20220307183058.png|im]]
- To improve efficiency
	- Cut the incoming vector into chunks -> no of [[Attention|attention]] heads

```python
class MultiHeadAttentionNew(nn.Module):
    def __init__(self, n_head, d_model, d_k, d_v, dropout=0.1):
        super().__init__()
        self.n_head = n_head
        
        self.w_qs = nn.Linear(d_model, n_head * d_k)
        self.w_ks = nn.Linear(d_model, n_head * d_k)
        self.w_vs = nn.Linear(d_model, n_head * d_v)
        
        nn.init.normal_(self.w_qs.weight, mean=0, std=np.sqrt(2.0 / (d_model + d_k)))
        nn.init.normal_(self.w_ks.weight, mean=0, std=np.sqrt(2.0 / (d_model + d_k)))
        nn.init.normal_(self.w_vs.weight, mean=0, std=np.sqrt(2.0 / (d_model + d_v)))
        
        self.fc = nn.Linear(n_head * d_v, d_model)
        nn.init.xavier_normal_(self.fc.weight)
        self.dropout = nn.Dropout(p=dropout)
        self.layer_norm = nn.LayerNorm(d_model)

    def forward(self, q, k, v, mask=None):
        residual = q
        q = rearrange(self.w_qs(q), 'b l (head k) -> head b l k', head=self.n_head)
        k = rearrange(self.w_ks(k), 'b t (head k) -> head b t k', head=self.n_head)
        v = rearrange(self.w_vs(v), 'b t (head v) -> head b t v', head=self.n_head)
        attn = torch.einsum('hblk,hbtk->hblt', [q, k]) / np.sqrt(q.shape[-1])
        if mask is not None:
            attn = attn.masked_fill(mask[None], -np.inf)
        attn = torch.softmax(attn, dim=3)
        output = torch.einsum('hblt,hbtv->hblv', [attn, v])
        output = rearrange(output, 'head b l v -> b l (head v)')
        output = self.dropout(self.fc(output))
        output = self.layer_norm(output + residual)
        return output, attn
```






































## Backlinks

> - [ConvBERT](ConvBERT.md)
>   - Convolutional BERT (ConvBERT) improves the original [[BERT]] by replacing some [[Multi Head Attention]] [[Self Attention]] segments with cheaper and naturally local operations, so-called [[span-based dynamic convolutions]]. These are integrated into the self-[[Attention|attention]] mechanism to form a mixed [[Attention|attention]] mechanism, allowing Multi-headed Self-[[Attention|attention]] to capture global patterns; the Convolutions focus more on the local patterns, which are otherwise captured anyway. In other words, they reduce the computational intensity of training BERT.
>    
> - [Attention](Attention.md)
>   - [[Multi Head Attention]]

_Backlinks last generated 2022-07-26 20:33:15_
