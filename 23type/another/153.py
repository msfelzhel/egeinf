def f(a,b,k:str):
    if a>b: return 0
    if a==b: return 1
    if a<b:
        if k != '!':
            if k != '+':
                return f(a+1,b,'+') + f(a+2,b,'+')
            if k != '*':
                return f(a*2,b,'*') + f(a*3,b,'*')
        else:
            return f(a*2,b,'*') + f(a*3,b,'*') + f(a+1,b,'+') + f(a+2,b,'+')

print(f(1,22,'!'))