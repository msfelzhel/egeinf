f = open('24_4682.txt').readline()
#AE
#BCD
f = f.replace('E','A')
f = f.replace('C','B').replace('D','B')
f = f.replace('AB','*').replace('A',' ').replace('B',' ')
f = f.split()
print(len(max(f)))