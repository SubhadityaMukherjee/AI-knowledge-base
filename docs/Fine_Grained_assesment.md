---
title: Fine Grained assesment

tags: usermodel learning
date modified: Wednesday, October 12th 2022, 2:18:50 pm
date created: Wednesday, October 12th 2022, 2:18:48 pm
---

# Fine Grained Assesment
```toc
```

## Counting Learning Events
- We also assumed that a step is the product of one or more learning events, and defined a [Learning_Event](Learning_Event.md) to be a mental event based on a [Knowledge_Component](Knowledge_Component.md). Learning events and knowledge components are not directly observable, but steps are.
- Mastery really means the probability that a [Knowledge_Component](Knowledge_Component.md) will be applied when it should be applied. If the student's competence was frozen instead of constantly changing due to learning and forgetting, then mastery could be estimated by counting the number of times a [Knowledge_Component](Knowledge_Component.md) was applied and dividing by the number of times it should have been applied. Thus, we need to discuss three issues: (1) How to detect applications of a [Knowledge_Component](Knowledge_Component.md), (2) how to detect times when a [Knowledge_Component](Knowledge_Component.md) should have been applied, and (3) how to adjust for instruction, learning and forgetting.

## Counting Failures
- Counting only the successful applications of a [Knowledge_Component](Knowledge_Component.md) is not enough; we need to know how many times the student failed to apply it as well.
- One approach is to detect failed attempts at steps. Suppose for simplicity that there is a one-to-one correspondence between a step and a [Learning_Event](Learning_Event.md)
- If the student fails to make the step, then the student must lack the knowledge that underlies the [Learning_Event](Learning_Event.md).
