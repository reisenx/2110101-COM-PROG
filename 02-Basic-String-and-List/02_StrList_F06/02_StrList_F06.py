# Create Function add_vector(u,v)
# This function can calculate a sum of 2 input vectors
def add_vector(u,v):
    # Convert a string list into a float list
    ux,uy,uz = float(u[0]), float(u[1]), float(u[2])
    vx,vy,vz = float(v[0]), float(v[1]), float(v[2])

    # Calculate and return the sum vector
    vec_sum=[ux+vx, uy+vy, uz+vz]
    return vec_sum

# Execute the input string
exec(input())