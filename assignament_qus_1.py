def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a,end=" ")
        print(b,end=" ")
        for n in range(2,n):
            c=a+b
            a=b
            b=c
            print(c,end=" ") 
fib(10)