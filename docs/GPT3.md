---
title: GPT3

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:53 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# GPT3
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- shows that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches
- autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting
- without any gradient updates or fine-tuning
- on-the-fly reasoning or domain adaptation
- methodological [[Issues|issues]] related to training on large web corpora
- can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans

## Backlinks

> - [CLIP](CLIP.md)
>   - can be applied to any visual classification benchmark by simply providing the names of the visual categories to be recognized, similar to the “zero-shot” capabilities of [[GPT]] and [[GPT3]]
>    
> - [DALL-E](DALL-E.md)
>   - based on the [[GPT3]]
>    
> - [Benchmark LLM](Benchmark LLM.md)
>   - From [[GPT3]] to [[PaLM]], the state-of-the-art performance on natural [[language]] tasks is being pushed forward with every new large [[language]] model
>    
> - [GELU](GELU.md)
>   - Used in [[GPT3]], [[Transformer]], [[Vision Transformer]], [[BERT]]

_Backlinks last generated 2022-10-04 13:01:19_
