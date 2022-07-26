---
title: Decision Boundaries
---

# Decision Boundaries
- Minimal risk decision function is unique and must be represented in terms of [Distributions](Distributions) of data generating RVs X and Y
	- A is some subvolume of P. (n dimensional hypercubes or volume bodies)
	- $P_{X,Y}$ is ground truth
		- Function that assigns every choice of $A \subseteq P , c \in C$   the number P
- Decision function $h: P \rightarrow {c_{1}, …, c_{k}}$ partitions pattern space into k disjoint decision regions $R_{1}, …, R_{k}$ by $$R_{i}= \{x \in P | h(x) = c_{i}\}$$
- If a test pattern falls into $R_{i}$ it is classified as class i

## Finding Decision Regions
- which yields the lowerst misclassification rate or highest [Probability](Probability.md) of correct classification
- $f_{i}$ be the [PDF](PDF.md) for [Class Conditional distribution](Class%20Conditional%20distribution.md)
- [Probability](Probability.md) of obtaining a correct classification for $R_{i}$ is $$\Sigma_{i=1}^{k}P(X \in R_{i}, Y = c_{i})$$
- ![im](assets/Pasted%20Image%2020220318161058.png)
- This region has curved boundaries aka decision boundaries
	- Folded and on higher dims : very complex and fragmented
- x is a vector
- For patterns on these boundaries, two or more classifications are equally probable
- Maximal if $$R_{i}= \{x \in P| i = argmax_{j} P(Y=c_{j})f_{j}(x)\}$$
- Then $$h_{opt}: P \rightarrow C_{j}x \rightarrow c_{argmax_{j}P(Y=c_{j})f_{j}(x)}$$
- Algo learns estimates of the [Class Conditional distribution](Class%20Conditional%20distribution.md) and class probabilities aka priors
































































































