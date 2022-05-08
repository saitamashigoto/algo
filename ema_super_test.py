import random

if __name__ == '__main__':
    fin = open('ema_super', 'w')
    n = random.randint(2, 15)
    m = random.randint(2, 15)
    n = 7
    m = 3
    fin.write('%d %d\n' % (n, m))
    result = ''
    for _ in range(n):
        for _ in range(m):
            result += random.choice([ 'G'])
        result += '\n'
    fin.write(result.rstrip())
    fin.close()        
    