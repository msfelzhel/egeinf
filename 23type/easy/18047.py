def f(a,b):
    if a<b: return 0 
    if a == b: return 1 
    if a == 24: return 0
    return f(a-2,b) + f(a-3,b) + f(a//4,b)
print(
    f(36,13)
)