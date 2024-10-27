def dell(n):
    d = set()
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d) 
def p(a):
    return a>1 and all(a%i!=0 for i in range(2,int(a**0.5)+1))

for x in range(1000,9999+1):
    s = sum(dell(x))
    if s%100 == 23:
        print(x,s)
    
   