
"""
  Composing Strings
   
"""
from time import time

def get_letters(document):
    """
    This approach maybe terribly inefficient because string are immutable,
    the command, letters += c, would compute the concatenation, letter += c, 
    as a new string instance and then reassign the identifier, letter, to that result.
    Construction of a new string require proportional to its length, if the final result has n chars,
    the series concatenation would tike time proportional to the familiar sum 1+2+3+....+n therefor O(N)2 time.
    """
    # letters = ''.join(c for c in document if c.isalpha()) the entire function in single line using comprehension
    # return letters
    letters = ''
    start = time()
    for c in document:
        if c.isalpha():
            letters += c
    end = time()
    return letters, (end - start)

def get_letters_linear(document):
    # letters = ''.join[c for c in document if c.isalpha()]
    # letters = ''.join(c for c in document if c.isalpha())
    # return letters
    temp = []
    start = time()
    for c in document:
        if c.isalpha():
            temp.append(c)
    letters = ''.join(temp)
    end = time()
    return letters, (end - start)
        

print(get_letters('dsfdfsefsef3434343dfdfdfs34%@%adfs33dfdfdf'))
print(get_letters_linear('dsfdfsefsef3434343dfdfdfs34%@%adfs33dfdfdf'))