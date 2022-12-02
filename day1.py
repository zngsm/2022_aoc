import sys; sys.stdin = open("input/day1", "r")

ans_1 = 0
calories = 0

total_calories = []

for line in sys.stdin.readlines():
    number = line.strip()
    if number.isdigit():
        calories += int(number)
    else:
        ans_1 = max(ans_1, calories)
        total_calories.append(calories)
        calories = 0

total_calories.sort(reverse=True)
ans_2 = sum(total_calories[:3])

print("1번", ans_1)
print("2번", ans_2)