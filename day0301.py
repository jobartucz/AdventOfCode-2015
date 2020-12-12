
positions = set()
position = (0,0)
positions.add(position)

houses = 1
with open("day03.txt", "r") as f:
    for line in f:
        for c in line:
            if c == '>':
                newpos = (position[0]+1,position[1])
                if newpos not in positions:
                    houses += 1
                    positions.add(newpos)
                position = newpos
            elif c == '<':
                newpos = (position[0]-1,position[1])
                if newpos not in positions:
                    houses += 1
                    positions.add(newpos)
                position = newpos
            elif c == '^':
                newpos = (position[0],position[1]+1)
                if newpos not in positions:
                    houses += 1
                    positions.add(newpos)
                position = newpos
            if c == 'v':
                newpos = (position[0],position[1]-1)
                if newpos not in positions:
                    houses += 1
                    positions.add(newpos)
                position = newpos

# print(positions)
print(houses)