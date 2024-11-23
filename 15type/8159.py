def f(x,y):
    B = 50 <= x <= 70
    return (2*x + y != 150) or not(B) or (A > y)
m = []
for A in range(1,1000):
    if all(f(x,y) for x in range(1,100) for y in range(1,100)):
        m.append(A)
print(min(m))