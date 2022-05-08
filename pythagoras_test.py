import random

if __name__ == '__main__':
    fin = open('pythogoras', 'w')
    c = random.randint(5, 1000)
    fin.write('%d\n' % (c))
    fin.close()
