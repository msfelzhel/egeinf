x = 16**20 + 2**30 - 32
k = 0
while x>0:
     if x%4 == 3:
         k+=1
     x = x//4
print(k)