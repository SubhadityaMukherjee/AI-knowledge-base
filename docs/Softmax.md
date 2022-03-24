# Softmax
- Output : probabilities
- $$\frac{e^{\frac{x}{T}}}{\Sigma_k(e^{\frac{x_{k}}{T}})}$$
- Softer argmax (0,1)
- Multinoulli

## T is the Temperature
- Higher the T -> Softer it the distribution. Aka less confident about distribution
- Lower -> Harder. More confident



## Backlinks
* [[Activation Functions]]
	* [[Softmax]]
* [[Recurrent]]
	* [[Softmax]] but on every output vector simultaneously
* [[Uncertainty]]
	* Most networks are overconfident - [[Softmax]] confidences do not have a good probabilistic interpretation. Wrong predictions with more confidence
* [[Uncertainty Classification]]
	* Use [[Softmax]] or [[Sigmoid]]

## ...