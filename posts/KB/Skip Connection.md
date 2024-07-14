---
categories: ['temp']
toc: true
title: Skip Connection
tag: architecture
date modified: Monday, October 10th 2022, 2:02:16 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Skip Connection
- ![Pasted%20Image%2020220306120520.png](images/Pasted%20image%2020220306120520.png)
- $$x_i = F(x_{i-1}) + x_{i-1}$$
- [Effect Of Depth](Effect%20Of%20Depth.md)
- Previous layer gradient carried to next module untouched -> [loss](loss.md) surface is smoother
- Transfer #gradients to prevent [Vanishingexploding gradients](Vanishingexploding%20gradients.md)
- Learns the difference (residual) $$F(x) = H(x)-x$$



