arr1 = [1,2,3,4,5] 


d = 4
n = 5

for x in range(5):
	print(arr1[(x+d) % len(arr1)], end=' ')
print(".")

#d %= n
d = d % n
print(d%n)
print(*(arr1[d:] + arr1[:d]))

print(arr1)

d1 = [x for x in range(1,6)]
d2 = []
print(d1)
for x in range(2):
	temp = d1[x]
	d1[x] = d1[x+1]
	d1[x+1] = temp
	print(d1[x], end='')
print(d1)



