---
title: Akaike Information Criterion

tags: loss 
date modified: Wednesday, August 10th 2022, 4:11:57 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Akaike Information Criterion
- Considers goodness-of-fit to the data and penalizes complexity of the model
- $$AIC=−2log⁡(L)+2q$$
- where:
- L: likelihood function for a particular model
- q: number of variables of this model
- If error terms $\epsilon$ follows [Normal Distribution](Normal%20Distribution.md) , expected value 0 + constant variance $$AIC = \frac{1}{\eta \sigma^{2}}(RSS + 2p \hat \sigma^2)$$

