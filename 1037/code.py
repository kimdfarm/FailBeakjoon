import sys
e = 1
def lcm(a,b):
    c , d = a,b
    while b:
        a ,b = b, a% b        
    return c * d / a
a = int(sys.stdin.readline().rstrip())
b = list(map(int,sys.stdin.readline().rstrip().split()))
b = b[:a]
if len(b) == 1:
    print(b[0] * 2)
else:
    for i in range(len(b)):
        e = int(lcm(e,b[i]))
    if e in b:
        e = int(e * 2)
    print(e)
