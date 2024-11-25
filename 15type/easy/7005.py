def ygol(a,b,c):
    return a+b+c == 180
def f(x):
    return ygol(37,A,x+45) == ygol(A,x,90) and (not((A+23<120)))
m = []
for A in range(1,100):
    if all(f(x) for x in range(1,1000)):
        m.append(A)
print(min(m))