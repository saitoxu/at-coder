# めぐる式二分探索
# ref. https://qiita.com/drken/items/97e37dd6143e33a64c8c


def is_ok(A, index, key):
    return A[index] >= key


def binary_search(A, key):
    ng = -1
    ok = len(A)

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(A, mid, key):
            ok = mid
        else:
            ng = mid

    return ok

if __name__ == "__main__":
    ary = [1, 2, 3, 5, 8]
    print(binary_search(ary, 4)) # => 4
