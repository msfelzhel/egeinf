def dist(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return abs(x2-x1)+abs(y2-y1)
fa = open('A18314.txt')
clustersA = [[],[]]
for s in fa:
    x,y = [float(c) for c in s.split()]
    if x>23:
        clustersA[0].append([x,y])
    else:
        clustersA[1].append([x,y])
def centr(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl)
        m.append([sm,p])
    return min(m)[1]
centrA = [centr(kl) for kl in clustersA]
pxA = sum(x for x,y in centrA)/len(clustersA)*1000
pyA = sum(y for x,y in centrA)/len(clustersA)*1000
print(int(pxA),int(pyA))