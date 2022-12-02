import sys; sys.stdin = open("../input/day2", "r")

mapper_ans_1 = {
    "A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3,
}

score_1 = {
    1: (3, 0, 6),
    2: (6, 3, 0),
    3: (0, 6, 3)
}

mapper_ans_2 = {
    "X": (0, 3, 1, 2),
    "Y": (3, 1, 2, 3),
    "Z": (6, 2, 3, 1)
}


def game_1(y, m):
    return score_1[m][y-1]


def game_2(y, m):
    return mapper_ans_2[m][y]


ans_1 = 0
ans_2 = 0
for line in sys.stdin.readlines():
    y, m = line.strip().split()
    you, me = mapper_ans_1[y], mapper_ans_1[m]
    ans_1 += (me + game_1(you, me))
    ans_2 += (mapper_ans_2[m][0] + game_2(you, m))

print("1번째", ans_1)
print("2번째", ans_2)
