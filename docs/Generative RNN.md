---
title: Generative RNN

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:41 am
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Generative RNN
- initial sequence is used as seed and output is sampled 
    - random or argmax to sample
    - normally not taking argmax but sample with respective [[Softmax]] probabilities -> allows to generate something different than input
- new output is used as seed to generate next 
- repeat until termination criterion

