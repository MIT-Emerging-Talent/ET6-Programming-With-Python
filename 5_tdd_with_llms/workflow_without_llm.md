# Workflow without LLM

A suggested workflow to practice when developing a function without help from AI. With
experience you can adapt this workflow to match your style:

1. **Understand the requirements**: Clearly describe the _behavior_ you want your function to have.
   - Write your description as a _docstring_ with _doctests_
1. **Red: Create a test and make it fail.**
    - Write the test as if the function already existed.
    - Write an empty function with the correct name and `pass` in the body.
    - Run the test. It should fail. This is a calibration measure to ensure that your imports are working and that your tests are calling the correct function. This is a meaningful failure, and you expect it to fail.
1. **Green: Make the test pass by any means necessary.**
    - Write just enough code to pass the test. Keep it simple!
    - You can even hard-code of the expected value to verify the test works.
    - If you wrote code that passes the test, you are finished. The test is the objective definition of "done."
      - You can improve your code in the next step
      - If new behaviors are needed, then another test is needed.  You can do this on the next cycle.
1. **Refactor: Improve your function's code.**
    - Make changes to your _strategy_ or _implementation_ without failing the tests you already pass
    - Do not add any new _behaviors_!  You can do this on the next cycle with another test.
    - Keep rerunning the tests to make sure they still pass.
    - You can add more tests for the same behaviors as long as they pass.
1. Give the code a final review using
   [the checklist from Documenting and Testing](../3_documenting_and_testing/code_review_checklist.md)

> adapted from [hmandal/'s Gist](https://gist.github.com/hmandal/32038873bbe8ea8148ec51ffe9fc6ce5)
