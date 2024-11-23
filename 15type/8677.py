def f(x):
    B = 80 <= x <= 100
    return (x%17 == 0) <= (not(B) or (A < x + 30))
m = []
for A in range(1,10000):
    if all(f(x) for x in range(1,100000)):
        m.append(A)
print(max(m))