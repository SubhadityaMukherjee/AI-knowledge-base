# Basics
- Model can decide where to look in the input

## Soft Attention
- For a simple Seq2Seq, all hidden state vectors $h_t$ across timesteps are linearly combined
- $c_i = \Sigma_{j=1}^T \alpha_{ij} h_j$
- $a_{ij} = \frac{exp(e_{ij})}{\Sigma_{k=1}^T exp(e_{ij})}$
- ![[Pasted image 20220307181112.png]]

### Scaled Dot Product Attention
- $Attention(Q, K,V) = softmax(\frac{QK^T}{\sqrt{d_K}})V$
	- Q is query, K is key V is value. Same dims
	- Generalization of soft attention

### Encoder Decoder Attention
- Q comes from prev decoder
- K,V from encoder

### Self Attention
- Q,K,V all from same module but prev layer

## Multi Head Attention
- Multiple attention instances, each focusing on a different part of the input
- $MultiHead(Q,K,V) = Concat(head_1, head_2, …., head_h)W^O$
	- $head_i = Attention(QW_i^Q, KW_i^K , VW_i^V)$
- W is learnable projections for attention params
- ![[Pasted image 20220307183058.png]]

## Image Captioning
![[Pasted image 20220307183552.png]]

## Encoding

### Position Encoding
- Transformers are feed forward. So need a way to inject position into seq 
- $PE(pos, 2i) = sin(\frac{pos}{10000^\frac{2i}{d_{model}}})$
- $PE(pos, 2i+1) = cos(\frac{pos}{10000^\frac{2i}{d_{model}}})$

## Embedding
- More complex than 1 hot
- Lookup table is an example. 
	- $token\_embedding(i) = gather(W, i)$
