for x in '123456789ABC':
    s = int('9' + x + 'AB',13) + int(x + '46C',16) - int('B7' + x,15)
    if s%14 == 0:
        print(x,s/14)