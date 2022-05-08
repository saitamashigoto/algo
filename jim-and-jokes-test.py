import random

if __name__ == '__main__':
    days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    fin = open('jim-and-jokes', 'w')
    n = random.randint(1, 100000)
    fin.write('%d\n' % (n))
    result = []
    for _ in range(n):
        m = random.randint(1, 12)
        d = random.randint(1, days[m])
        fin.write('%d %d\n' % (m, d))
    
    fin.close()
