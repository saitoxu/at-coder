xa, ya, xb, yb, xc, yc = map(lambda i: int(i), input().split(' '))

def main():
    a, b, c, d = move_zero(xa, ya, xb, yb, xc, yc)
    print(abs(a * d - b * c) / 2)

def move_zero(xa, ya, xb, yb, xc, yc):
    return [xb - xa, yb - ya, xc - xa, yc - ya]

main()
