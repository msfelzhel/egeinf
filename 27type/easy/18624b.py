def dist(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
data = []
fb = open('B18624.txt')
for s in fb:
    p = [float(c) for c in s.split()]
    data.append(p)
def getkk(p0):
    clusters = [p for p in data if dist(p0,p) < 1]
    if len(clusters) > 0:
        for p in clusters: data.remove(p)
        next_cluster = [getkk(p) for p in clusters]
        clusters = clusters + sum(next_cluster,[])
    return clusters
clustersB = []
while len(data) > 0:
    p0 = data.pop()
    kll = [p0] + getkk(p0)
    clustersB.append(kll)
def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl)
        m.append([sm,p])
    return min(m)[1]
centerB = [center(kl) for kl in clustersB]
px = sum(x for x,y in centerB)/len(clustersB)*100000
py = sum(y for x,y in centerB)/len(clustersB)*100000
print(int(px),int(py))