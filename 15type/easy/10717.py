def treyg(a,b,c):
    return max(a,b,c) < a+b+c - max(a,b,c)
def f(x):
    return not((treyg(x,11,18) == (not(max(x,5) > 68 ))) and (treyg(x,A,5)))
m = []
for A in range(1,100):
    if all(f(x) for x in range(1,1000)):
        m.append(A)
print(max(m))


