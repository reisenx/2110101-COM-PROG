u = str(input())
v = str(input())

mod_u = u[1 : len(u)-1]
mod_v = v[1 : len(v)-1]

ux,uy,uz = mod_u.split(", ")
vec_u = [float(ux), float(uy), float(uz)]
vx,vy,vz = mod_v.split(", ")
vec_v = [float(vx), float(vy), float(vz)]

ux,uy,uz = vec_u
vx,vy,vz = vec_v
vec_sum = [ux+vx, uy+vy, uz+vz]
print(vec_u, "+", vec_v, "=", vec_sum)