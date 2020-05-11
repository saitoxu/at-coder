# nCk mod. pの計算
# ref. https://drken1215.hatenablog.com/entry/2018/06/08/210000

mod = 10 ** 9 + 7
N = 2 * 10 ** 5

fac = [0] * N
finv = [0] * N
inv = [0] * N

fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2, N):
    fac[i] = fac[i - 1] * i % mod
    # mod pにおける1, 2, ..., nの逆元
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    finv[i] = finv[i - 1] * inv[i] % mod


def com(n, k):
    global fac, finv, mod
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


if __name__ == "__main__":
    print(com(10, 2)) # => 45
