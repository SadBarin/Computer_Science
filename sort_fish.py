
# From book Computer Science Distilled: Learn the Art of Solving Computational Problems
# Author: Wladson Ferreira Filho

def merge(sea, fresh):
  buffer = []

  while len(sea) > 0 or len(fresh) > 0:
    fish = ''

    if len(sea) > len(fresh):
      fish = sea[0]
      sea.pop(0)
    else:
      fish = fresh[0]
      fresh.pop(0)

    buffer.append(fish)

  return buffer

print(merge(['Perch', 'Sailfish'], ['Trevally', 'Tarakihi', 'Jobfish']))

# Algorithm complexity: O(n)

