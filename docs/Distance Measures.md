---
title: Distance Measures

tags: 
---

# Distance Measures
- [[Euclidean Distance]]
- [Cosine Similarity](Cosine%20Similarity.md)
- [[Hamming Distance]]
- [[Manhattan Distance]]
- [[Chebyshev Distance]]
- [[Hausdorff Distance]]
- [[Chi Squared Distance]]
- [[Bhattacharya Distance]]
 - [[Minkowski Distance]]
- [[Jaccard Distance]]
    - <h1>Haversine</h1>
        - Haversine distance is the distance between two points on a sphere given their longitudes and latitudes
        - The main difference is that no straight line is possible since the assumption here is that the two points are on a sphere.
        - ssumed the points lie on a **sphere**
        - As you might have expected, Haversine distance is often used in navigation
        - calculate the distance between two countries when flying between them
        - Note that it is much less suited if the distances by themselves are already not that large. The curvature will not have that large of an impact.
    - <h1>Sørensen-Dice Index</h1>
        - very similar to Jaccard index
        - Although they are calculated similarly the Sørensen-Dice index is a bit more intuitive because it can be seen as the percentage of overlap between two sets, which is a value between 0 and 1
        - overstate the importance of sets with little to no ground truth positive sets
        - As a result, it could dominate the average score taken over multiple sets
        - It weights each item inversely proportionally to the size of the relevant set rather than treating them equally.


