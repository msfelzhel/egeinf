a = [int(x) for x in open('172013.txt')]
ans = []
for i in range(len(a)):
    if (a[i]%10 == 2 or a[i]%10 == 7) and a[i]%3 == 0 and a[i]%11 == 0:
        ans.append(a[i])
print(len(ans),min(ans))