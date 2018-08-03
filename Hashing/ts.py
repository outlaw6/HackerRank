def hourglassSum(arr):
    maxs = []
    
    for x in range(len(arr) - 2):
        for y in range(4):
            maxs1 = arr[x][x] + arr[x][x+1] + arr[x][x+2] + arr[x+1][y+1] + arr[x+2][x] + \
            arr[x+2][x+1] + arr[x+2][x+2]
            maxs.append(maxs1)
    return max(maxs)


    
arr =[[1 ,1 ,1 ,0 ,0 ,0],
      [0, 1, 0, 0 ,0 ,0],
      [1 ,1 ,1 ,0 ,0, 0],
      [0 ,0, 2, 4 ,4 ,0],
      [0 ,0 ,0 ,2 ,0, 0],
      [0 ,0 ,1, 2 ,4, 0]]



result = hourglassSum(arr)

print(str(result))