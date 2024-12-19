f = open('24_4627.txt').readline()
m = 0
k = 0
for y in range(3):
    for i in range(y,len(f)-2,3):
        if f[i] + f[i+1] + f[i+2] == 'NPO' or f[i] + f[i+1] + f[i+2] == 'PNO':
            k+=1
        else:
            m = max(m,k)
            k = 0
print(m)