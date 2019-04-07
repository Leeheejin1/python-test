card = int(input('카드의 개수를 입력하세요:'))
b= list()
for i in range(card-1):
    b.append(int(input()))
print(b)
for k in range(1,card+1):
    if k in b:
        pass
    else:
        print(k)