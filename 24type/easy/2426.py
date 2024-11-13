f = open('242426.txt').readline()
f = f.replace('A',' ').replace('B',' ').replace('C',' ')
ans = [len(c) for c in f.split()]
print(max(ans))