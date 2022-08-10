---
tags: temp
date modified: Wednesday, August 10th 2022, 11:41:32 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

title: BYOL Loss

tags: loss

---

# [BYOL](BYOL.md) Loss
- Similarity loss between $q_\theta (z_\theta)$ and $sg(z^{'}_{\xi})$
- $\theta$ is trained weights
- $\xi$ is exponentially moving average of $\theta$ and sg is stop gradient
- $f_\theta$ is discarded, $y_\theta$ is used as image representation
- ![byol](assets/byol.jpg)

