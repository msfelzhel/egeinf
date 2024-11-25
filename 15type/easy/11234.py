from itertools import combinations
def f(x):
    B = 120 <= x <= 130 
    return (B <= (x%7!=0)) or (A > 2*x)
m = []
for A in range(1,1000):
    if all(f(x) for x in range(1,10000)): 
        m.append(A)
print(min(m))