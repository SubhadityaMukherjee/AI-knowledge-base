# Architectures

## Le Net
- Spatial dims reduce with depth, no of neurons increase
- ![[Pasted image 20220306115954.png]]

## Alex Net
- Dropout + Relu 
- No of filters increase according to depth
- ![[Pasted image 20220306120121.png]]

## Inception

### V1
- Conv at different filter scales to find different kinds of features -> stack them up
- ![[Pasted image 20220306120214.png]]

### V2/V3
- nxn conv -> 1xn followed by nx1 conv
- ![[Pasted image 20220306121513.png]]

## Vgg
- Deeper AlexNet
- Object detection and Image captioning
- 5x5 -> two 3x3
- No of filters increase according to depth
- No of filters : increase by power of two
- Filter size : Odd numbers
- SGD + LR Schedule

## Res Net
- Deeper Networks have issues because of vanishing #gradients
- Propagate gradients forward for deeper networks
- Skip connections
- output of F(x) has the same dims as x -> add
- If only spatial dims match (aka not channels) -> concat
- less params than VGG
- [[Layers#Skip Connection]]

## Dense Net
- Generalized ResNet
- Skip connections inside the Dense block itself
- [[Layers#Dense Skip Connections]]
- Transition layer -> Dense -> 1x1 conv , 2x2 avg pool -> Dense

## Mobile Net
- [[Conv#Depthwise Separable]]

## Xception
- Only use Depth wise separable convs + Inception modules
- Cross channel and spatial correlations can be decoupled completely

## Nasnet
- Neural Architecture Search
- Controller RNN produces architectures and evaluated until convergence

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

## Temporal Conv
- FCN + [[Conv#Causal 1D Conv]] + Residual

## Seq2Seq
- RNNs
- Encoder Decoder
- Long term dependency issues
	- Even if hidden state vector has a high dimensionality, cannot hold all info

## Transformer
- Encoder Decoder
- Auto regressive : decoder outputs fed back as inputs to decoder
- [[Attention]]
- ![[Pasted image 20220307183126.png]]
- Feed forward blocks, are two Dense MLPs with relu. Residual connections in between
- Embedding layers transform between 1 hot and vector rep

## BERT
- Bidirectional Encoder rep from transformers
- Self supervised
- Masked language modeling, next sentence prediction
- ![[Pasted image 20220307183916.png]]
- [CLS] : start of classification task, [SEP] between sentences, [MASK] : masked token

## GPT
- Pretrained using unsupervised learning and finetuned
- [[LossFunctions#Log Likelihood Loss]]
- ![[Pasted image 20220307184212.png]]