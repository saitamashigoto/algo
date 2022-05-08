import math

def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    res = []
    for p in range(2, n+1):
        if prime[p]:
            res.append(p)
    return res


def getFactorization(x):
    primes = sieve(int(math.sqrt(x)))
    res = []
    i = 0
    while i < len(primes) and primes[i]*primes[i] <= x:
        if x % primes[i] == 0:
            res.append(primes[i])
            while x % primes[i] == 0:
                x //= primes[i]
        i += 1
    if x > 1:
        res.append(x)
    return res
