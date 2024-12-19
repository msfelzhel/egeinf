f = open('24_4643.txt').readline()
f = f.replace('B','A').replace('2','1')
k = 0
m = 0 
for y in range(3):
    for i in range(y,len(f)-2,3):
        if f[i] + f[i+1] + f[i+2] == '11A':
            k+=1
        else:
            m = max(m,k)
            k = 0
print(m)