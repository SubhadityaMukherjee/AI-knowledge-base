---
categories: ['temp']
date modified: Monday, October 10th 2022, 2:02:33 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

toc: true
title: BYOL Loss

categories: ['temp']

---

# [BYOL](BYOL.md) Loss
- Similarity [loss](loss.md) between $q_\theta (z_\theta)$ and $sg(z^{'}_{\xi})$
- $\theta$ is trained weights
- $\xi$ is exponentially moving average of $\theta$ and sg is stop gradient
- $f_\theta$ is discarded, $y_\theta$ is used as image representation
- ![byol](images/byol.jpg)



