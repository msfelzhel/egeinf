def dist(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5 #нахождение расстояние между точками
clustersA = [[],[]]
fa = open('A17916.txt')
for s in fa:
    x,y = [float(c) for c in s.split()]
    if y>8:
        clustersA[0].append([x,y])   #разбиение по плоскостям
    else:
        clustersA[1].append([x,y])
fb = open('B17916.txt')
data = []
for s in fb:
    p = [float(c) for c in s.split()] #добвление точек файла B 
    data.append(p)
def getkl(p0):
    clustersB = [p for p in data if dist(p0,p)<1]
    if len(clustersB)>0:
        for p in clustersB: data.remove(p)
        next_clustersB = [getkl(p) for p in clustersB]
        clustersB = clustersB + sum(next_clustersB,[])  #алгоритм разбиения файла по соседям 
    return clustersB
clustersB = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + getkl(p0) #разбиение кластера B алгоритмом 
    clustersB.append(cluster)
def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl) # поиск центроидов
        m.append([sm,p])
    return min(m)[1]
centerA = [center(kl) for kl in clustersA]
centerB = [center(kl) for kl in clustersB]
pxA = sum(x for x,y in centerA)/2*10000
pyA = sum(y for x,y in centerA)/2*10000
print(int(pxA),int(pyA))
pxB = sum(x for x,y in centerB)/5*10000
pyB = sum(y for x,y in centerB)/5*10000
print(int(pxB),int(pyB))

