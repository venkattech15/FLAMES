x=str(input())
y=str(input())
n=list(x)
m=list(y)
def same(x,y):
    h=list()
    k=list()
    c=x.copy()
    d=y.copy()
    for i in range(0,len(x)):
        for j in range(0,len(d)):
            if x[i]==d[j]:
                h.append(i)
                del d[j]
                break
    c=[i for j,i in enumerate(c) if j not in h ]
    return len(c)+len(d)
v=same(n,m)
def flame(v):
    t=list("flames")
    p = list("flames")
    while len(t)<v:
        t.extend(t)
    for i in range(0,5):
        n = t[v-1]
        del t[0:v]
        p.remove(n)
        if n in t:
            t.remove(n)
        while len(t)<v:
            t.extend(p)
    return p[0]
d={'f':"friends",'l':"love",'a':"affection",'m':"marriage",'e':"enemies",'s':"sister"}
i=flame(v)
print('{0} and {1} are {2}'.format(x,y,d[i]))






