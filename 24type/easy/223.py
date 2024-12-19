f = open('24_223.txt').readline()
f = f.replace('TIK','*').replace('TOK','*')
print(f.count('*'))
