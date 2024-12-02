import torch


def run(input_lines):
    pairs = [[int(value) for value in line.split("   ")] for line in input_lines]
    lefts = [pair[0] for pair in pairs]
    rights = [pair[1] for pair in pairs]
    lefts.sort()
    rights.sort()
    diffs = [abs(pair[0] - pair[1]) for pair in zip(lefts, rights)]
    return sum(diffs)
