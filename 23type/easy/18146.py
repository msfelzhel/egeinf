def f(a,b):
    if a < b: return 0
    if a == b: return 1 
    if a == 28: return 0 
    if a != 28: return f(a-3,b) + f(a//3,b) + f(a//2,b)
print(f(46,20)*f(20,3))