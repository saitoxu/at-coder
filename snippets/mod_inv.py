# 拡張Euclidの互除法による逆元計算
# ref. https://drken1215.hatenablog.com/entry/2018/06/08/210000


# ax + by = gcd(a, b)となるような(x, y)を求める
# 返り値は(gcd(a, b), x, y)のtuple
def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, y, x = ext_gcd(b, a % b)
    return d, x - (b // a) * y, y


# 非再帰バージョン
def ext_gcd2(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


# 逆元計算(aとmは互いに素であることが必要)
def mod_inv(a, m):
    _, x, _ = ext_gcd(a, m)
    return x % m


if __name__ == "__main__":
    print(mod_inv(2, 13)) # => 7
