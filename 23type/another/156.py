def f(a,b):
    if a>b: return 0
    if a==b: return 1
    if a<b: return f(a+1,b) + f(a*1.5,b)

print(f(1,22))