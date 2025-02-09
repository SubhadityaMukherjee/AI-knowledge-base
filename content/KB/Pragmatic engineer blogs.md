---
title: Pragmatic engineer blogs
toc: true
tags:
  - blog_notes
  - software
date modified: Thursday 6th February 2025, Thu
date created: Thursday 6th February 2025, Thu
---

# Pragmatic Engineer Blogs
```toc
```
## [stackoverflow vs chatgpt](https://blog.pragmaticengineer.com/are-llms-making-stackoverflow-irrelevant/)

- ![](https://blog.pragmaticengineer.com/content/images/2025/01/2.webp)
- **The drop in questions indicates that trouble is ahead.** Most of StackOveflow's traffic comes from search engines, so this decline is unlikely to have an equally dramatic _immediate_ drop in visits. However, any fall can turn into a vicious cycle: with fewer questions asked, the content on the site becomes dated and less relevant, as fewer questions mean fewer up-to-date answers. In turn, the site gets less search engine traffic, and visitors who get to the site via search find answers woefully out of date.
- where will LLMs get new training data from if stack overflow is not being used
## [Is the “AI developer”a threat to jobs – or a marketing stunt? - The Pragmatic Engineer](https://blog.pragmaticengineer.com/ai-developer-marketing-stunt/)
- "Devin is the new state-of-the-art on the SWE-Bench coding benchmark, has successfully passed practical engineering interviews from leading AI companies, and has even completed real jobs on Upwork.
- Devin is an autonomous agent that solves engineering tasks through the use of its own shell, code editor, and web browser.
- even Cognition AI admits that the tool only solved about 1 in 7 GitHub issues unassisted in tests.
- What if it's a well-choreographed show performed out of necessity?
- **What if AI dev tool startups have been backed into a corner by Microsoft, which has eaten their lunch?**
- the only major source control platforms that don't have AI assistants yet are GitLab and Bitbucket, and this is surely just a matter of time.
- This means, one of the few ways to launch an AI dev tools startup is to claim you will _fully_ replace software engineers. Anything less, and there's no reason why developers should swap their existing coding assistant, and open up their codebase for a brand new tool to crawl and contribute to.
- **The good news is the claim "you will not need software engineers" has been on repeat since the 1960s**
- Efficient frameworks are continuously created so that fewer developers can build the same application; no-code tools promise to build software without the need of developers. And while all of these initiatives partially succeed: we keep observing a need for software developers.
- LLMs have a core problem with hallucination, and coding is one of the few use cases of adding a second validation loop to test the modified code and eliminate this hallucination
## [A Comment Is An Invitation For Refactoring - The Pragmatic Engineer](https://blog.pragmaticengineer.com/a-comment-is-an-invitation-for-refactoring/)
- **A comment is an apology** for not choosing a more clear name, or a more reasonable set of parameters, or for the failure to use explanatory variables and explanatory functions.
- The problem with comments is that they have no compile-time check and _tend to be forgotten_. It's very easy to change your code but forget about the comments.
- I come across this pattern fairly often, where there are several comments splitting up parts of a long method
- This is an invitation to again extract the sections the comments refer to.
- explain how a bug is eliminated by some otherwise hard to understand line(s) of code
- Commented out code is dead code, and dead code rots your codebase.

## [Stop Calling it Bad Code - The Pragmatic Engineer](https://blog.pragmaticengineer.com/bad-code/)

- **Be specific** on the flaws you see, even at the cost of being more verbose. _"I find this function too complicated".__"This class has multiple responsibilities". "The variable name does not describe its purpose clearly"._
- **Give a specific suggestion ** on how to improve the issue, if it not obvious from your description.
- **Talk about the future implications of the code you see, if not changed**.
- **Ask the person writing the code**, what they think about your comments.
- By not using generic and negative terms like "bad", conversations about code become constructive.

## [Talk First, Code Later - The Pragmatic Engineer](https://blog.pragmaticengineer.com/talk-first-code-later/)

- **When making changes to a system you are not familiar with, follow these steps to reduce churn**:
- **Summarize the problem** you're trying to solve. Talk with people owning the system, sharing your problem.
- **Share and validate** the fix you're thinking of. Reach out to engineers on the owning team: in-person, over chat/email or a call, and talk
- **Describe your code changes clearly**,
- It's interesting how problems like this are mostly nonexistent when the whole team is colocated.
- However, when working across locations, the "t
- talk first, code later" _approach is an un-intuitive tool that speeds development up and leads to better communication between engineers and teams

## [Efficient Software Project Management at its Roots - The Pragmatic Engineer](https://blog.pragmaticengineer.com/efficient-software-project-management-at-its-roots/)

- Many projects I've seen go south were ones where stakeholders were not aligned
- A common tool I see used is via a **project kickoff with all stakeholders present **_and_** involved**. By all stakeholders, I mean everyone who will be working on the project or will have some sort of input.
- Given this is an expensive meeting, the person leading the meeting typically prepares an overview about the background ("why"), goals ("what") suggested approach ("how") and end state.
- In order to keep clarity throughout the project, as well as an ongoing sense of focus, milestones that help the team focus are something I've seen work exceptionally well.
- **no-BS update**
	- For distributed teams, an email to all internal stakeholders can work well. For teams onsite, a team check-in with stakeholders locally present also works nice
	- It's meant to be a quickly thrown together description on where the team is against the milestones, what the upcoming goals are for the next period and what progress was made the last period
	- By creating a culture where people commit to short-term goals, then hold themselves accountable and check in with each other helps keep both feet on the ground.
- have a culture that rewards raising concerns early on and be pragmatic in tradeoffs to mitigate risk
- Most of the risk in software projects is discovered by engineers, on the ground. The best engineers love problem-solving and are naturally optimistic. So when they come across a problem, they see a challenge to solve, not a potential delay to the project.
