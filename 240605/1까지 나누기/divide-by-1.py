n=int(input())
cnt =0
i = 1

while n > 1 : 
    cnt +=1 
    n = n// i 
    i+=1
print(cnt)