import sys;
from collections import defaultdict

sys.stdin = open("../input/day5")

start = False
results = defaultdict(list)
while True:
    try:
        line = input()
        if not start:
            for idx, n in enumerate(range(1, len(line), 4)):
                if line[n].strip() and not line[n].isdigit():
                    results[idx+1].insert(0, line[n])

        if not line.strip():
            start = True

        if start and line.strip():
            command = line.split()
            cnt = int(command[1])
            from_ = int(command[3])
            to_ = int(command[5])


            # PART 1
            # for _ in range(cnt):
            #     a = results[from_].pop()
            #     results[to_].append(a)

            # PART 2
            # results[to_] += results[from_][len(results[from_])-cnt:]
            # results[from_] = results[from_][:len(results[from_])-cnt]

    except EOFError:
        break

ans = ""
for key, value in sorted(results.items()):
    ans += value[-1]

print(ans)
