n = int(input())

result = False 

for i in range(2,n) : 
    if n%i == 0 : result = True

if result == True : print('C')
else : print('N')