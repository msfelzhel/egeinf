f = open('24_864.txt').readline()
k = 0
m = 0
for i in range(len(f)):
    if f[i] != 'A' and f[i] != 'E':
        k+=1
    else:
        m = max(k,m)
        k = 0
print(m)