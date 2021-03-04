
# From book Computer Science Distilled: Learn the Art of Solving Computational Problems
# Author: Wladson Ferreira Filho

number = int(input('Enter a number: '))

def fib(n):
  if n <= 2:
    return 1

  return fib(n - 1) + fib(n - 2)

print(fib(number))
