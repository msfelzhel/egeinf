a = [int(x) for x in open('p1tufp-t9.txt')]
ans = []

for i in range(len(a)-2):
    sr = (sum(a)/len(a))
    sl = [a[i],a[i+1],a[i+2]]
    if (a[i] > sr and a[i+1] > sr) or (a[i+1] > sr and a[i+2] > sr) or (a[i] > sr and a[i+2] > sr):
        ans.append(sum(sl))
print(len(ans),max(ans))