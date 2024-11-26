def dist(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return abs(x2-x1) + abs(y2-y1)
fb = open('B18314.txt')
clusters = [[],[],[]]
for s in fb:
    x,y = [float(c) for c in s.split()]
    if y<-5 and x<0:
        clusters[0].append([x,y])
    elif x < 17:
        clusters[1].append([x,y])
    else:
        clusters[2].append([x,y])
def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p0) for p0 in kl)
        m.append([sm,p])
    return min(m)[1]
centerB = [center(kl) for kl in clusters]
px = sum(x for x,y in centerB)/len(clusters)*1000
py = sum(y for x,y in centerB)/len(clusters)*1000
print(int(px),int(py))