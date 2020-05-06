# logNのべき乗
# ref. https://ttrsq.exblog.jp/24414256/


def pow(x, y):
    a = 1
    b = x
    c = y
    while c > 0:
        if c & 1:
            a = a * b
        b = b * b
        c = c >> 1
    return a

if __name__ == "__main__":
    print(pow(2, 10))  # => 1024
