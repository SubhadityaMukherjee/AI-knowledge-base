---
title: Adagrad
tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:58 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Adagrad
- Past squared grads as scaling factor for learning rate
- $$\begin{align}& g_{t,i} = \nabla_\theta J(\theta_{t,i}) \\ & \theta_{t+1, i} = \theta_{t,i} - \eta \cdot g_{t,i} \\ & \theta_{t+1, i} = \theta_{t,i} - \frac{\eta}{\sqrt{G_{t,ii} + \epsilon}} \cdot g_{t,i} \end{align}$$
- Doesnt forget past gradients

