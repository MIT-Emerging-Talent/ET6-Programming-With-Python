# Studying with LLMs

LLMs exists and can code, we know this. And you will use it, we know this too.
So here's our advice on how to use generative AI when studying Welcome to JS:

Generative AI can write and explain code for you, but writing and explaining
code are not the most important skills a developer needs. More importantly, a
developer needs to _understand_ a program, its purpose and its context:

- Who is a program's user and why will they use it?
- Who is developing the program, and how do they share this work?
- What problem does program solves, and is this problem represented in code?
- ...

... sure, AI can _help_ you answer all of these questions. But you need to know
how to ask these questions very clearly otherwise AI will become a crutch, not a
tool.

Welcome to JS covers the hidden skills behind understanding, discussing,
planning and writing programs. Every learning objective in this module is a
skill you should master without the help of AI - you can use AI for help
learning each skill, but you have only mastered a skill when you can complete
its exercises without AI.

Remember: AI can _write_ code for you, but it can't _understand_ a program
**for** you.

## LLMs are not perfect!

LLMs are useful but they also cause harm. This doesn't meet you should never use
LLMs - it just means you should use them responsibly and be aware of the risks
they pose to your own work, to others, and to the environment:

- LLMs may generate responses in violation of copyright law, or that violate
  data privacy.
- LLMs
  [consumes more energy](https://ai.stackexchange.com/questions/38970/how-much-energy-consumption-is-involved-in-chat-gpt-responses-being-generated)
  than older tools like [internet search](https://arxiv.org/pdf/2307.01135.pdf).
- LLMs can _hallucinate_ - they can produce responses that feel correct but are
  actually untrue.
- LLMs can, despite many guardrails, produce responses that perpetuate
  stereotypes and misconceptions.

---

## Collaboration Strategies

When you use generative AI, think of it as a collaboration not as a code or
explanation generator. You bring your ideas, understanding, and direction to the
conversation and the AI will bring some too. But ultimately it's your
responsibility to steer the collaboration to your learning goals. It's your
responsibility to understand how the final code works, make sure is clear, and
actually solves the problem you're working on.

### Add Context to your Chats

To help keep your chats with LLMs on topic and limited to
[Just Enough Python](./just_enough_python.md), we suggest you attach these documents
to your chat with an LLM, this will work better with some LLMs than with others.
If you're not able to upload the files, you can copy-paste the first one as your
first message:

- **[welcome-to-js.llm-instructions.md](./welcome-to-js.llm-instructions.md)**:
  This document helps the LLM understand Welcome to JS.
- **[welcome-to-js.llm-examples.md](./welcome-to-js.llm-examples.md)**: This
  document has example programs the LLM can use for additional inspiration.

> PS. These documents are a work-in-progress. Send us a PR when you find room
> for improvement!

### Start with this Template

Below is a template prompt you can use with or without
`welcome-to-js.llm-context.md` to get your study sessions off to a good start:

```
I would like to practice <skill>.

By the end of this session, I should able to:
- <learning objective 1>
- ...

Program to use as a practice context:
<paste a program to study OR the LLM will generate one>

Instructions for this session:
- Adjust for individual or group study, supporting peer learning if applicable.
- Tailor difficulty to my comfort level, providing less support as I progress.
- Connect the skill to real-world programming with practical examples.
- Use and explain precise vocabulary related to this skill.
- Guide me through self-assessment strategies.
- Offer alternative explanations and additional practice programs as needed.
- Conclude with open-ended, Socratic-style reflection questions.
- ! Remind me to verify information, as LLMs can make mistakes !
```

### General Strategies

Here are some general tips for collaborating with LLMs when studying:

- If you can't use the LLM [instructions](./studying_with_llms.instructions.md) and [examples](./studying_with_llms.examples.md), then
  begin your chat by describing the persona you'd like the LLM to use. For
  example: _Answer like you are a patient programming teacher who always asks
  comprehension questions before moving on._ You can make these personas as
  detailed as you like.
- When you ask an LLM a question, also ask it to list what it needs you to know
  from you before it can give a good answer. Something like: _Please ask me for
  any additional information you need to answer my prompt._
- Ask the LLM to generate some comprehension questions alongside its
  explanation. You can then discuss then enter your answers and the LLM can help
  you understand the questions you get wrong.
- A great way to practice asking questions that are clear enough for an LLM is
  to use plain old internet search and StackOverflow! Once you can regularly
  find answers on StackOverflow, then you are a strong enough question asker to
  get the most out of LLMs.

### Specific Strategies

Welcome to JS will also introduce strategies for collaborating with generative
AI on specific skills like debugging, documenting, logging, ... but only after
you have practiced the skill without the help of AI. These strategies are
included in each chapter where they fit best.

---

## Suggested Study

- [How to use AI coding tools to learn a new programming language (GitHub blog)](https://github.blog/developer-skills/programming-languages-and-frameworks/how-to-use-ai-coding-tools-to-learn-a-new-programming-language/)
- [How to learn a programming language using AI (InfoWorld)](https://www.infoworld.com/article/2337313/learn-a-programming-language-using-ai.html)
- [r/ChatGPTCoding: How to help LLMs understand your code?](https://www.reddit.com/r/ChatGPTCoding/comments/1coskgn/how_to_help_llms_understand_your_code/)
