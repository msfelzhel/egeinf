def getSum(x): 
    sum = 0
    for digit in str(x): 
      sum += int(digit)      
    return sum
n = '3' * 111
while n.count('33333') >= 1 or n.count('1111',1) >= 1:
    if n.count('33333') >= 1:
        n = n.replace('33333','111',1)
    else:
        n = n.replace('111','33',1)
print(getSum(n))
 

