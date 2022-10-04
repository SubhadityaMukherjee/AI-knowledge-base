---
tags: temp
title: Markov for Continuous Distributions
date modified: Thursday, August 11th 2022, 12:32:50 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Markov for Continuous Distributions
- Family of [[PDF]]
- If a [[Markov Chain]] with state set S, matrix M is executed m times . The transition probabilities transmit between states and then, $$P(X_{n+m}=s_{j}|X_{n}= s_{i}) = M^{m}(i, j)$$
- where $M^{m}= M \cdot M \cdot M … \cdot M$ (m times)
- To get the [[PDF]] $$g^{n+1}(x) = \int_{\mathbb{R}^{k}}T(x|y)g^{n}(y)dy$$
- [[Invariant Distribution]]

## Backlinks

> - [Markov Chain](Markov Chain.md)
>   - [[Markov for Continuous Distributions]]

_Backlinks last generated 2022-10-04 13:01:19_
