---
title: Rejection Sampling
tags: distribution 
date modified: Thursday, August 11th 2022, 12:32:47 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Rejection [[Sampling]]
- Also called Best-of-n [[sampling]]
- No [[CDF]] with a simple inverse
- Importance [[sampling]]
- Use a simpler distribution which is somewhat related to the target [[PDF]]
	- Sample by transformation
- Now if we can take a [[Proto PDF]] $g_{0} \geq f$ where we can sample from the [[PDF]] g
- Take a point from g with [[Probability]] $f(\tilde x)/g_{0}(\tilde x)$
	- Either accept or reject if satisfies [[Probability]]
	- If accepted then return the sample
- Drop a point from $g_{0}(x)$ with that [[Probability]]
- Depends on how close g is to f of course
- ![[assets/Pasted image 20220324114746.png|im]]
	- If the ratio $\frac{f}{g_{0}}$ is small. (aka f is bigger), then there are many rejections and the algo will be slow. Impossible to not do in high dim spaces

## Backlinks

> - [Goodhart's Law](Goodhart's Law.md)
>   - [[Rejection Sampling]]

_Backlinks last generated 2022-10-04 13:01:19_
