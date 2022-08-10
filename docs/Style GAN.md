---
title: Style GAN

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:45 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Style GAN
- builds the picture layer after layer, where the [layers](Layers.md) get bigger and more accurate
- For example, the first layer is 4 by 4 pixels, the second 8 by 8, and so on
- every new layer can benefit from the less granular results of the previous ones
- better separate the generator and the discriminator, which ensures less dependence of the generator on the training set
- his allows one to, for example, reduce discrimination in the generated pictures

