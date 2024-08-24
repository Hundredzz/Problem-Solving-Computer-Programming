"""code"""
import math
def f_x(n_v):
    """function"""
    num = 2 + (math.log2(n_v**2)/(2*n_v*math.log2(n_v)))
    return num
def f_y(n_v,s_v):
    """function"""
    num = ((math.sin(math.radians(30)) + math.sqrt(2*s_v))/(f_x(n_v)+3))
    return num
def f_z(k_v):
    """function"""
    num = f_y(k_v,k_v)**2 + ((8456 * f_x(k_v)**4)/(24*k_v))
    return num
def main():
    """function"""
    n_v = float(input())
    s_v = float(input())
    k_v = float(input())
    print(f"X: {f_x(n_v):.1f}, Y: {f_y(n_v,s_v):.1f}, Z: {f_z(k_v):.1f}")
main()
