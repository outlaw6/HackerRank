l1 = []
for x in range(2):
    l1.append(str(input()).split(" "))
d1 = int(l1[0][0]) # Day returned
m1 = int(l1[0][1]) # Month returned
y1 = int(l1[0][2]) # Year returned

dd1 = int(l1[1][0]) # Due day
mm1 = int(l1[1][1]) # Due month
yy1 = int(l1[1][2]) # Due year

if (y1 > yy1):
    print("10000")
    exit()
elif (y1 < yy1):
    print("0")
else:
    if (d1 == dd1) and (m1 == mm1) and (yy1 == y1):
        print("0")
    elif (d1 < dd1) and (m1 < mm1):
        print("0")
    elif (d1 <= dd1) and (m1 <= mm1):
        print("0")
    elif (m1 > mm1):
        print(500 * (m1 - mm1))
    elif (d1 > dd1) and (m1 == mm1):
        print(15 * (d1 - dd1))