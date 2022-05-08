import random

if __name__ == '__main__':
    fin = open('bus-station', 'w')
    n = random.randint(1, 5)
    r = random.randint(1, 10)
    c = random.randint(1, 10)
    fin.write('%d %d %d\n' % (r, c, n))
    result = ''
    for i in range(r):
        for j in range(c):
            result += (random.choice(['.', '.']))
        result += '\n'
    fin.write(result.rstrip())
    fin.close()        
        
    