import random

if __name__ == '__main__':
    fin = open('cards', 'w')
    t = 1
    n = random.randint(1, 50000)
    fin.write('%d\n%d\n' % (t, n))
    result = []
    for _ in range(n):
       result.append(str(random.randint(0, n))) 
    fin.write(' '.join(result))
    fin.write('\n')
    fin.close()
