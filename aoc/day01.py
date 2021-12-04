import os
from typing import List


def part1(lines: List):
    """
    Returns:
        int: The number of times the depth increases from one measurement to
        the next.
    """

    depth_increases = 0
    previous = int(lines[0])
    for line in lines[1:]:
        current_measurement = int(line)
        if current_measurement > previous:
            depth_increases += 1
        previous = current_measurement

    return depth_increases


def part2(lines: List):

    depth_increases = 0

    previous_window = [
        int(lines[0]),
        int(lines[1]),
        int(lines[2])
    ]

    next_window = [previous_window[1], previous_window[2]]

    for line in lines[3:]:
        next_window.append(int(line))

        if sum(next_window) > sum(previous_window):
            depth_increases += 1

        previous_window = list(next_window)

        next_window.pop(0)

    return depth_increases


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(__file__), 'input01.txt'), 'r') as f:
        lines = f.readlines()
        print(part1(lines))
        print(part2(lines))
