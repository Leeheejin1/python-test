fib=1
pre=1
ppre=0
count=1

x=int(input('수를 입력하시오:'))
while x >= fib :
    if x==1:
        fib=1
    elif fib==x:
        print(count)
        break
    else :
        fib=pre+ppre
        ppre=pre
        pre=fib
    count=count+1
else :
    print(-1)
