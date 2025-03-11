import sys
b = []
a = int(sys.stdin.readline().rstrip())
for i in range(a):
    b.append(list(map(int, sys.stdin.readline().rstrip().split())))
c = []
def prime_num(g):
    h = []
    g = int(g)
    while(g > 1):
        for l in range(2,g+1):
            if g % l == 0:
                h.append(l)
                g = int(g / l)
                break 
    hi = []
    hj = []
    if not h:  
        return [], []
    hi.append(h[0])
    hj.append(1)
    for m in range(1,len(h)):
        if h[m] == h[m-1]:
            hj[-1] = hj[-1]+1
        else:
            hi.append(h[m])
            hj.append(1)

    return hi ,hj

for j in range(len(b)):

    x1, y1 = prime_num(b[j][0])
    x2, y2 = prime_num(b[j][1])
    ea = []
    for value in x1:
        if value in x2:
            ea.append(x2.index(value))
        else:
            ea.append(-1)
    ea = list(set(ea))
    if -1 in ea:
        ea.remove(-1)
    Xx = 1
    for n in ea:
        ma = max(y1[x1.index(x2[n])] , y2[n])
        mi = min(y1[x1.index(x2[n])] , y2[n])
        if ma ==mi:
            Xx = Xx * (x2[n] ** ma)
        else:
            cd = ma-mi
            Xx = Xx * (x2[n] ** cd)
    
    c.append(int(b[j][0] * b[j][1] / Xx))
for c in c:
    print(c)
