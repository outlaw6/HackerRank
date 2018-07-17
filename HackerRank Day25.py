def isPrime(x):
    if x <= 0:
        return "Not prime"
    if x == 1:
        return "Not prime"
    if x == 2:
        return "Prime"
    for y in range(2,int(x**0.5 + 1)):
        if x % y == 0:
            
            return "Not prime"
    return "Prime"

T = int(input())
list1 = []
for  x in range(T):
    list1.append(int(input()))
for x in list1:
    print(isPrime(x))