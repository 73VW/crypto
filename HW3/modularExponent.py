"""
    Maël Pedretti
    HE-Arc 2017
    Modular Exponent
"""
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

def fastExponent(b, e, m):
    print("Fast version!")
    start_time = time.time()
    c = 1
    while e>0:
        if (e&1)>0 : c = (c*b) % m
        e >>= 1
        b = (b**2) % m
    print("Result is", c, " computed in ", time.time()-start_time, "s")


if __name__ == "__main__":
    B = 12734779
    E = 24397878
    M = 497
    print("Computing modular exponent:\nb={}\te={}\tm={}".format(B,E,M))
    slowExponent(B,E,M)
    fastExponent(B,E,M)
