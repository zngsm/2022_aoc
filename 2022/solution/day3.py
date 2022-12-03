import sys; sys.stdin = open("../input/day3")


### part1
total = 0
for line in sys.stdin.readlines():
    input_ = line.strip()
    n = len(input_)
    first = set(input_[:n//2])
    second = set(input_[n//2:])
    ans = (first & second).pop()
    if ord(ans) < 97:
        total += ord(ans) - (65 - 27)
    else:
        total += ord(ans) - 96
print("첫번째", total)


### part2
lines = sys.stdin.readlines()

total = 0
for idx in range(0, len(lines), 3):
    first = set(lines[idx].strip())
    second = set(lines[idx+1].strip())
    third = set(lines[idx+2].strip())
    ans = (first & second & third).pop()
    if ord(ans) < 97:
        total += ord(ans) - (65 - 27)
    else:
        total += ord(ans) - 96

print("두번째", total)

