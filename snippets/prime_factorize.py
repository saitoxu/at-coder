# 試し割り法による素因数分解
# ref. https://note.nkmk.me/python-prime-factorization/


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

if __name__ == "__main__":
    print(prime_factorize(12)) # => [2, 2, 3]
