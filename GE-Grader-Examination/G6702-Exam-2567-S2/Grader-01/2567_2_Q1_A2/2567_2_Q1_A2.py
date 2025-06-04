# Input
T_old = float(input())
T_room = float(input())
delta_t = float(input())
material_type = int(input())
wind_type = int(input())

# Calculate k
k1 = [0.05, 0.02, 0.01, 0.015]
k2 = [1.5, 1.0, 0.8]
k = k1[material_type - 1] * k2[wind_type - 1]

# Calculate total_time and T_final
total_time = delta_t
T_new = T_old - k * (T_old - T_room) * delta_t
# Loop until the temperature difference is less than 10^-3
while(abs(T_old - T_new) >= 10**-3):
    total_time += delta_t
    T_old = T_new
    T_new = T_old - k * (T_old - T_room) * delta_t

# Output
print(round(total_time, 2), round(T_new, 3))

# Material Type
# | Type | Material |  k1   |
# |------|----------|-------|
# |  1   |  Metal   | 0.05  |
# |  2   |  Water   | 0.02  |
# |  3   |  Plastic | 0.01  |
# |  4   |  Others  | 0.015 |
# ---------------------------

# Wind Type
# | Type | Velocity |  k2  |
# |------|----------|------|
# |  1   | > 5 m/s  | 1.5  |
# |  2   | 1-5 m/s  | 1.0  |
# |  3   | < 1 m/s  | 0.8  |
# --------------------------

# Newton's Law of Cooling Formula
# k = k1 * k2
# T_new = T_old - k * (T_old - T_room) * delta_t