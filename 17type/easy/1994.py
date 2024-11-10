a = [int(x) for x in open('171994.txt')]
ans = []
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) %7 == 0:
        if (a[i] * a[i+1]) > 0:
            ans.append((a[i] * a[i+1]))
print(len(ans),min(ans))