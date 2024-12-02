# Debugging

> Debugging is twice as hard as writing the code in the first place. Therefore,
> if you write the code as cleverly as possible, you are, by definition, not
> smart enough to debug it.
>
> - [Brian Kernighan](https://github.com/dwmkerr/hacker-laws#kernighans-law)

[![debugging tactics](./.assets/debugging_tactics.jpeg)](https://addyosmani.com/blog/debugging-tactics/)

Debugging is a complicated skill. It's a mix of experience (_"I've seen this
before ..."_), strategies ("I'll try back-tracing this time"), specific
knowledge (_"This list method modifies the data in-place"_), patience (_"Breath
in, breath out, try again"_) and good habits (_"If only I'd written tests!"_).
You will never know everything about debugging because every project is
different. But if you practice good habits, can avoid many bugs and be ready to
fix the bugs you can't avoid.

- [Learning Objectives](#learning-objectives)
- [Debuggin](./debugging.md)
- [Prep Work](./prep_work.md)
- [Lesson Plan](./lesson_plan.md)

---

## Learning Objectives

<details><summary>Priorities: 🥚🐣🐥🐔 (click for more info)</summary>
<br />

Learning objective for this workshop are labeled so you can prioritize your
study time. The emojis show the _minimum_ mastery you are expected to achieve
for each skill, but there is no maximum! If you have the time you should aim to
master all of the skills introduced in this workshop.

- 🥚 You are expected to master these skills. They are the foundations you will
  need to move forward.
- 🐣 You are expected to be comfortable with these skills. It's ok if you still
  need help sometimes.
- 🐥 You are expected to be familiar with these skills. It's enough to recognize
  them in practice and apply them with help.
- 🐔 You are not expected to know these skills, but they are important if you
  want to excel. You should only focus on these after mastering the 🥚, 🐣 and
  🐥 objectives.

---

</details>

### Fixing Bugs

- 🦆 You are not embarrassed to do some
  [rubber duck debugging](https://rubberduckdebugging.com/).
- 🥚 You know that someone else will always use your program
  [in a way you didn't imagine](https://www.youtube.com/watch?v=CfCiW4UhqLo).
- 🥚 You can study a program skeptically, always asking "_how can I break this
  program?_".
- 🐣 You can identify steps of execution that surprise you. This will help
  understand the gap between what a program _does_ do, and what it _should_ do.
- 🐣 You can clearly describe a bug by answering questions like these:
  - on what line does the bug occur?
  - what language features are involved with the bug?
  - what _should_ the program do? Name specific test cases and lines of code!
  - What _does_ the program do? Name specific test cases and lines of code!
- 🐣 You can recognize these four types of bug: overt vs. covert, and persistent
  vs. intermittent.
- 🐥 You can trace a program backwards from a surprising step to understand how
  it happened (either mentally or on paper, VSCode's debugger only goes
  forward).

### Avoiding Bugs in the Fist Place

- 🥚 Pair programming with someone you trust.
- 🥚 Always use the simplest and most understandable solution.
  ([KISS](https://github.com/dwmkerr/hacker-laws#the-kiss-principle))
- 🥚 Develop your code one small step at a time, writing and running tests for
  each change before moving on.
- 🥚 Have others read and review your code, they will find mistakes you missed
  and think of improvements you wouldn't.
- 🥚 Write less code. Keep your end goal in mind and avoid writing any code that
  is not _absolutely necessary_ to reach your goal.
- 🥚 Keep a Bug Log; Write down bugs you've encountered and how you fixed them.
  This log will help you avoid making the same mistakes, and double as
  inspiration for how to fix new bugs.
