l1 = [[10,1,2011], [1,1,2011]]

d1 = int(l1[0][0])
m1 = int(l1[0][1])
y1 = int(l1[0][2])

dd1 = int(l1[1][0])
mm1 = int(l1[1][1])
yy1 = int(l1[1][2])

if (y1 > yy1):
	print("10000")
	exit()
if (y1 <= yy1):
	if (d1 == dd1) and (m1 == mm1) and (yy1 == y1):
		print("0")
	elif (d1 <= dd1) and (m1 <= mm1):
		print("0")
	elif (m1 > mm1):
		print(500 * (m1 - mm1))
	elif (d1 > dd1) and (m1 == mm1):
		print(15 * (d1 - dd1))



'''if (d1 == dd1) and (m1 == mm1) and (yy1 == y1):
    print("0")
    exit()
if (yy1 > y1):
    print("0")
elif (yy1 < y1):
    print("10000")
if yy1 >= y1:
    if mm1 < m1:
        print(500 * (m1 - mm1))
    if mm1 >= m1:
        print(15 * (abs(d1-dd1)))'''