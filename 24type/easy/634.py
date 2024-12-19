f = open('24_634.txt').readlines()
k = 0
for s in f:
    c = 0
    for i in range(len(s)-3):
        if s[i] + s[i+2] + s[i+3] == 'ZRO':
            c +=1
    if c > 0:
        k+=1
        
print(k)
