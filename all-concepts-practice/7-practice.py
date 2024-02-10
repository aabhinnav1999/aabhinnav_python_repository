def prod(n,res=1):
    if n==0:
        print('=',res)
        return None
    if n!=1:
        print(n,'x ',end='')
    else:
        print(n,end=' ')
    res*=n
    prod(n-1,res)
prod(6)