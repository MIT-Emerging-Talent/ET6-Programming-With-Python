# Workflow with LLM

A suggested workflow to practice when developing a function with LLMs. With
experience you can adapt this workflow to match your style:

0. Clearly describe the _behavior_ you want your function to have. Include a
   couple input/output examples.
   - Write your description as a _docstring_
1. Write a suite of unit tests for this docstring covering as many boundary cases as possible.
   - Double-check the tests to be sure you understand them and they are correct
   - Include tests for defensive assertions.
   - Run your tests to make sure they have no errors.
2. Pick one unit test s and write the simplest possible function that will pass it.
   - Test the function to make sure it passes.
   - If you can't pass this test, focus on another one instead.  You can always come back to the one you skipped.s
   - Step through the function to make sure it works how you think it does.
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
   [the checklist from Documenting and Testing](../3_documenting_and_testing/code_review_checklist.md)
