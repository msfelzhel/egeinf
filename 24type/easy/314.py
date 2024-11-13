f = open('D0H9XQ_5J.txt').readline()
f = f.replace('STOCK','!').replace('OCK','*')
print(f.count('*'))