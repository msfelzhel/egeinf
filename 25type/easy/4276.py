def dell(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
for x in range(400_000_001,400_000_011):
    d = dell(x)
    if len(d) >= 7:
       print(d[7],len(d))
