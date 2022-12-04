import sys; sys.stdin = open("../input/day4")


### part1
total = 0
total_2 = 0
for line in sys.stdin.readlines():
    elf_1, elf_2 = line.strip().split(",")
    s1, e1 = map(int, elf_1.split("-"))
    s2, e2 = map(int, elf_2.split("-"))

    if s1 <= s2 and e1 >= e2:
        total += 1
    elif s2 <= s1 and e2 >= e1:
        total += 1

    if s1 > e2 or e1 < s2 or s2 > e1 or e2 < s1:
        continue
    total_2 += 1

print(total)
print(total_2)