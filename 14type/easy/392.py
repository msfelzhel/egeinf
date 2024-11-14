x = (2**345 + 8**65 - 4**130)*(8**123 - 2**89 + 4**45)
ans = ''
while x>0:
    ans = str(x%8) + ans
    x = x//8
sym = 0
for i in ans:
    sym += int(i)
print(sym)