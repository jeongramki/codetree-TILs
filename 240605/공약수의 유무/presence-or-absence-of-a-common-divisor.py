arr = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 24, 30, 32, 40, 48, 60, 64, 80, 96, 120, 160, 192, 240, 320, 480, 960]

a, b = map(int, input().split())
result = 0
for i in range(a,b+1) :
    if i in arr :  result = 1

print(result)