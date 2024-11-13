a = [int(x) for x in open('_XE8pxWvO.txt')]
ans = []
for i in range(len(a)-1):
    if (abs(a[i]) + abs(a[i+1])) <= 200 and (abs(a[i]) + abs(a[i+1])) >= 50:
        ans.append(min(a[i],a[i+1]))
print(len(ans),min(ans))