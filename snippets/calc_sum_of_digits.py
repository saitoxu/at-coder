# 各桁の和を計算
# ref. https://qiita.com/drken/items/fd4e5e3630d0f5859067#第-5-問--abc-083-b---some-sums-200-点


def calc_sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


if __name__ == "__main__":
    print(calc_sum_of_digits(123)) # => 6
