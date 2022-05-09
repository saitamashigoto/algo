import math
import sys



def solve(min, max):
    n, d = (estimatePi(max))
    return '%d/%d' % (n, d)


def estimatePi(n):
    n3 = n*3
    start = 1
    end = n-1
    mT = 0
    i = 0
    while start <= end:
        # if i >= 10**1:
        #     break
        # i += 1
        nTerms = end-start + 1
        
        if nTerms%2:
            mT = start + nTerms//2
            valL = abs((n3 + mT-1)/n - math.pi)
            val = abs((n3 + mT)/n - math.pi)
            valH = abs((n3 + mT+1)/n - math.pi)
            if val < valH and valL < val:
                end = mT
            elif val > valH and valL > val:
                start = mT
            else:
                break
        else:
            mT = start + nTerms//2 - 1
            valL = abs((n3 + mT)/n - math.pi)
            valH = abs((n3 + mT+1)/n - math.pi)
            if valL < valH:
                end = mT
            elif valH < valL:
                start = mT
            if nTerms == 2:
                if valH < valL:
                    mT += 1
                break
    return (n3 + mT, n)


if __name__ == '__main__':
    fptr = sys.stdout

    min, max = list(map(int, input().strip().split()))
    result = solve(min, max)

    fptr.write(result + '\n')

    fptr.close()
