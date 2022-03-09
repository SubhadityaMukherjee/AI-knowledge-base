# Layers

## Notation
- Grad of a function f wrt A :  $\nabla_Af$
- Neuron Pre activation : Z
- Activations : Y
- Tensor shape : (w,h,c)
- Matrix multi : $A\cdot B$
- Hadmard prod (coeff wise) : $A \circ B$
- Conv : $A\ast B$

## Perceptron
- $f(x)=sign(\Sigma _i w_ix_i +b) = sign(\mathbf{w^Tx}+b)$
	- $sign(x) = \begin{cases} 1 & x\geq0 \\ 0 & otherwise\end{cases}$
![[Pasted image 20220304121008.png]]
- computational graph![[Pasted image 20220304121221.png]]
- Multi layer
	- Stack multiple perceptrons
	- $\begin{align} \\& h_0 = x h1= sign(\mathbf{w_1^T}+b_1) \\ &…\\& h1= sign(\mathbf{w_{L-1}^T}+b_L) \end{align}$

## Dense
- Weighted linear comb
- Forward
	- $z = W\cdot x + b$ , $y=g(z)$
- Backward
	- $\delta = g'(z)\circ \nabla_y E$
	- $\nabla_WE = \delta \cdot x^T$ , $\nabla_bE = \delta$
	- $\nabla_xE = W^T\cdot \delta$

## Pooling
- Summarize low level features
- Reduce input dims
- Max/Avg
- Too much pooling reduces performance
	- Multiple convs first 
- Max pool + dilated/strided convs control effective receptive field size

## [[Conv]]

## Skip Connection
- ![[Pasted image 20220306120520.png]]
- $x_i = F(x_{i-1}) + x_{i-1}$
- [[Effect_Of_Depth]]
- Previous layer gradient carried to next module untouched -> loss surface is smoother

## Dense Skip Connections
- $x_i = F(x_0,x_1 ,… ,x_{i-1})$
	- F : 3x3 conv + ReLU -> k feature maps
	- no of feature maps : $k(i-1) + k_0$ where k is growth rate (hyperparam)

## Recurrent
- memory through state persisted between timesteps
	- operation invariant to the sequence
	- reduces no of params needed
- variable sized inputs and outputs : encoder decoder
- Three weight matrices and two bias vectors. 
- $h_t = \sigma_h(W_{hh}h_{t-1} + W_{xh}x_t + b_h)$
- $y_t = \sigma_y(W_{hy}h_t + b_y)$
- Stateful : hidden state kept across batches of inputs
- Activation usually sigmoid or tanh
- BPTT
	- ![[Pasted image 20220306185944.png]]![[Pasted image 20220306190603.png]]
	- #gradients 
		- If eigen decomposition $W = Q\wedge^tQ$, then $h_t = Q^T\wedge^tQ$
		- If less than 0 then will converge to 0 or if bigger then will explore to infinity -> long sequences
		- Element wise clipping #tricks 
			- Clip if bigger than value
		- Norm clipping
			- Clip if $||g|| >v$ set $g = \frac{gv}{||g||}$
			- v can be decided by trial and error

## Long Short Term Memory (LSTM)
- Smaller chance of exploding or vanishing #gradients 
- Better ability to model long term dependencies
- Gated connections
- Splitting state into parts -> output pred and feature learning
- Gates
	- Forget $g_f = \sigma(W_{hf}h_{t-1} + W_{xf}x_t + b_f)$
		- How much of the previous cell state is used
	- Input $g_i = \sigma(W_{hi}h_{t-1} + W_{xi}x_t + b_i)$
		- How proposal is added to the state
	- Output $g_o = \sigma(W_{ho}h_{t-1} + W_{xo}x_t + b_o)$
		- Component wise products
- Hidden state 
	- $C_t$ to model cross timestep dependencies
		- Cell state proposal : $\hat C = tanh(W_{hc}h_{t-1} + W_{xc}x_t + b_c)$
		- Final cell state : $C_t = g_f \cdot C_{t-1} + g_i\cdot \hat C$
	- $h_t$ to predict output
		- $h_t = g_o \cdot \sigma_y(C_t)$

## Gated Recurrent Unit (GRU)
- Two gates, sigmoid
	- Reset : $g_r = \sigma(W_{hr}h_{t-1} + W_{xr}x_t + b_r)$
	- Update :  $g_u = \sigma(W_{hu}h_{t-1} + W_{xu}x_t + b_u)$
- Hidden state proposal
	- $\hat h_t = tanh(W_{xh}x_t + W_{hh}g_r\cdot h_{t-1} + b_h)$
- Final hidden state
	- Linear interpolation between last hidden state and proposal
	- $h_t = (1-g_u)\cdot h_{t-1} + g_u \cdot \hat h_t$

## Convolutional RNN
- $h_t = \sigma_h(W_{hh}\star h_{t-1} + W_{xh}\star x_t + b_h)$
- $y_t = \sigma_y(W_{hy}\star h_t + b_y)$
- $\star$ is spatial conv
- 5D shapes -> [samples, timesteps, width, height, channels]
- Very memory intensive
