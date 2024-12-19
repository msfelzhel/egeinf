f = open('24_3584.txt').readline()
k = 0
m = 0
for y in range(2):
    for i in range(y,len(f)-1,2):
        if f[i] + f[i+1] == 'BA' or f[i] + f[i+1] == 'DA':
            k+=1
        else:
            m = max(m,k)
            k = 0
print(m)
