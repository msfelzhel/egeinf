a = [int(x) for x in open('171998.txt')]
ans = []
for i in range(len(a)-2):
    if abs(a[i]*a[i+1]*a[i+2])%7 == 0:
        if (a[i]+a[i+1]+a[i+2])%10 == 5:
            ans.append(a[i]+a[i+1]+a[i+2])
print(len(ans),max(ans))