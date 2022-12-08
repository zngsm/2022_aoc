import sys

sys.stdin = open("../input/day8", "r")

arr = [
    list(map(int, line.strip()))
    for line in sys.stdin.readlines()
]
N = len(arr)

## PART 1 ##
visit = set()
for y in range(N):
    start_l = arr[y][0]
    start_r = arr[y][N - 1]
    start_t = arr[0][y]
    start_b = arr[N - 1][y]
    visit.add((y, 0))
    visit.add((y, N - 1))
    visit.add((0, y))
    visit.add((N - 1, y))
    for x in range(1, N - 1):
        if arr[y][x] > start_l:
            visit.add((y, x))
            start_l = arr[y][x]
        if arr[y][N - 1 - x] > start_r:
            visit.add((y, N - 1 - x))
            start_r = arr[y][N - 1 - x]
        if arr[x][y] > start_t:
            visit.add((x, y))
            start_t = arr[x][y]
        if arr[N - 1 - x][y] > start_b:
            visit.add((N - 1 - x, y))
            start_b = arr[N - 1 - x][y]

print("Part1", len(visit))

## PART 2 ##
# 상하좌우
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

ans = 0
for y in range(N):
    for x in range(N):
        start = arr[y][x]
        total = 1
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            dist = 0
            while 0 <= ty < N and 0 <= tx < N and arr[ty][tx] < start:
                dist += 1
                ty += dy[i]
                tx += dx[i]
                if 0 <= ty < N and 0 <= tx < N and arr[ty][tx] >= start:
                    dist += 1
            total *= dist
        ans = max(ans, total)

print("Part2", ans)
