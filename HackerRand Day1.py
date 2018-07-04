lista1 = [ [1,1,1,0,0,0],
		   [0,1,0,0,0,0],
		   [1,1,1,0,0,0],
		   [0,0,2,4,4,0],
		   [0,0,0,2,0,0],
		   [0,0,1,2,4,0]  ]


lista2 = []
for times in range(len(lista1) - 2):
	for x in range(4):
		print(lista1[times][x],lista1[times][x+1],lista1[times][x+2])
		print(" ",lista1[times+1][x+1])
		print(lista1[times+2][x],lista1[times+2][x+1],lista1[times+2][x+2])

		suma = lista1[times][x] + lista1[times][x+1]+ lista1[times][x+2] + lista1[times+1][x+1] + lista1[times+1][x] + lista1[times+2][x] + lista1[times+2][x+1] + lista1[times+2][x+2]
		lista2.append(suma)


print(lista2)
print(max(lista2))