import random

if __name__ == '__main__':
    fin = open('diff-prod', 'w')
    n = random.randint(0, 10**9)
    m = random.randint(0, 10**9)
    fin.write('1\n%d %d\n' % (n, m))
    fin.close()
