---
title: GPT3

tags: architecture 
date modified: Wednesday, August 10th 2022, 11:41:28 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# GPT3
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- shows that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches
- autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting
- without any gradient updates or fine-tuning
- on-the-fly reasoning or domain adaptation
- methodological [issues](Issues.md) related to training on large web corpora
- can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans

