---
tags: temp
title: Skip Connection
tag: architecture
date modified: Wednesday, August 10th 2022, 11:41:23 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Skip Connection
- ![Pasted%20Image%2020220306120520.png](assets/Pasted%20image%2020220306120520.png)
- $$x_i = F(x_{i-1}) + x_{i-1}$$
- [Effect_Of_Depth](Effect_Of_Depth.md)
- Previous layer gradient carried to next module untouched -> loss surface is smoother
- Transfer #gradients to prevent [Vanishingexploding gradients](Vanishingexploding%20gradients.md)
- Learns the difference (residual) $$F(x) = H(x)-x$$

