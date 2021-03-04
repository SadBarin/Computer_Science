
# From book Computer Science Distilled: Learn the Art of Solving Computational Problems
# Author: Wladson Ferreira Filho

word = str(input('Enter a palindrome: ')).lower().replace(' ', '')

def palindrome(word):
  if len(word) <= 1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])

print(palindrome(word))
