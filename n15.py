a = input().split()
dics={}
for i in a:
    if i not in dics:
        dics[i] =0
    else:
        dics[i]+=1
    print(dics[i],end=" ")
