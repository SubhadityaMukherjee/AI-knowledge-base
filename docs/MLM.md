---
title: MLM

tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:41 am
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# MLM (Masked Language Modeling)
- [from](https://publish.obsidian.md/fabian-groeger/Machine+Learning+%26+Deep+Learning/Deep+Learning/Architectures/Transformers/Masked+LM)
- 15% of the words in each sequence are replaced by `[MASK]`
- model tries to predict original values of the masked words
- uses the context provided by the other non-masked words in the sequences
- [[loss]] function only considers the predictions of the masked words, ignores non-masked ones
    - leads to slower convergence than with directional models
- additions to standard architecture:
    - classification layer on top of the encoder output
    - multiplying the encoders output vectors with the embedding matrix -> transforms them into the vocabulary dimension
    - calculating probability of each word in the vocabulary using [[Softmax]]

## Backlinks
> - [[MLIM]]
>   - [[.md|MLM]] + RECON losses apply only to the masked text/image areas and measure reconstructed text and image quality.

_Backlinks last generated 2022-08-10 16:56:31_
