# Recursion

A recursive function is one that calls itself to solve a problem. Rather than
tackling a big problem all at once with little steps (like a for loop),
recursion breaks the problem into smaller versions of the same problem, solves
the smallest part, and combines the results. This strategy of breaking down and
building back up is a key strategy in computer science.

## Learning Objectives

- 🥚 **The Callstack**: You can inspect, explain, and predict a program's
  callstack using the debugger.
- 🥚 **Stack Overflow**: You can inspect and explain stack overflow errors.
- 🥚 **Recursion: _Mechanism_ vs. _Strategy_**:  You can separate the _mechanism_ of recursion in Python from recursive _strategies_ in problem solving:
  - _Recursion Mechanism in Python_: A function can call itself from inside its body, adding one more frame to the callstack.  Recursive function calls behave exactly the same as non-recursive function calls, they're just written somewhere different.
  - _Recursive Strategy_: Solving a problem by breaking it into smaller similar problems, solving the smaller problems separately, then combining the small solutions to a larger one.
- 🥚 **Parts of a Recursive Solution**: You can explain how the 5 parts of a
  basic recursive strategy work together:
  - **Base Case**: The smallest version of the problem you are solving.
  - **Turn-Around**: How you solve the base case.
  - **Break-Down**: Create a smaller version of the problem from a bigger version.
  - **Recursion**: Calling the function recursively with the smaller problem.
  - **Build-Up**: Combining the smaller solution(s) to create a larger solution.
- 🥚 **Labeling Recursive Solutions**: You can use comments to identify and
  label the 5 parts of a recursive solution written in Python.
- 🥚 **semi-Formal Definition**: You can write a semi-formal recursive
  definition to describe a recursive solution written in Python.
- 🐣 **Visualizing Implementation**: You can use the debugger and print
  statements to visualize a recursive solution's implementation.
- 🐣 **Visualizing Strategy**: You can visualize a recursive solution's strategy
  using the tool(s) of your choice:
  - The `trace_recursion` decorator in this repository.
  - VSCode Extensions: [recursion-viewer](https://marketplace.visualstudio.com/items?itemName=DmytroBaida.recursion-viewer)
  - Python Packages:
    [`rcviz`](https://github.com/carlsborg/rcviz?tab=readme-ov-file),
    [recursion-visualizer](https://pypi.org/project/recursion-visualizer/),
    [Recursion-Tree-Visualizer](https://github.com/Bishalsarang/Recursion-Tree-Visualizer?tab=readme-ov-file), [vizrecurse](https://pypi.org/project/vizrecurse/)
  - Websites: [recursionvisualizer.com](https://www.recursionvisualizer.com),
    [recursion.vercel.app](https://recursion.vercel.app),
    [recursion-visualizer.vercel.app](https://recursion-visualizer.vercel.app),
    [visualgo.net](https://visualgo.net/en/recursion)
- 🐣 **Debugging Recursion**: You can use the 5 parts of recursion to help find
  and fix bugs in a recursive solution.
- 🐥**Writing Recursion**: You can plan a recursive solution using the 5 parts
  as a guide, then can implement your strategy as a Python function.
