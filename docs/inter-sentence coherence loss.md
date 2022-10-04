---
title: inter-sentence coherence loss

tags: loss
date modified: Thursday, August 11th 2022, 12:32:43 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Inter-sentence Coherence Loss
- inter-sentence coherence loss called sentence-order prediction (SOP) is used.
- The key problem with this loss is that it merges topic prediction and coherence prediction into one task.
- Intuitively, we can argue that topic prediction is much easier than coherence prediction. The consequence is that when the model discovers this, it can focus entirely on this subtask, and forget about the coherence prediction task; actually taking the path of least [[Resistance|resistance]]. The authors actually demonstrate that this is happening with the NSP task, replacing it within their work with a sentence-order prediction or SOP task.

## Backlinks

> - [ALBERT](ALBERT.md)
>   - [[inter-sentence coherence loss]]

_Backlinks last generated 2022-10-04 13:01:19_
