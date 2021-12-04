import os
from typing import List


def part1(lines: List):

    depth = 0
    forward = 0

    for line in lines:
        distance = int(line.split(' ')[1])
        if line.startswith('forward'):
            forward += distance
        elif line.startswith('up'):
            depth -= distance
        else:
            depth += distance

    return (depth, forward)


def part2(lines: List):

    depth = 0
    forward = 0
    aim = 0

    for line in lines:
        amount = int(line.split(' ')[1])
        if line.startswith('forward'):
            forward += amount
            depth += aim * amount
        elif line.startswith('up'):
            aim -= amount
        else:
            aim += amount

    return (depth, forward)



if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), 'input02.txt'), 'r') as f:
        lines = f.readlines()

        depth, forward = part1(lines)
        print(depth * forward)

        depth, forward = part2(lines)
        print(depth * forward )