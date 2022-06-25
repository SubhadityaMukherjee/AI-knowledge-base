---
title: Skip Connection
tag: architecture
---

# Skip Connection
- ![Pasted%20Image%2020220306120520.png](assets/Pasted%20Image%2020220306120520.png)
- $$x_i = F(x_{i-1}) + x_{i-1}$$
- [[Effect_Of_Depth]]
- Previous layer gradient carried to next module untouched -> loss surface is smoother
- Transfer #gradients to prevent [[Vanishingexploding gradients]]
- Learns the difference (residual) $$F(x) = H(x)-x$$























































