import math
def mosteller(W,H):
    return math.sqrt(W*H)/60

def du_bois(W,H):
    return 0.007184*(W**0.425)*(H**0.725)

def fujimoto(W,H):
    return 0.008883*(W**0.444)*(H**0.663)

def main():
    W = float(input())
    H = float(input())
    mos = mosteller(W,H)
    du = du_bois(W,H)
    fuji = fujimoto(W,H)
    print("Mosteller =",round(mos,5))
    print("Du Bois =",round(du,5))
    print("Fujimoto =",round(fuji,5))

exec(input())