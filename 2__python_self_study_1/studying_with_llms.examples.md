# Just Enough Python: LLM Examples

This document has example programs to give LLMs inspiration when helping
learners study Just Enough Python.

It is helpful to use scaffolding: start with extremely simple programs and
plenty of explanatory comments, then gradually introduce more complexity and
less support as the learner progresses.

## Fill in the Blanks

This program demonstrates using `_` in the code as an exercise for learners. You
can also use letters in the blanks and ask specific questions about each blank.

```Python
"""
Fill in the Blanks Exercise

This program demonstrates using _ in the code as an exercise for learners.
You can also use letters in the blanks and ask specific questions about each blank.
"""

# --- gather user phrase ---

phrase = None
while phrase is None or phrase == "":
    phrase = input('enter a phrase: ')
    phrase = phrase.strip()

# --- get user's choice ---

keep_letters = input(
    '"ok" to remove everything that is not a letter\n' +
    '"cancel" to repeat each character: '
).strip()

# --- process the phrase based on choice ---

new_phrase = ''
if keep_letters == "ok":  # This replaces __B__ in the original
    # --- keep only letters ---
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for character in phrase:  # This replaces __C__ in the original
        if character.lower() in letters:  # This replaces __D__ in the original
            new_phrase = new_phrase + character
else:
    # --- double each character ---
    
    for character in phrase:
        new_phrase = new_phrase + character + character  # This replaces __E__

# --- show the result ---
print(new_phrase)

"""
Comprehension questions:

- Which interaction belongs in A? How can you tell?
- What happens if the user just hits enter in A? How does the program respond?
- Which variable belongs in B? What type does it store? How can you tell?
- Which variable belongs in C? Where does its value come from?
- Is it possible to know from the source code how many times the program will loop over C?
- What method belongs in D? Why is the string changed to lowercase before?
- Which variable belongs in E? What role does this variable have?
"""
```

Comprehension questions:

- Which interaction belongs in **A**? How can you tell?
- What happens if the user cancels the prompt in **A**? How does the program
  respond?
- Which variable belongs in **B**? What type does it store? How can you tell?
- Which variable belongs in **C**? Where does its value come from?
- Is it possible to know from the source code how many times the program will
  loop over **C**?
- What method belongs in **D**? Why is the string changed to lowercase before?
- Which variable belongs in **E**? What role does this variable have?

## Refactoring

```Python
"""
Refactoring Exercise

What strategy can replace the need for continue?
How might you redesign the loop to avoid this keyword entirely?
"""

to_be_frogged = None

while to_be_frogged is None or to_be_frogged == "":
    to_be_frogged = input(
        'enter some text to frogify.\n' +
        '- "f" will be replaced with "frog"\n' +
        '- "F" will be replaced with "FROG": '
    ).strip()

frogged = ''

for character in to_be_frogged:
    if character == 'f':
        frogged = frogged + 'frog'
        continue
    if character == 'F':
        frogged = frogged + 'FROG'
        continue
    frogged = frogged + character

print(frogged)
```

## Modifying

```python
"""
Modifying Exercise

How could you modify this program so it checks that user input is SHORTER than a specific limit?
"""

limit = 5
phrase = ''
long_enough = False

while not long_enough:
    phrase = input('enter anything longer than ' + str(limit) + ' characters: ')
    
    if phrase == "":
        print('there is no escape')
    elif len(phrase) <= limit:
        print('too short')
    else:
        long_enough = True

print('"' + phrase + '" is ' + str(len(phrase)) + ' characters long')
```

## Naming Variables

```Python
"""
Naming Variables Exercise

Fill in appropriate names for variables A, B, and C
"""

__A__ = None
while __A__ is None or __A__ == "":
    __A__ = input('enter some text, each character will be repeated: ')
    __A__ = __A__.strip()

__B__ = ''
for __C__ in __A__:
    __B__ = __B__ + __C__ + __C__

print(__A__ + ' -> ' + __B__)

"""
Comprehension questions:

- What is this program's behavior?
- What would be a good name for each variable?
"""
```

Comprehension questions:

- What is this program's behavior?
- What would be a good name for each variable?

## Users Stories + Test Cases + Review Checklist

As learners progress you can also start to discuss user stories, test cases and
code review checklists. Because the programs are simple it's enough to use
formatted comments for these - Welcome to JS does not use any libraries for
testing but does use ESLint.

```Python
"""Magic Mirror

A user can input a non-empty string and only the letters will be turned into a mirror
  - given the user hits enter with no input, they will be prompted again
  - given their input is valid, the loop will exit and the mirrored letters will be displayed

Test cases:
  only letters:
    'abc' -> 'abc|cba'
    'hello' -> 'hello|olleh'
    'JavaScript' -> 'JavaScript|tpircSavaJ'
  only not-letters:
    '.(-).' -> '|'
    '-=>|<=-' -> '|'
    '. - ^ - .' -> '|'
  mixed letters and not-letters:
    'hello!' -> 'hello|olleh'
    'good bye?' -> 'goodbye|eybdoog'
    'let input = ""' -> 'letinput|tupnitel'
"""

# Get valid input from user
text = None
while text is None or text == "":
    text = input('Enter text to mirror: ')
    text = text.strip()

# Extract only letters from the input
letters = ''
for char in text:
    if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
        letters = letters + char

# Create the mirrored output
# First build the reversed string
reversed_letters = ''
for i in range(len(letters) - 1, -1, -1):
    reversed_letters = reversed_letters + letters[i]

# Combine original and reversed with separator
result = letters + '|' + reversed_letters
print(result)

"""
Checklist:
  [ ] the code is formatted
  [ ] variable names are clear and helpful
  [ ] each line of code is explained in a comment above that line
    - use full sentences and correct Python vocabulary
  [ ] the program runs
  [ ] the program has no errors
  [ ] all of the test cases work
  [ ] you tested strange inputs that could break your program (edge cases)
"""
```
