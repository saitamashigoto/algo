import random

if __name__ == '__main__':
    fin = open('sherlok_square', 'w')
    l = random.randint(1, 10)
    s1 = random.randint(1, 10)
    s2 = random.randint(1, 10)
    q = random.randint(1, 10)
    fin.write('%d %d %d\n%d\n' % (l, s1, s2, q))
    result = ''
    for _ in range(q):
        result += str(random.randint(1, l**2))
        result += '\n'
    fin.write(result.rstrip())
    fin.close()
