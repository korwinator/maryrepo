

def D(n):
    if n == 0 or n == 1:
        return 1
    if n > 1 and n % 2 == 0:
        return D(n//4) + 1
    if n > 1 and n % 2:
        return D((3*n)+1) + 1

print(D(357))


def ND(n):
    W = 0
    while(1):
        if n == 0 or n == 1:
            W += 1
            return W
        elif n % 2 == 0:
            n = n//4
        else:
            n = 3*n + 1
        W += 1

print(ND(5))

