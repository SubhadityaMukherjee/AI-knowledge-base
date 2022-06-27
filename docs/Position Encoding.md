---
title: Position Encoding
tags: architecture 
---

# Position Encoding
- Transformers are feed forward. So need a way to inject position into seq
- $$PE(pos, 2i) = sin(\frac{pos}{10000^\frac{2i}{d_{model}}})$$
- $$PE(pos, 2i+1) = cos(\frac{pos}{10000^\frac{2i}{d_{model}}})$$
- Conceptually, adding word order to a sentence
	- Something like ("Hello", 1) , ("from",2) , ("me", 3)
























