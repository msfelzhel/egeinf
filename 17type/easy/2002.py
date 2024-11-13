ans = []
a = [int(x) for x in open('fSPnJFbJE.txt')]
for i in range(len(a)-3):
    sp = [a[i],a[i+1],a[i+2],a[i+3]]
    if a[i] > a[i+1] > a[i+2] > a[i+3]:
        if a[i] - a[i+3] > 1000:
            ans.append(sum(sp))
print(len(ans),min(ans))
