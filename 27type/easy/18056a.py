def dist(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
data = []
fa = open('A18056.txt')
for s in fa:
    p = [float(c) for c in s.split()]
    data.append(p)
def getk(p0):
    clusters = [p for p in data if dist(p0,p) < 1]
    if len(clusters) > 0:
        for p in clusters: data.remove(p)
        next_cluster = [getk(p) for p in clusters]
        clusters = clusters + sum(next_cluster,[])
    return clusters
clustersA = []
while len(data) > 0:
    p0 = data.pop()
    kll = [p0] + getk(p0)
    print(len(kll))
    clustersA.append(kll)
clustersA = [kl for kl in clustersA if len(kl) > 10]
def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl)
        m.append([sm,p])
    return min(m)[1]
centerA = [center(kl) for kl in clustersA]
px = sum(x for x,y in centerA)/len(clustersA)*100000
py = sum(y for x,y in centerA)/len(clustersA)*100000
print(int(px),int(py))