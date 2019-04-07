i=1
fib=1
pre=1
ppre=0
x=int(input('수를 입력하시오:'))
while(i != x):
    if x==1:
        fib=1
    else:
        fib=pre+ppre
        ppre=pre
        pre=fib
    i=i+1
print(fib)