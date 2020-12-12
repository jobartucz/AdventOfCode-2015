
positions = set()
position = []
position.append((0,0))
position.append((0,0))
positions.add(position[1])

houses = 1

with open("day03.txt", "r") as f:
    for line in f:
        # line = "^v^v^v^v^v"
        s = 0
        for c in line:
            if c == '>':
                newpos = (position[s][0]+1,position[s][1])
                if newpos not in positions:
                    houses += 1
                    positions.add(newpos)
                position[s] = newpos
            elif c == '<':
                newpos = (position[s][0]-1,position[s][1])
                if newpos not in positions:
                    houses += 1
                    positions.add(newpos)
                position[s] = newpos
            elif c == '^':
                newpos = (position[s][0],position[s][1]+1)
                if newpos not in positions:
                    houses += 1
                    positions.add(newpos)
                position[s] = newpos
            elif c == 'v':
                newpos = (position[s][0],position[s][1]-1)
                if newpos not in positions:
                    houses += 1
                    positions.add(newpos)
                position[s] = newpos
            if s == 0:
                s = 1
            else:
                s = 0

# print(positions)
print(houses)