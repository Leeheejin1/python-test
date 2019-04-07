b=input('단어를 입력하세요')
c=0
for i in range(0,len(b)):
    if b[i] == 'f':
        print(i,end=" ")
        c= 1
    else:
        if i==len(b)-1 and c==0:
            print(-1)