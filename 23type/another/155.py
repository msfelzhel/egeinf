def f(a,b):
    if a<b: return 0
    if a==b : return 1
    if a>b: return f(a-1,b) + f(int((a+1)//2),b)

print(f(78,16) * f(16,4))