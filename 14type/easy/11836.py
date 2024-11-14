for x in '0123456789ABCDEFGHIJKLMNOPQRSTUV':
    s = int('931' + x + '964',32) + int('4' + x + '51' + x + '1',32)
    a = s + int('2861' + x + '637',32)
    if a%31 == 0:
        print(x,a/31)
