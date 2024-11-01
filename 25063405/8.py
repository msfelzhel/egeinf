alf = '0123456'
k = 0
for a1 in '123456':
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    for a6 in alf:
                        for a7 in alf:
                            a = a1+a2+a3+a4+a5+a6+a7
                            if (a.count('2') == 2 and a.count('6') == 0 and a.count('4') == 0) or (a.count('2') == 0 and a.count('6') == 2 and a.count('4') == 0) or (a.count('2') == 0 and a.count('6') == 0 and a.count('4') == 2): 
                                k+=1
                            if (a.count('2') == 1 and a.count('6') == 1 and a.count('4') == 0) or (a.count('2') == 1 and a.count('6') == 0 and a.count('4') == 1) or (a.count('2') == 0 and a.count('6') == 1 and a.count('4') == 1):
                                k+=1
print(k)