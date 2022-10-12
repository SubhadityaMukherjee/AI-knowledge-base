---
tags: temp
title: EEG Cluster Testing
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# [[EEG]] Cluster Testing
- If done for each point, same test repeated and false positives increase
- eg: t test in each electrode
- A result is more believable if it occurs in a set of adjacent channels:  
	- Threshold data of statistical test  
	- Compute clusters  
	- Threshold randomized data  
	- Compute clusters for 100 or so distr of randomized data
	- Decide if its rare
- $$sumT = \text{sum of all t stats}$$
- ![[assets/Pasted image 20220502155613.png|im]]
	- There was a significant difference between easy and more difficult trials between 712 ms post-stimulus and 768 ms post-stimulus. This difference was initially localized to a few central electrodes but over time spread out more posteriorly. This is consistent with previous studies that have shown

## Backlinks
> - [[[EEG]] Statistical Analysis](EEG Statistical Analysis.md)
>   - [[EEG Cluster Testing]]

_Backlinks last generated 2022-10-04 13:01:19_
