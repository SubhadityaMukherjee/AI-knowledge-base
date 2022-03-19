# Triplet Loss
- Given an achor, pull similar closer and push dissimilar away
- Face recog [[FaceNet]]
- Anchor, positive sample are neigbors while neg isnt
- ![[Pasted image 20220310200651.png]]
- For each triplet, this condition must hold $$||f(x^a) - f(x^p)||^2 + \alpha \gt f(x^a) - f(x^n)||^2$$
- $\alpha$ is a margin b/w positive and neg
<<<<<<< HEAD
- Loss to minimize $$L(\theta) = \Sigma_i^n||f(x^a) - f(x^p)||^2 + f(x^a) - f(x^n)||^2 + \alpha$$



## Backlinks
* [[Loss Functions]]
=======
- Loss to minimize $$L(\theta) = \Sigma_i^n||f(x^a) - f(x^p)||^2 + f(x^a) - f(x^n)||^2 + \alpha$$## Backlinks
* [[LossFunctions]]
>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
	* [[Triplet Loss]]
* [[Semi Supervised]]
	* [[Triplet Loss]]

<<<<<<< HEAD
## ...
=======
>>>>>>> 1dd38fd29e2ea89a9d6c64b1ecd9e965740dd3c9
