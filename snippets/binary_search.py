# 二分探索
# ref. https://www.geeksforgeeks.org/python-program-for-binary-search/


def binary_search(arr, l, r, x):
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, l, mid - 1, x)
        else: 
            return binary_search(arr, mid + 1, r, x)
    else: 
        return -1


if __name__ == "__main__":
    ary = [1, 2, 3, 4, 5]
    print(binary_search(ary, 0, len(ary) - 1, 2)) # => 1
