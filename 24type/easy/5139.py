f = open('24_5139.txt').readline()
#BCDF
#AEU
f = f.replace('C','B').replace('D','B').replace('F','B')
f = f.replace('E','A').replace('U','A')
m = 0
k = 0 
for y in range(3):
    for i in range(y,len(f)-2,3):
        if f[i] + f[i+1] + f[i+2] == 'BAB':
            k+=1
        else:
            m = max(k,m)
            k = 0
print(m)
