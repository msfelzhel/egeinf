def f(a,b):
    if a < b: return 0
    if a == b: return 1 
    return f(a-4,b) + f(a-7,b) + f(int(a**0.5),b)
print(
    f(44,22) * f(22,3)
)