a = [int(x) for x in open('172402.txt')]
ans = []
for i in range(len(a)-2):
    if a[i]%3 == 2 or a[i+1]%3 == 2 or a[i+2]%3 == 2:
        ans.append(min(a[i],a[i+1],a[i+2]))
print(len(ans),sum(ans))