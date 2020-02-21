import math

input = '../input.txt'

result = []

with open(input) as fp:
    for _, line in enumerate(fp):
        if line != '\n':
            result = list(map(lambda n: int(n), line.split(',')))

def compute(list, noun, verb):
    pos = 0
    list[1] = noun
    list[2] = verb

    while pos < len(list) - 4:
        temp = 0
        opcode = list[pos]
        pos1 = list[pos+1]
        pos2 = list[pos+2]
        target = list[pos+3]

        if opcode == 99:
            break

        if opcode == 1:
            temp = list[pos1] + list[pos2]

        if opcode == 2:
            temp = list[pos1] * list[pos2]

        try:
            list[target] = temp
        except IndexError:
            break

        pos += 4
    return list[0]

def findNounVerb(result, target):
    noun = 0
    verb = 0

    while noun <= 99:
        while verb <= 99:
            res = compute(result.copy(), noun, verb)
            if res == target:
                print(noun, verb)
                return (noun, verb)
            verb += 1
        noun += 1
        verb = 0

noun, verb = findNounVerb(result, 19690720)
print(100 * noun + verb)
