num = int(input())

count = 0
i=0
while count !=2 :
    
    i+=1
    print(num * i , end = ' ')
    if (num*i%5) == 0 : count +=1