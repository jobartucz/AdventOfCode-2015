
with open("day01.txt") as f:
    lines = list(f)

floor = 0
i = 0
for c in lines[0]:
    i += 1
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor == -1:
        break

print(floor)
print(i)