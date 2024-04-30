num = int(input())
arr = list(map(int,input().split()))

differnce = 100
con = 500 

for a in arr : 
    for b in arr : 
        if a != b : 
            if a-b < 0 : con = -(a-b)
            else : con = a-b
        
        if con < differnce : differnce = con


print(differnce)