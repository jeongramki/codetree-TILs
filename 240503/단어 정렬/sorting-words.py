n = int(input()) # 숫자 입력

word_list= [ # 
    input() for _ in range(n) # 이게 더 직관적이다
]

word_list.sort()

for word in word_list : 
    print(word)