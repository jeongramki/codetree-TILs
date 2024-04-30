arr = list(map(int,input().split()))

max=1
min = 1000000
for elem in arr : 
    if max < elem < 500 : max = elem
    if 500 < elem < min : min = elem 

print(max, min)