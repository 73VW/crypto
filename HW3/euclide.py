"""
    Maël Pedretti
    HE-Arc 2017
    Extended Euclide Algorithm

    Base code can be found in slide 64
"""
import sys
def extendedEuclid(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r is not 0:
        quotient = old_r // r
        old_r, r = r, (old_r - quotient * r)
        old_s, s = s, (old_s - quotient * s)
        old_t, t = t, (old_t - quotient * t)

    print("Bézout coefficients:", old_s, old_t)
    print("greatest common divisor:", old_r)
    print("quotients by the gcd:", t, s)

if __name__ == "__main__":
    extendedEuclid(int(sys.argv[1]), int(sys.argv[2]))
