# Multiple Local Minima

# Saddle Points

# Vanishing/exploding #gradients
- Ill conditioning - Something like a pit of despair
- $\nabla_xE  = W^T(g'(a)\circ \nabla_y E)$
	- $g' = 1-g^2$
- Active neurons saturate -> prevent error #backprop
- $g(a) \approx 1 \rightarrow \nabla_xE \approx 0$
- W is initialized with random values << 1 -> gradient decays exponentially in each layer (max eigenvalue of weight matrix)
- Solutions
	- [[Regularization]] , [[Optimizers]] , [[Architectures]]

# Image Data
- Cant use MLPs 
	- Too many weights to learn
	- No translation equi-invariance

# Fitting
- Bayes risk
	- Minimal expected risk over set of all functions $R_B = min_{f\in y^X} R(f)$
	- If minimized -> Best possible function
	- Capacity of hypothesis space 
		- If low, $\mathscr{F}  = R(f) - R_B$ is large : Underfitting (Huge difference between best risk and current risk)
		- If high, $\mathscr{F}  = R(f) - R_B$ is small : Overfitting (Tiny difference between best risk and current risk)

# Freedom
- (N, D, P) N samples,  D degrees of freedom
- If N<D , then ill posed 
- Need N >> D
- If P learnable params , $P<N$ : underspecified
- If $P >> N$ : overparameterized
- No of params not a good indicator of overfitting
- Solution : [[Regularization]]