---
title: Amdahl's Law
tags: parallel
date modified: Thursday, August 11th 2022, 12:32:57 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Amdahl's Law
- Maximum expected improvement to an overall system when only part of the system is improved
- Theoretical maximum speedup using multiple processors
- $$Speedup = \frac{\text{Execution time before improvement}}{\text{Execution time after improvement}}$$
- $$Speedup = ((1-f_{E})+(\frac{f_{E}}{f_{I}}))^{-1}$$
	- $f_E$ is fraction enhanced
	- $f_{I}$ is factor of improvement
	- $S_{e}$ is speedup enhanced
- $$ExecutionTime_{new} = ExecutionTime_{old}\times [(1-f_{E})+f_{E}/S_{e}]$$
- $$MaximumSpeedupp = n/(1+(n-1)f )$$
	- n is no of processors

## Backlinks

> - [SIMD](SIMD.md)
>   - Limited by [[Amdahl's Law]]

_Backlinks last generated 2022-10-04 13:01:19_
