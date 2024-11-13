a = [int(x) for x in open('NSE-Nyyaf.txt')]
ans = []
for i in range(len(a)-1):
    if a[i] + a[i+1] >= 100 and (a[i] < 0 or a[i+1] < 0):
        ans.append(a[i]*a[i+1])
print(len(ans),max(ans))