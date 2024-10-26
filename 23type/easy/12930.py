def f(a,b):
    if a > b: return 0 
    if a == b: return 1 
    if a == 11: return 0 
    if a == 12: return 0
    return f(a+1,b) + f(a*2,b) + f(a**2,b)
print(
    f(2,10) * f(10,40)
) 