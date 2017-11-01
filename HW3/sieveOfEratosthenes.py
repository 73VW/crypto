"""
    Maël Pedretti
    HE-Arc 2017
    Sieve of Eratosthenes
"""

def iterativeSieve(l):
    while l:
        divider = l[0]
        l = [x for x in l if x%divider is not 0]
        print(divider)

def recursiveSieve(l):
    l_min = min(l)
    l_max = max(l)
    if l_min**2 > l_max:
        for i in l:
            print(i)
    else:
        print(l_min)
        recursiveSieve([x for x in l if x%l_min is not 0])

if __name__ == "__main__":
    LIMITE = 10

    print("Prime numbers under",LIMITE)

    l = list(range(2,LIMITE+1))
    print("iterative version: ")
    iterativeSieve(l)

    l = list(range(2,LIMITE+1))
    print("recursive version: ")
    recursiveSieve(l)
