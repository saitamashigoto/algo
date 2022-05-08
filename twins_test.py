import random

if __name__ == '__main__':
    fin = open('twins', 'w')
    n = random.randint(1, 10**9)
    m = random.randint(n, 10**9)
    fin.write('%d %d\n' % (n, m))
    fin.close()  