def dist(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
data = []
fa = open('B18676.txt')
for s in fa:
    p = [float(c) for c in s.split()]
    data.append(p)
print(len(data))
def getk(p0):
    cluster = [p for p in data if dist(p0,p) < 1]
    if len(cluster) > 0:
        for p in cluster: data.remove(p)
        next_cluster = [getk(p) for p in cluster]
        cluster = cluster + sum(next_cluster,[])
    return cluster
clusterA = []
while len(data) > 0:
    p0 = data.pop()
    kll = [p0] + getk(p0)
    print(len(kll))
    clusterA.append(kll)
def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl)
        m.append([sm,p])
    return min(m)[1]
centerA = [center(kl) for kl in clusterA]
px = sum(x for x,y in centerA)/len(clusterA)*100000
py = sum(y for x,y in centerA)/len(clusterA)*100000
print(int(px),int(py))
