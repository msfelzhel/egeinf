f = open('24_105.txt').readline()
k = 1
m = 0
for i in range(len(f)-1):
    if f[i] == f[i+1]:
        k+=1
    else:
        m = max(m,k)
        k = 1
print(m)