f = open('24_4642.txt').readline()
f = f.replace('B','A').replace('2','1')
f = f.replace('A1','*').replace('A',' ').replace('B',' ')
f = f.split()
print(len(max(f)))