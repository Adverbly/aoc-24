def run(input_lines):
    total = 0
    pairs = [[int(value) for value in line.split("   ")] for line in input_lines]
    rights = [pair[1] for pair in pairs]
    for left, _ in pairs:
        total += sum([x for x in rights if x == left])
    return total
