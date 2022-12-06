import sys;
sys.stdin = open("../input/day6", "r")

line = input()
print(line)

for idx in range(3, len(line)):
    target = line[idx-4:idx]
    if len(set(target)) == 4:
        print(idx)
        break

for idx in range(13, len(line)):
    target = line[idx-14:idx]
    if len(set(target)) == 14:
        print(idx)
        break
