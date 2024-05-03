A= input()
B= input()

cnt = 0 

if len(A) != len (B) : print('No')
else : 
    for i in range(len(A)) : 
        if A[i] != B[i] : cnt +=1
        else : pass
    
    if cnt > 3 : print('No')
    else : print('Yes')