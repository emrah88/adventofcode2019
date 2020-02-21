import math

input = '../input.txt'

result = 0

with open(input) as fp:
    for _, line in enumerate(fp):
        if line != '\n':
            result += math.floor(int(line) / 3) - 2

print(result)
