import sys

def main():
    N = int(input())
    A = list(map(lambda i: int(i), input().split(' ')))
    count = 0
    while True:
        for index, a in enumerate(A):
            if a % 2 == 0:
                A[index] = a // 2
            else:
                print(count)
                sys.exit()
        count += 1
    print(count)

main()
