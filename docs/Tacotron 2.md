---
title: Tacotron 2

tags: architecture 
date modified: Wednesday, August 10th 2022, 11:41:23 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Tacotron 2
- [Natural TTS Synthesis by Conditioning WaveNet on Mel [Spectrogram](Spectrogram.md) Predictions](<https://arxiv.org/abs/1712.05884)>
- Tacotron 2
- speech synthesis directly from text
- recurrent sequence-to-sequence feature prediction network that maps character embeddings to mel-scale spectrograms
- modified WaveNet model acting as a vocoder to synthesize timedomain waveforms from those spectrograms
- MOS
- evaluate the impact of using mel-spectrograms as the input to WaveNet instead of linguistic, duration, and F0 [features](Features.md)
- using a compact acoustic intermediate representation enables significant simplification of the WaveNet architecture

