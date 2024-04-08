h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

t1 = (h1*3600) + (m1*60) + s1
t2 = (h2*3600) + (m2*60) + s2

dt = ((24*3600) + t2 - t1) % (24*3600)
dh = dt//3600
dt = dt-(dh*3600)
dm = dt//60
dt = dt-(dm*60)
ds = dt

print(str(dh) + ":" + str(dm) + ":" + str(ds))