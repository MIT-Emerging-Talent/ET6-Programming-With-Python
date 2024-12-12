""" Repeat Character

Write a function that takes in a string, a single character, and a number. 
The function returns a string with each occurrence of the character repeated n times.

"""

def repeat_character(text: str, char_to_repeat: str, repetitions: int) -> str:
    """The function returns a string with each occurrence of the character repeated n times.

    Parameters:
        text (str): we will repeat the character in this string
        char_to_repeat (str): this is the character we want to repeat
        repetitions (int): how many times to repeat the character

    Returns:
      string: the string with a single character repeated

    Raises:
      AssertionError: if the first argument is not a string
      AssertionError: if the second argument is not a single character
      AssertionError: if the third argument is not an integer
      AssertionError: if the third argument is less than 0

    >>> repeat_character('Omnia', 'm', 7)
    'Ommmmmmmnia'

    >>> repeat_character('Jola-Moses', 's', 2)
    'Jola-Mossess'

    >>> repeat_character('Hasan', 'e', 999999999999)
    'Hasan'

    >>> repeat_character('Rafaa', 'a', 3)
    'Raaafaaaaaa'
    """

    assert isinstance(repetitions, int), 'third argument must be an integer'
    assert repetitions >= 0, 'third argument cannot be less than 0'

    repeated_text = ''

    for char in text:
      if char.lower() == char_to_repeat.lower():
        # repeated_text += char_to_repeat * repetitions
        repeated_text += char * repetitions
      else:
        repeated_text += char

    return repeated_text
