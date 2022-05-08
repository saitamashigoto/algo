import random

if __name__ == '__main__':
    fin = open('absolute_permutation', 'w')
    t = random.randint(1, 10)
    fin.write(str(t) + '\n')
    for _ in range(t):
        n = random.randint(1, 10**5)
        k = random.randint(0, n-1)
        fin.write(str(n) + ' ' + str(k) + '\n')
    