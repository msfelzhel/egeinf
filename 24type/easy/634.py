f = open('24_634.txt').readlines()
c = 0
k = 0
for s in f:
    k = 0
    for i in range(len(s)-3):
        if s[i] + s[i+2] + s[i+3] == 'ZRO':
            k+=1
    if k > 0:
        c+=1
print(c)