---
title: AdamW

tags: optimizer 
date modified: Thursday 11th May 2023, Thu
date created: Thursday 11th May 2023, Thu
---

# AdamW
```toc
```

- @loshchilovDecoupledWeightDecay2019

## Adam Features
- why use the same learning rate for every parameter, when we know that some surely need to be moved further and faster than others
- Since the square of recent gradients tells us how much signal we're getting for each weight, we can just divide by that to ensure even the most sluggish weights get their chance to shine
- with a little tweak to keep early batches from being biased
- Few research articles used it to train their models, new studies began to clearly discourage to apply it and showed on several experiments that plain ole SGD with momentum was performing better.
- ![[images/Pasted image 20230511133235.png]]
- ![[images/Pasted image 20230511133244.png]]
- Ilya Loshchilov and Frank Hutter pointed out in their paper that the way weight decay is implemented in Adam in every library seems to be wrong, and proposed a simple way (which they call AdamW) to fix it
- PhD student Jeremy Bernstein has pointed out that the claimed convergence problems are actually just signs of poorly chosen hyper-parameters, and that perhaps amsgrad won't fix things anyway. Another PhD student, Filip Korzeniowski, showed some early results that seemed to support this discouraging view of amsgrad.

## Weight Decay Vs L2 Regularization
- L2 regularization is a classic method to reduce over-fitting, and consists in adding to the loss function the sum of the squares of all the weights of the model, multiplied by a given hyper-parameter
```python
final_loss = loss + wd * all_weights.pow(2).sum() / 2
```
- where wd is the hyper-parameter to set
- This is also called weight decay, because when applying vanilla SGD it's equivalent to updating the weight like this
```python
w = w - lr * w.grad - lr * wd * w
```
- In this equation we see how we subtract a little portion of the weight at each step, hence the name decay
- So why make a distinction between those two concepts if they are the same thing
- The answer is that they are only the same thing for vanilla SGD, but as soon as we add momentum, or use a more sophisticated optimizer like Adam, L2 regularization (first equation) and weight decay (second equation) become different
- When using the Adam optimizer, it gets even more different: in the case of L2 regularization we add this $wd\times w$ to the gradients then compute a moving average of the gradients and their squares before using both of them for the update. Whereas the weight decay method simply consists in doing the update, then subtract to each weight.
- And after experimenting with this, Ilya Loshchilov and Frank Hutter suggest in their article we should use weight decay with Adam, and not the L2 regularization that classic deep learning libraries implement.
- Inside the step function of the optimizer, only the gradients are used to modify the parameters, the value of the parameters themselves isn't used at all
- It still has to be done after the gradients are computed
- the optimizer should have been set with wd=0 otherwise it will do some L2 regularization, which is exactly what we don't want
- loop over all the parameters and do our little weight decay update
- [[Amsgrad]]

