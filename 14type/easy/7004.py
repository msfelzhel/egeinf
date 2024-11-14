for x in '0123456789ABCDEF':
    s = s1 = int('B7A' + x + '9',16) + int('54'+ x + 'ED',16)
    sv6 = ''
    while s>0:
        sv6 = str(s%6) + sv6
        s = s//6
    sans = 0
    for i in sv6:
        sans += int(i)
    if sans == 25:
        print(x,s1)
    ## другая идея
    #sqm = 0
    #for i in str(s):
        #sqm += int(i)
    # = ''
    #while sqm > 0:
        # = str(sqm%6) + sum_ans
        #sqm = sqm//6
    #print(sum_ans)
    #if int(sum_ans) == 25:
        #print(x,s)
