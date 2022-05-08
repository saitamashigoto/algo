import random

if __name__ == '__main__':
    fin = open('sherlok-count', 'w')
    q = random.randint(1, 10**5)
    q = 10**5
    fin.write('%d\n' % (q))
    for _ in range(q):
        n = random.randint(1, 10**9)
        k = random.randint(1, 10**9)
        fin.write('%d %d\n' % (n, k))
    fin.close()
