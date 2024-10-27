def dell(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
def p(x):
    if len(dell(x)) == 0:
        return True
    else:
        return False        
for x in range(600001,600501):
    d = dell(x)
    a=x-1
    b=x+1
    if 6 in d:
        if p(a) == True and p(b) == True:
            print(a,b)
