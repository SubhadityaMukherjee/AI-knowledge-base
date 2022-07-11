---
title: Cyclic Learning Rate

tags: optimizer 
---

# Cyclic Learning Rate
- With respect to local minima and [saddle points](Saddle%20Points.md), one could argue that you could simply walk "past" them if you set steps that are large enough. Having a learning rate that is too small will thus ensure that you get stuck.
- Now, Cyclical Learning Rates - which were introduced by Smith (2017) - help you fix this issue. These learning rates are indeed cyclical, and ensure that the learning rate moves back and forth between a _minimum value_ and a _maximum value_ all the time.
- ![](assets/Pasted%20image%2020220626150653.png)
- ![](assets/Pasted%20image%2020220626150655.png)
- ![](assets/Pasted%20image%2020220626150701.png)


















