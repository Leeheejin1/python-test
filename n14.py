a = [int(s) for s in input().split()]
count=0

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            count=count+1
        
print(count)

