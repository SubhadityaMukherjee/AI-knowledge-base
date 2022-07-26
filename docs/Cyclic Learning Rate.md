---
title: Cyclic Learning Rate

tags: optimizer 
---

# Cyclic Learning Rate
- With respect to local minima and [[Saddle Points|saddle points]], one could argue that you could simply walk "past" them if you set steps that are large enough. Having a learning rate that is too small will thus ensure that you get stuck.
- Now, Cyclical Learning Rates - which were introduced by Smith (2017) - help you fix this issue. These learning rates are indeed cyclical, and ensure that the learning rate moves back and forth between a _minimum value_ and a _maximum value_ all the time.
- ![[assets/Pasted image 20220626150653.png]]
- ![[assets/Pasted image 20220626150655.png]]
- ![[assets/Pasted image 20220626150701.png]]




























