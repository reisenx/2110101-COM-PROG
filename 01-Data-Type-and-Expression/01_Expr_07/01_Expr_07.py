# Import Math library
import math
# W is a width of an object
# H is a height of an object

# Create function mosteller(W,H)
# Calulate and return body surface area using Mosteller's formula
def mosteller(W,H):
    return math.sqrt(W*H)/60

# Create function du_bois(W,H)
# Calulate and return body surface area using Du Bois's formula
def du_bois(W,H):
    return 0.007184*(W**0.425)*(H**0.725)

# Create function fujimoto(W,H)
# Calulate and return body surface area using Fujimoto's formula
def fujimoto(W,H):
    return 0.008883*(W**0.444)*(H**0.663)

# Create function main()
# main() function can calculate and output each body surface area calculated by those 3 formula
def main():
    W = float(input())
    H = float(input())
    mos = mosteller(W,H)
    du = du_bois(W,H)
    fuji = fujimoto(W,H)
    print("Mosteller =",round(mos,5))
    print("Du Bois =",round(du,5))
    print("Fujimoto =",round(fuji,5))

# Execute the input string
exec(input())
