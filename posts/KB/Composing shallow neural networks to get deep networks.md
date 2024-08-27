---
title: Composing shallow neural networks to get deep
toc: true
categories:
  - deeplearning
date modified: Tuesday 27th August 2024, Tue
date created: Tuesday 27th August 2024, Tue
---

# Composing shallow neural networks to get deep networks
```toc
```

- Consider two networks with 3 hidden units. Input $x, x'$ , output $y, y'$
	- ![[Pasted image 20240827202511.png]]
	- ![[Pasted image 20240827202529.png]]
- ![[Pasted image 20240827201808.png]]
- If we use a [[Relu]], this also is a family of piecewise linear functions. 
	- the number of linear regions is potentially greater than for a shallow network with six hidden units
- This maps three ranges of $x$ to same range of $y \in [-1,1]$ -> 9 linear regions

## Deep neural networks
- (Input -> Shallow network -> second network) is a special case of neural network
- Output of the first network (f1) $y$ is a linear combination of the activations at the hidden units. And the first operations of the second network (f2) are linear in the output of the first network. Hence f2(f1) = linear function
- ![[Pasted image 20240827203123.png]]
	- $$\psi_{10}= \theta'_{10}+ \theta'_{11}\phi_{0},\psi_{11}= \theta'_{11}\phi_{1}, \psi_{12}=\theta'_{11}\phi_{2}...$$
	- which is a network with 2 hidden layers.
	- So a network with two layers can represent a family of functions formed by composing those networks.
- ![[Pasted image 20240827203340.png]]
### Folding space
- One way to think about composing networks is by thinking of it as folding space and then applying an [[Activation Functions]]. 
- ![[Pasted image 20240827202757.png]]
	- ![[Pasted image 20240827204450.png]]
