def dist(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5 #нахождение расстояние между точками
fa = open('A18051.txt')
clustestersA = [[],[]]
for s in fa:
    x,y = [float(c) for c in s.split()]
    if x>1.0029:
        clustestersA[0].append([x,y])
    else:
        clustestersA[1].append([x,y])
def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl) # поиск центроидов
        m.append([sm,p])
    return min(m)[1]
centerA = [center(kl) for kl in clustestersA]
pxA = sum(x for x,y in centerA)/2*10000
pyA = sum(y for x,y in centerA)/2*10000
print(int(pxA),int(pyA))