f = open('4637.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if a[3]*a[3]*a[3] >= 2*a[0]*a[1]*a[2] and a[0] > 10 and a[1] > 10 and a[2] > 10 and a[3] > 10:
        k+=1
print(k)
        
    
