def f(x):
    return (x&39 == 0) or ((x&11 == 0) <= (not(x&A ==0)))
m = []
for A in range(1,100):
    if all(f(x) for x in range(1,1000)):
        m.append(A)
print(min(m))
        