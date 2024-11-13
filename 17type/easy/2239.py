a = [int(x) for x in open('rL3yA3Dr8.txt')]
ans = []
max_all = [x for x in range(len(a)) if x%19 == 0]
for j in range(len(a) - 1):
    if (a[j] > max(max_all)) + (a[j+1] > max(max_all)) >= 1:
        ans.append(a[j] + a[j+1])
print(len(ans),min(ans))