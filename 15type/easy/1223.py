from itertools import combinations

def f(x):
    B = 25 <= x <= 40
    C = 12 <= x <= 33
    A = a1 <= x <= a2
    return (B <= A) and (not(C) or A)

ox = [i/4 for i in range(12*4,40*4+1)]
m = []
for a1,a2 in combinations(ox,2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(min(m))