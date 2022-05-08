import random

if __name__ == '__main__':
    fin = open('sumar', 'w')
    n = 3
    fin.write(str(n))
    fin.write('\n')
    for _ in range(n):
        x1 = ((random.randint(-10**9, 10**9)))
        x2 = ((random.randint(-10**9, 10**9)))
        y1 = ((random.randint(-10**9, 10**9)))
        y2 = ((random.randint(-10**9, 10**9)))
        fin.write('%d %d %d %d' % (x1, x2, y1, y2))
        fin.write('\n')
    fin.close()
