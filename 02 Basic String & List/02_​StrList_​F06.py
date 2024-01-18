# Create Function add_vector(u,v)
# This function can calculate a sum of 2 input vectors
def add_vector(u,v):
    # Convert a string list into a float list
    vec_u = [float(u[0]), float(u[1]), float(u[2])]
    vec_v = [float(v[0]), float(v[1]), float(v[2])]

    # Calculate and return the sum vector
    vec_sum=[vec_u[0]+vec_v[0], vec_u[1]+vec_v[1], vec_u[2]+vec_v[2]]
    return vec_sum

# Execute the input string
exec(input())