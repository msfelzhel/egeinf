def dist(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return max(abs(x2-x1),abs(y2-y1))
clusters = [[],[]]
fa = open('A18054.txt')
for s in fa:
    x,y = [float(c) for c in s.split()]
    if x>2.5:
        clusters[0].append([x,y])
    else:
        clusters[1].append([x,y])
def centr(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl)
        m.append([sm,p])
    return min(m)[1]
centerA = [centr(kl) for kl in clusters]
pxA = sum(x for x,y in centerA )/2*10000
pyA = sum(y for x,y in centerA)/2*10000
print(int(pxA),int(pyA))