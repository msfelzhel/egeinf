def f(s,m):
    if s > 20: return m%2 == 0
    if m == 0: return 0
    h = [f(s+1,m-1),f(s+2,m-1),f(s+3,m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)
def z(s,m):
    if s > 20: return m%2 == 0
    if m == 0: return 0
    h = [z(s+1,m-1),z(s+2,m-1),z(s+3,m-1)]
    return any(h) if (m-1)%2 == 0 else any(h)
print(*[s for s in range(1,20) if f(s,2)])
print(*[s for s in range(1,20) if f(s,5)][0:3])
print(len([s for s in range(1,20) if z(s,2)]))