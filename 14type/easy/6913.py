for x in '0123456789ABCDEFGHIJKLMNOPQRSTUVW':
    s = int('12' + x + '34',33) + int('49' + x + '9',33)
    if s%19 == 0:
        print(x,s/19)