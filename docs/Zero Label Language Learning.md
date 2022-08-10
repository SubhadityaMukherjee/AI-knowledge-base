---
title: Zero Label Language Learning

tags: temp
date modified: Thursday, August 11th 2022, 12:32:43 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Zero Label Language Learning
- [Towards Zero-Label Language Learning](https://arxiv.org/abs/2109.09193)
- [Unsupervised Data Generation](Unsupervised%20Data%20Generation.md)
- SuperGLUE
- Treat LMs as few-shot generators (rather than few-shot learners)
- Create prompts with <sample, label> pair(s)
- Ask the model to generate more for the same label
- The emphasis is on the labelled data generation (rather than inference)
- The new idea is about generating more data and going with conventional route
- This paper confirms all the above by introducing UDG using LMs, even for complex higher-order tasks and empirically shows classical fine-tuning with more data works better.

