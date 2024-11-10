a = [int(x) for x in open('172015.txt')]
ans = []
for i in range(len(a)):
    if (a[i]%10 == 5 or a[i]%10 == 7) and a[i]%9 != 0 and a[i]%11 != 0:
        ans.append(a[i])
print(len(ans),(max(ans) + min(ans)))