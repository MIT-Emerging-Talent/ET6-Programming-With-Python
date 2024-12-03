# CoAIthoring Workflow

A suggested workflow to practice when developing a function with LLMs. With
experience you can adapt this workflow to match your style:

0. Clearly describe the _behavior_ you want your function to have. Include a
   couple input/output examples.
   - Write your description as a _docstring_
1. Ask the AI to generate a suite of black box unit tests for this docstring,
   covering as many boundary cases as possible.
   - You may need to reformat the tests to have one assertion per method.
   - Read the tests to be sure you understand them and they are correct, make
     changes or add test cases as necessary.
   - You can also ask the AI to generate tests for defensive assertions.
2. Ask the AI to generate a function that will pass your unit tests. Provide
   your unit tests in your prompt as context.
   - Test the function to make sure it passes. AI isn't always right!
   - Debug any failing test cases. You can do this manually, and with help from
     the LLM.
   - If you still can't debug the function, explain to the AI which test cases
     failed then ask it to regenerate the function.
   - Repeat until all the tests pass.
3. Study the passing code to understand it's _strategy_. Code is not
   maintainable if you don't understand it.
   - You may need to change the function's _implementation_ to understand it,
     try: renaming variables, adding comments, ... whatever helps!
   - If you have trouble understanding the code, you can try asking the AI to
     explain it.
   - If you still can't understand the solution, return to step 2 and ask the AI
     to solve the same challenge using a different strategy.
   - Don't forget to run your tests after every change you make!
4. Polish the function's _implementation_ so it is as clear and helpful as
   possible.
   - Use a linter and a formatter.
   - Add comments and change variable names when necessary to explain the
     _strategy_
   - See if you can't simplify the control flow. For example, are there too many
     nested structures?
   - Don't forget to run your tests after every change you make!
5. Give the code a final review using
   [the checklist from Documenting and Testing](https://github.com/MIT-Emerging-Talent/documenting-and-testing/blob/main/code-review-checklists.md)
