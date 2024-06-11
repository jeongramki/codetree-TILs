n,m = map(int, input().split())

cnt =1 

answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n*m) : 
    for row in range(n) : 
        for col in range(m) : 
            if row + col == i : answer[row][col]= cnt ;cnt +=1


for row in range(n) : 
        for col in range(m) : 
            print(answer[row][col], end = ' ')
        print()