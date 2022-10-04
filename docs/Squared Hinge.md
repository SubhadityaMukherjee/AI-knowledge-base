---
title: Squared Hinge
tags: loss
date modified: Thursday, August 11th 2022, 12:32:45 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Squared Hinge
- [[Hinge Loss]]
- problems involving yes/no (binary) decisions and when you’re not interested in knowing how certain the classifier is about the classification
- [[Tanh]] for last layer
- maximum margin

$$\mathrm{sum}\left( \left( \mathrm{max}\left( 0, 1 - y \cdot ŷ \right) \right)^{2} \right)$$

