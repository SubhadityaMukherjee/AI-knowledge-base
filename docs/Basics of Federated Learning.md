---
title: Basics of Federated Learning
---

# Basics of [Federated Learning](Federated%20Learning.md)
1. Get data (Hopefully a lot)
2. Preprocess (aka clean up) the data
3. Find/create an architecture
4. Train the model using the data(1) and the architecture(3). This step is done once. And then periodically updated as the data changes over time. Keep this in mind.
5. Push the model out to n users
6. Collect data about how well the model did. (Bye bye privacy)
7. Send this data back to the main model.
7 (#new). Find the difference between the original model and the personalized one's parameters. Do this for multiple users. Remove identifiable information.
7.1 (#new). Aggregate (eg. average) the information and then send that to the main model
8. Retrain the model on new data




















































































