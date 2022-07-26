---
title: Tacotron 2

tags: architecture 
---

# Tacotron 2
- [[Spectrogram|Natural TTS Synthesis by Conditioning WaveNet on Mel [Spectrogram]] Predictions](https://arxiv.org/abs/1712.05884)
- Tacotron 2
- speech synthesis directly from text
- recurrent sequence-to-sequence feature prediction network that maps character embeddings to mel-scale spectrograms
- modified WaveNet model acting as a vocoder to synthesize timedomain waveforms from those spectrograms
- MOS
- evaluate the impact of using mel-spectrograms as the input to WaveNet instead of linguistic, duration, and F0 [[Features|features]]
- using a compact acoustic intermediate representation enables significant simplification of the WaveNet architecture






















