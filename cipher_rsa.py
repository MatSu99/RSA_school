import random
import math


def key_generator():  # It will generate components of RSA algorithm n, d, e
    pq = pq_gen(2)
    n_d_e = rsa_components(pq[0], pq[1])
    n = n_d_e[0]
    d = n_d_e[1]
    e = n_d_e[2]
    return n, d, e


def ex_euk_al(a,b):  # Extended euclidean formula for generating n, e, d of RSA algorithm
    xs=[1,0]        # initial values
    ys=[0,1]
    sign=1
    while b!=0:
        r=a%b
        q=a//b
        a=b
        b=r
        xx=xs[1]
        yy=ys[1]
        xs[1]=q*xs[1]+xs[0] # creation of a sequence xs
        ys[1]=q*ys[1]+ys[0] # creation of a sequence ys
        xs[0]=xx
        ys[0]=yy
        sign=-sign
    # computation of coefficients x and y
    x=sign*xs[0]
    y=-sign*ys[0]
    return [a, x, y]


def pq_gen(t):  # It will generate two different prime numbers, based on Miller-Rabin test
    p = 0
    q = 0

    for i in range(2):
            while True:
                n = random.randint(pow(10, 4)+1, pow(20, 4)+1)
                if miller_rabin(t,n) == True:
                    if i == 0:
                        p = n
                    if i == 1:
                        q = n
                    break
    print("p = ", p)
    print("q = ", q)
    return (p, q) # touple


def rsa_components(p, q):  # Generates n, d, e for RSA  algorithm
    totient = (p-1) * (q-1)
    print("Totient =", totient)
    n = p * q

    while True:
        e = random.randint(3,totient)
        if math.gcd(e,totient) == 1:
            break

    l = ex_euk_al(e,totient)
    if l[0] == 1:
        d = l[1]%totient
    else:
        print("ERROR 4; looking for d")

    print("d = ", d)
    print("e = ", e)
    print("n = ", n)
    return n, e, d # Returns tuple


def rsa_encrypt(m ,n, e):  # RSA encryption m^e mod n
    a = fast_power(m, e, n)
    return a


def rsa_decrypt(c, n, d):  # RSA encryption c^d mod n
    m = fast_power(c, d, n)
    return m


def fast_power(a, k, n):  #  a^k % N FOR BIG NUMBERS
    b = 1
    while k != 0:
        ki = k % 2
        k = k//2
        b = (b * (a**ki)) % n
        a = (a * a) % n
    return b


def miller_rabin(t,n):  # Miller-Rabin test implementation
    n1 = n - 1
    s = 0
    d =n1
    while (d % 2) == 0:
        d = d//2
        s = s + 1

    for i in range(t):
        pseudo = 0
        a = random.randrange(2, n1, 1)
        y = fast_power(a, d, n)

        if y!= 1 and y != n1:
            j = 1
            while j < s:
                y = (y*y) % n
                if y == n1:
                    pseudo = 1
                    exit
                j = j+1
        else:
            pseudo = 1

        if pseudo == 0:
            return False
    return True




def initial_vect_generator(a):  # warning, generated string doesn't come from secret library
    iv = ""                     # Function to generate initial vector a-bits
    for i in range(a):
        iv = iv + str(random.randint(0,1))

    return iv
