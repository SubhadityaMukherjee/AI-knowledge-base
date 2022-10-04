---
tags: temp
date modified: Thursday, August 11th 2022, 12:32:57 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

---

title: BYOL Loss

tags: [[loss]]

---

# [[BYOL]] Loss
- Similarity [[loss]] between $q_\theta (z_\theta)$ and $sg(z^{'}_{\xi})$
- $\theta$ is trained weights
- $\xi$ is exponentially moving average of $\theta$ and sg is stop gradient
- $f_\theta$ is discarded, $y_\theta$ is used as image representation
- ![[assets/byol.jpg]]

## Backlinks

> - [BYOL](BYOL.md)
>   - [[BYOL Loss]]

_Backlinks last generated 2022-10-04 13:01:19_
