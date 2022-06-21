---
title: Rejection Sampling
---

# Rejection [[Sampling]]
- Also called Best-of-n [[sampling]]
- No [[CDF]] with a simple inverse
- Importance [[sampling]]
- Use a simpler distribution which is somewhat related to the target [[pdf]] 
	- Sample by transformation
- Now if we can take a [[Proto PDF]] $g_{0} \geq f$  where we can sample from the [[pdf]] g
- Take a point from g with [[probability]] $f(\tilde x)/g_{0}(\tilde x)$
	- Either accept or reject if satisfies [[probability]]
	- If accepted then return the sample
- Drop a point from $g_{0}(x)$ with that [[probability]]
- Depends on how close g is to f of course
- ![[../assets/Pasted image 20220324114746.png]]
	- If the ratio $\frac{f}{g_{0}}$ is small. (aka f is bigger), then there are many rejections and the algo will be slow. Impossible to not do in high dim spaces










































