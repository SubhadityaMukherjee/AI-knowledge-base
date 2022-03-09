# Activation Functions

## [[Initialization]]

## Sigmoid
- $\sigma(x) = \frac{1}{1+exp(-x)}$
- $\frac{d\sigma}{dx}(x) = \sigma(x)(1-\sigma(x))$
	- max : 0.25
- Logistic
- Xavier/Glorot init
- RNN : Hidden
- Bernoulli Distribution over a binary variable

## Relu
- $ReLU(x) = max(0,x)$
- $\frac{d}{d_x}ReLU(X) = \begin{cases}0 & x \geq 0 \\ 1 & otherwise \end{cases}$
- He init
- MLP, CNN : Hidden
	- Leaky
		- $max(0.01x,x)$
	- Parametric
		- $max(\alpha x,x)$

## Tanh
- $\frac{e^x-e^{-x}}{e^x+e^{-x}}$
- RNN : Hidden
- Xavier/Glorot init 

## Softmax
- Output : probabilities
- $\frac{e^x}{\Sigma_k(e^x_k)}$
- Softer argmax (0,1)
- Multinoulli

## Softplus
- $\ln(1+e^x)$

## Swish
- $x\cdot sigmoid(x)$

## Refs
- [mlmastery](https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/)
