print(sum([int([c for c in line if c.isdigit()][0] + [c for c in line if c.isdigit()][-1]) for line in open('input.txt').readlines()]))