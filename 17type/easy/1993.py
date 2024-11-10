a = [int(x) for x in open('171993.txt')]
ans = []
for i in range(len(a) - 1):
    if (a[i] + a[i+1])%3 == 0:
        if (a[i] + a[i+1])%6 != 0:
            if abs(a[i]*a[i+1])%10 == 8:
                ans.append(a[i]+a[i+1])
print(len(ans),max(ans))