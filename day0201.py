amt = 0
rib = 0
with open("day02.txt", "r") as f:
    for line in f:
        (l,w,h) = line.split("x")

        l, w, h = int(l), int(w), int(h)

        amt += 2*l*w + 2*w*h + 2*l*h + min(l*w,l*h,w*h)
        rib += min(l+l+h+h,l+l+w+w,w+w+h+h)
        rib += l*w*h

print(amt)
print(rib)