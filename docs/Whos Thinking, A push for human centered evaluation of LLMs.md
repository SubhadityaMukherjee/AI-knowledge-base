---
title: Whos Thinking, A push for human centered evaluation of LLMs

tags: explainability 
date modified: Wednesday 24th May 2023, Wed
date created: Wednesday 24th May 2023, Wed
---

# Whos Thinking, A Push for Human Centered Evaluation of LLMs
```toc
```

- @dattaWhoThinkingPush2023

## ABSTRACT
- In this paper, we draw parallels between the relatively mature field of XAI and the rapidly evolving research boom around large language models (LLMs)
- Specifically, we argue that humans' tendencies— again, complete with their cognitive biases and quirks—should rest front and center when evaluating deployed LLMs

## Large Language Models
- Current LLM evaluation mechanisms include quantitative metrics measuring notions of accuracy (how similar are the generated outputs to the expected outputs), robustness (how resilient is the model to transformations of the input), calibration (how meaningful are the generated probabilities in respect to uncertainty), efficiency (what are the energy, carbon, and time costs for training and inference) and more [35].
- There are substantial environmental costs associated with the volume of computational power required for training and inference [6, 49]
- Counterfactual fairness [24] examines how perturbing the demographic signals of existing test examples can change the performance of the model (e.g. "He worked at the local hospital" versus "She worked at the local hospital")
- other concerning forms of biases such as stereotypical associations, erasure, and over-representation in the semantics of its output [35, 38]
- LLMs have been shown to produce toxic outputs.
- LLMs often suffer from factual errors—they can "hallucinate" information [50] by providing very confident-sounding but entirely false responses
- Chatbot LLMs have also been found to engage in disturbingly emotional personal conversations when session lengths are not limited [47].
- There are also privacy concernswork has shown that LLMs are susceptible to training data leakage under adversarial attack [11].

## PARALLELS BETWEEN XAI AND LLMS
- LLM outputs are often meant for some downstream decision or task—what email to send to your client, what quick summary of an important document you will read, what answer is provided for a pertinent question
- Advocates push for first identifying a specific use case, then understanding the types of transparency useful and relevant for each stakeholder in that context, then designing the explanation method with these learnings held front and center, and finally evaluating how helpful the explanation was for specific tasks through practitioner user studies
- A system is valid if it does what it purports to do. If it doesn't, it is likely because there are issues of alignment between the intent of the system builder and the property the algorithm optimizes [40].

## Cognitive Engagement
- Cognitive effort is a form of labor, and unsurprisingly, people tend to favor less demanding forms of cognition and other mental shortcuts [18, 51].
- Unfortunately, this human tendency can lead to unintended or dangerous outcomes because humans are susceptible to a wide variety of cognitive biases such as confirmation bias
- Confirmation bias [41]
- refers to the interpreting of new evidence in ways that confirm one's existing beliefs
- For XAI, this manifests as practitioners only superficially examining explanations instead of digging deeply, leading to over-trust, misuse, and a lack of accurate understanding of the outputs [31]
- Forcing users to cognitively engage through some small task before showing a system's output yielded the highest performance in a comparative study [21]
- Train conductors in Japan famously point and call out important information on their journeys—a cognitive forcing method which has reduced human errors by nearly 85% [45].
- Realistically, how much will users actually cognitively engage with the magnitude of generated outputs to ensure that they are correct and aligned with their intentions?

## Mental Model Matching
- A user's mental model [42] of a technology is their internal understanding of how a technology works.
- People rely heavily on their mental models of technology to make decisions
- It has been found that XAI stakeholders use their mental models of XAI to decide when to use the technology [10], to evaluate how much to trust the outputted explanations [10, 20, 22], and to make sense of any results [22, 30]
- While ML practitioners may have had access to specialized training on how LLMs work, this is decidedly not the case for the vast majority of the general population
- How a general user believes an LLM to work may be very different from how it actually works, and this mismatch can be dangerous
- It is not difficult to imagine frightening scenarios where users anthropomorphize or deify an LLM chatbot, understanding it to be a "magical" source of ground truth. This could very quickly lead to conspiracy theories and the legitimization of disinformation campaigns [see, e.g., 23]

## Use Case Utility
- XAI and LLMs are often tools for accomplishing some other goal.
- Very limited work has explored the utility of LLMs in use-case– specified user studies, but a user study on Microsoft/Github's Copilot [1], an LLM-based code generation tool, found that it "did not necessarily improve the task completion time or success rate" [52]
- LLM outputs often sound very confident, even if what they are saying is hallucinated [50]
- When the user inquires about the incorrectness, they also have a documented tendency to argue that the user is wrong and that their response is correct. In fact, some have called LLMs "mansplaining as a service" [34]
- This can make it more difficult for humans to implement cognitive checks on LLM outputs.
- While some recent LLM work has outlined categories of failure modes for LLMs based on the types of cognitive biases use [29], we push for greater work in this field

## WHY IS THIS IMPORTANT
- the potential scale of LLM usage is massive as a fundamentally lower-level ML-
based building block than XAI
- ChatGPT [43] set historic records for its customer growth, with over 100 million users in its first 2 months [2].
- Unlike XAI, whose users are largely technical practitioners [7] focusing on one pipeline, LLMs are often designed for public use and are meant to help with a wide variety of tasks.
- The ability to influence or make decisions is a form of inherent power, and offloading cognition onto AI agents must first be met with caution.
- The consequences of not having a qualitative understanding of how humans interact with LLM outputs is grave

