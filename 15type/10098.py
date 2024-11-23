def f(x,y):
    return (x+2*y < A) or (y > x) or (x > 60)
m = []
for A in range(1,1000):
    if all(f(x,y) for x in range(100) for y in range(100)):
        m.append(A)
print(min(m))
        