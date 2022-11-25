---
title: Global and Sliding Window Attention

tags: architecture 
date modified: Monday, October 10th 2022, 2:02:26 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Global and [Sliding_Window_Attention](Sliding_Window_Attention.md)
- [Sliding_Window_Attention](Sliding_Window_Attention.md) and [Dilated_Sliding_Window_Attention](Dilated_Sliding_Window_Attention.md) are not always enough
- global [attention](Attention.md)” on few pre-selected input locations.
- This [attention](Attention.md) is operation symmetric: that is, a token with a global [attention](Attention.md) attends to all tokens across the sequence, and all tokens in the sequence attend to it
- ![Pasted image 20220621181106](images/Pasted%20image%2020220621181106.png)

