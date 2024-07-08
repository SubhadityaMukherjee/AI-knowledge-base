---
toc: true
title: Double Descent

categories: ['optimizer']
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Double Descent
- When increasing the model size or the number of epochs, performance on the test set initially improves, then worsens but then again starts to improve and finally saturates.  
- This phenomena is against conventional wisdom, because the test error should not be decreasing again after increasing.
- occurs often in the over-parameterization regime
    - models which have a lot of parameters
    - models that have huge complexity
- ![](images/Pasted%20image%2020240620151512.png)
