from itertools import combinations

def f(x):
    P = 15 <= x <= 33
    Q = 35 <= x <= 48
    A = a1 <= x <= a2
    return (A and (not(Q))) <= (P or Q)

ox = [i//4 for i in range(15*4,48*4+1)]
m = []
for a1,a2 in combinations(ox,2):
    if all(f(x) for x in ox):
        m.append(a2-a1)
print(max(m))