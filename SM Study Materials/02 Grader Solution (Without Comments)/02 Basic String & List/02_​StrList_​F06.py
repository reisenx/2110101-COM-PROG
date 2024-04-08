def add_vector(u,v):
    ux,uy,uz = float(u[0]), float(u[1]), float(u[2])
    vx,vy,vz = float(v[0]), float(v[1]), float(v[2])
    vec_sum=[ux+vx, uy+vy, uz+vz]
    return vec_sum

exec(input())