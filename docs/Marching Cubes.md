---
title: Marching Cubes
tags: visualization
---

# Marching Cubes
- 3D version of [[Marching Squares]]
- Cell consists of 8 node values: (i+{0,1}, j+{0,1}, k+{0,1})
- 1. Consider a cell
- 2. Classify each vertex as inside or outside
- 3. Build an index
- 4. Get edge list from table[index]
- 5. Interpolate the edge location
- $$x = i + \frac{(c-v[i])}{(v[i+1]-v[i])}$$
- 6. Compute gradients
- [[Finite Differences]] Central
- 7. Consider ambiguous cases
- [[Midpoint Decider]]
- [[Asymptotic Decider]]
- 8. Go to next cell
- ![im](assets/Pasted%20Image%2020220417235937.png)

## Limitations
- Produces many triangles
- Cannot represent sharp edges
- Produces “ugly” (thin) triangles
- Produces ringing artifacts!






















































