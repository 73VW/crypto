"""
    Maël Pedretti
    HE-Arc 2017
    Modular Exponent
"""
import sys
import time


def slowExponent(b, e, m):
    print("Slow version!")
    start_time = time.time()
    c = 1
    e_prime = 1
    while e_prime <= e:
        c = (b*c)%m
        e_prime+=1
    print("Result is", c, " computed in ", time.time()-start_time, "s")

def fastExponent(b, e, m, small_printing):
    if not small_printing:
        print("Fast version!")
    else:
        mystr = "%s^%s mod %s" % (b, e, m)
    start_time = time.time()
    c = 1
    while e>0:
        if (e&1)>0 : c = (c*b) % m
        e >>= 1
        b = (b**2) % m
    if small_printing:
        print(mystr, " = %s" % c)
    else:
        print("Result is", c, " computed in ", time.time()-start_time, "s")


if __name__ == "__main__":
    B = int(sys.argv[1])
    E = int(sys.argv[2])
    M = int(sys.argv[3])
    small_printing = False
    try:
        small_printing = bool(sys.argv[4])
    except Exception:
        pass
    if small_printing is False:
        print("Computing modular exponent:\nb={}\te={}\tm={}".format(B,E,M))
        slowExponent(B,E,M)
    fastExponent(B,E,M, small_printing)
