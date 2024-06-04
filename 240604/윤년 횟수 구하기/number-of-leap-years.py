a = int(input())
num =0
for i in range(1,a+1) : 
    if i % 4 == 0 and i%100!=0: num +=1
    elif i % 4 == 0 and i%100==0: num += 0 
    
print(num)