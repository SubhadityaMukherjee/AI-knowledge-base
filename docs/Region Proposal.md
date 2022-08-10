---
title: Region Proposal
tags: architecture 
date modified: Thursday, August 11th 2022, 12:32:47 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Region Proposal
- region proposal generation that shares full-image convolutional [features](Features.md) with the detection network,
- nearly cost-free region proposals
- haring convolutional [features](Features.md) with the down-stream detection network
- simultaneously predicts object bounds and objectness scores at each position

