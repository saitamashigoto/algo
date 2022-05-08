import random

if __name__ == '__main__':
    fin = open('rectangle', 'w')
    q = 1
    p = 2
    r = 0
    
    fin.write('%d\n' % (q))
    for _ in range(q):
        n = 10
        fin.write('%d\n' % (n))
        for _ in range(n):
            x, y = random.randint(r, p), random.randint(r, p)
            fin.write('%d %d\n' % (x, y))
    fin.close()
