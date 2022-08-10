---
title: Rejection Sampling
tags: distribution 
date modified: Thursday, August 11th 2022, 12:32:47 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Rejection [Sampling](Sampling)
- Also called Best-of-n [sampling](sampling)
- No [CDF](CDF.md) with a simple inverse
- Importance [sampling](sampling)
- Use a simpler distribution which is somewhat related to the target [PDF](PDF.md)
	- Sample by transformation
- Now if we can take a [Proto PDF](Proto%20PDF.md) $g_{0} \geq f$ where we can sample from the [PDF](PDF.md) g
- Take a point from g with [Probability](Probability.md) $f(\tilde x)/g_{0}(\tilde x)$
	- Either accept or reject if satisfies [Probability](Probability.md)
	- If accepted then return the sample
- Drop a point from $g_{0}(x)$ with that [Probability](Probability.md)
- Depends on how close g is to f of course
- ![im](assets/Pasted%20image%2020220324114746.png)
	- If the ratio $\frac{f}{g_{0}}$ is small. (aka f is bigger), then there are many rejections and the algo will be slow. Impossible to not do in high dim spaces

