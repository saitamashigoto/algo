import random

if __name__ == '__main__':
    fin = open('test.txt', 'w')
    n = random.randint(1, 10**5)
    k = random.randint(1, 100)
    seq = []
    for _ in range(n):
        seq.append(str(random.randint(1, 10**9)))
    fin.write(str(n))
    fin.write(' ')
    fin.write(str(k))
    fin.write('\n')
    fin.write(' '.join(seq))
    fin.write('\n')
    fin.close()
    