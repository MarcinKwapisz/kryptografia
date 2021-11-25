# from modul_1.py import GenerujLiczbe
import random
def GenerujLiczbe(k,n):
    k = int(k)
    n = int(n)
    if  n == 0:
        n=int(pow(2,k))
    minimum = 0
    if k < 1 and n < 1:
        return "l>1"
    if k == 1:
        maximum= 1
    else:
        kb = bin(k)[2::]
        minimum = int('1'+'0'*(len(kb)-1),2)
        maximum = n-1
    if minimum < maximum:
        return random.randint(minimum, maximum)
    else:
        return "zakres"

def EfektywnePotegowanie(b, k, n):
    y = 1
    binary = list(reversed(bin(k)[2:]))
    i = len(binary) - 1
    while i >= 0:
        y = (y ** 2) % n
        if binary[i] == "1":
            y = (y * b) % n
        i = i - 1
    return y

def SprawdzPierwsza(n):
    if n == 1:
        return False
    elif n == 2 or n==3:
        return True
    n = int(n)
    licznik = 30
    while (licznik != 0):
        base = int(GenerujLiczbe(2,n - 2))
        if EfektywnePotegowanie(base, n - 1, n) != 1:
            return False
        licznik = licznik -1
    return True

def extendedEuclidean(x, N):
    A, B = N, x
    U, V = 0, 1
    while True:
        q = A // B
        temp1, temp2 = B, A + (-q * B)
        A, B = temp1, temp2
        temp1, temp2 = V, U + (-q * V)
        U, V = temp1, temp2
        if B == 0:
            break
    d, u = A, U
    v = (d - x * u) // N
    return (u, v, d)

def OdwrotnoscWGrupie(n,b):
    n = int(n)
    b=int(b)
    g, x, y = extendedEuclidean(n, b)
    if y == 1:
        return g % b
    else:
        return False

def RSA_Alice_generate():
    #krok 1
    while True:
        p = GenerujLiczbe(2048,0)
        check_p = SprawdzPierwsza(p)
        if check_p:
            print ("Znaleziono p")
            while True:
                q = GenerujLiczbe(2048,0)
                check_q = SprawdzPierwsza(q)
                if (check_p and check_q) and p != q:
                    print (p, " ", q)
                    break
            break
    #krok 2
    n = p*q
    print("n ",n)
    fi = (p-1)*(q-1)
    print("fi ",fi)
    #krok 3
    while True:
        e = random.randint(0,fi)
        m = extendedEuclidean(e, fi)
        if m[2] == 1:
            break
        # print("m !=",m[2])
    print("e ",e)
    #krok 4
    d = OdwrotnoscWGrupie(e, fi)
    print("d ",d)
    #krok 5
    Ka = [n, e]
    ka = [n, d]
    return Ka, ka

def RSA_Bob(Ka):
    n = Ka[0]
    e = Ka[1]
    #krok 2
    M = random.randint(0,n-1)
    print ("M Bob",M)
    #krok 3
    Cipher =  EfektywnePotegowanie(M, e, n)
    # print("Cipher ",Cipher)
    return Cipher

def RSA_Alice_decript(Cipher, ka):
    n = ka[0]
    d = ka[1]
    M = EfektywnePotegowanie(Cipher, d, n)
    print ("M Alice ", M)

Ka, ka = RSA_Alice_generate()
Cipher = RSA_Bob(Ka)
RSA_Alice_decript(Cipher, ka)