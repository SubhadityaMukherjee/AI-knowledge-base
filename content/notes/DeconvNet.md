---
title: DeconvNet

tags: explainability 
date modified: Wednesday, October 12th 2022, 4:42:12 pm
date created: Wednesday, October 12th 2022, 4:17:49 pm
---

# DeconvNet
```toc
```

---

title: DeconvNet

tags: explainability
date modified: Wednesday, October 12th 2022, 4:18:00 pm
date created: Wednesday, October 12th 2022, 4:17:49 pm
---

# DeconvNet
```toc
```
- ![Pasted image 20221012161759](images/Pasted%20image%2020221012161759.png)
- DeconvNet is a calculation of a backward convolutional network that reuses the weights at each layer from the output layer back to the input image
- The employed mechanisms are deconvolution and unpooling, which are especially designed for CNNs with convolutions, max-pooling, and Rectified Linear Units (ReLUs). The method makes it possible to create feature maps of an input image that activates certain hidden units most, linked to a particular prediction
- With their propagation technique, they identified the most responsible patterns for this output. The patterns are visualized in the input space
- DeconvNet is limited to max-pooling layers, but the unpooling uses an approximate inverse

