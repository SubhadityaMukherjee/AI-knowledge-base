---
title: X_Vectors
tags: architecture
---
# X_Vectors
- [WaveGlow: a Flow-based Generative Network for Speech Synthesis](https://arxiv.org/abs/1811.00002)
- flow-based network capable of generating high quality speech from mel-spectrograms
- combines insights from [Glow](GLOW.md) and WaveNet in order to provide fast, efficient and high-quality audio synthesis, without the need for auto-regression
- mplemented using only a single network, trained using only a single cost function: maximizing the likelihood of the training data, which makes the training procedure simple and stable
- more than 500 kHz on an NVIDIA V100 GPU













