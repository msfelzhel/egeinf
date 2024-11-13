f = open('242420.txt').readline()
f = f.replace('C',' ').replace('D',' ')
ans = [len(c) for c in f.split()]
print(max(ans))