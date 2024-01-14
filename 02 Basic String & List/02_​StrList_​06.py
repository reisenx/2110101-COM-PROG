#Input u and v vector as a string
u=str(input())
v=str(input())

#Delete "[]" Bracket from u and v string
mod_u=u[1:len(u)-1:1]
mod_v=v[1:len(v)-1:1]

#Then split u and v string
vec_u = mod_u.split(", ")
vec_u = [float(vec_u[0]), float(vec_u[1]), float(vec_u[2])]
vec_v = mod_v.split(", ")
vec_v = [float(vec_v[0]), float(vec_v[1]), float(vec_v[2])]

#Calculate and output the sum vector
vec_sum=[vec_u[0]+vec_v[0], vec_u[1]+vec_v[1], vec_u[2]+vec_v[2]]
print(vec_u, "+", vec_v, "=", vec_sum)