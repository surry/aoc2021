import os

from typing import List


def part1(lines: List[str]):

    gamma = 0
    epsilon = 0

    sums = None

    for line in lines:
        line = line.strip()
        if sums is None:
            sums = [0] * len(line)

        for i, ch in enumerate(line):
            sums[i] += int(ch)

    num_lines = len(lines)
    bit_length = len(line)

    for i, sum in enumerate(sums):
        #print(f'Sum {i} is {sum}')
        if  sum > num_lines//2:
            # number of 1s in the column is greater than the number of 0s
            gamma += 1 << (bit_length - i - 1)
        else:
            epsilon += 1 << (bit_length - i - 1)

    return (gamma, epsilon)


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), 'input03.txt'), 'r') as f:
        lines = f.readlines()

        gamma, epsilon = part1(lines)

        print(gamma * epsilon)
