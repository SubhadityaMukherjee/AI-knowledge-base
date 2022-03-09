## Res Net
- Deeper Networks have issues because of vanishing #gradients
- Propagate gradients forward for deeper networks
- Skip connections
- output of F(x) has the same dims as x -> add
- If only spatial dims match (aka not channels) -> concat
- less params than VGG
- [[Layers#Skip Connection]]