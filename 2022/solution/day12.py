import sys
from collections import deque


sys.stdin = open("../input/day12", "r")
arr = [
    list(line.strip())
    for line in sys.stdin.readlines()
]

N = len(arr)
M = len(arr[0])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ascii_v = [[0 for _ in range(M)] for _ in range(N)]
for y in range(N):
    for x in range(M):
        if arr[y][x] == "S":
            ascii_v[y][x] = 1
        elif arr[y][x] == "E":
            ascii_v[y][x] = ord("z") - ord("a") +1
        else:
            ascii_v[y][x] = ord(arr[y][x]) - ord("a") + 1


def search():
    Q = deque()
    for y in range(N):
        for x in range(M):
            if arr[y][x] == "S":
                Q.append(((y, x), 0))

    visit = set()
    while Q:
        (sy, sx), d = Q.popleft()
        if (sy, sx) in visit:
            continue
        visit.add((sy, sx))
        if arr[sy][sx] == "E":
            return d
        for i in range(4):
            ty = sy + dy[i]
            tx = sx + dx[i]
            if 0 <= ty < N and 0 <= tx < M and ascii_v[ty][tx] <= ascii_v[sy][sx] + 1:
                Q.append(((ty, tx), d+1))


def search_2():
    Q = deque()
    for y in range(N):
        for x in range(M):
            if arr[y][x] == "E":
                Q.append(((y, x), 0))

    visit = set()
    while Q:
        (sy, sx), d = Q.popleft()
        if (sy, sx) in visit:
            continue
        visit.add((sy, sx))
        if ascii_v[sy][sx] == 1:
            return d
        for i in range(4):
            ty = sy + dy[i]
            tx = sx + dx[i]
            if 0 <= ty < N and 0 <= tx < M and ascii_v[ty][tx] >= ascii_v[sy][sx] -1:
                Q.append(((ty, tx), d+1))


part_1 = search()
print(part_1)
part_2 = search_2()
print(part_2)