---
title: CTC

tags: loss 
---

# CTC
- [Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks](https://www.cs.toronto.edu/~graves/icml_2006.pdf)
- Many real-world sequence learning tasks require the prediction of sequences of labels from noisy, unsegmented input data
- Recurrent neural networks (RNNs) are powerful sequence learners that would seem well suited to such task
- hey require pre-segmented training data, and post-processing to transform their outputs into label sequences, their applicability has so far been limited
- temporal classification
- label unsegmented sequences directly
- probabilistic principles
- TIMIT speech corpus






















## Backlinks

> - [Listen Attend Spell](Listen Attend Spell.md)
>   - bypass the conditional independence assumptions of [[CTC]], and show how they can learn an implicit language model that can generate multiple spelling variants given the same acoustics
>   - producing character sequences without making any independence assumptions between the characters is the key improvement of LAS over previous end-to-end [[CTC]] models
>    
> - [Speech Recognition](Speech Recognition.md)
>   - combination of the deep bidirectional LSTM recurrent neural network architecture and a modified Connectionist Temporal Classification ([[CTC]]) objective function

_Backlinks last generated 2022-07-26 20:33:15_
