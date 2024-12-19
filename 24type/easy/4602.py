f = open('24_4602.txt').readline()
#BCD
#AO
f = f.replace('C','B').replace('D','B')
f = f.replace('O','A')
f = f.replace('BA','*').replace('B',' ').replace('A',' ')
f = f.split()
print(len(max(f)))