## Basic RNN Architectures
![[Pasted image 20220307171009.png]]

### Stacking RNN
- Deeper 
- Each level -> output is seq of features that is input at next set of layers in the hierarchy
- ![[Pasted image 20220307171139.png]]

### Bi Directional RNN
- Not causal
- Looks at the forward timestep dimension and also the backward
	- Both combined to make a prediction
- ![[Pasted image 20220307171243.png]]