def dist(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
data = []
fb = open('B18051.txt')
for s in fb:
    p = [float(c) for c in s.split()]
    data.append(p)
def getcl(p0):
    clusters = [p for p in data if dist(p0,p) < 0.2]
    if len(clusters) > 0:
        for p in clusters: data.remove(p)
        next_cluster = [getcl(p) for p in clusters]
        clusters = clusters + sum(next_cluster,[])
    return clusters
clustersB = []
while len(data) > 0:
    p0 = data.pop()
    kl1 = [p0] + getcl(p0)
    clustersB.append(kl1)
print(len(clustersB))
def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl) # поиск центроидов
        m.append([sm,p])
    return min(m)[1]
centerB = [center(kl) for kl in clustersB]
pxA = sum(x for x,y in centerB)/len(clustersB)*10000
pyA = sum(y for x,y in centerB)/len(clustersB)*10000
print(int(pxA),int(pyA))

