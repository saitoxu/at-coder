N, K = map(lambda i: int(i), input().split(' '))
R = list(map(lambda i: int(i), input().split(' ')))

def main():
    rate = 0
    R.sort()
    for i in range(0, K):
        rate = (rate + R[i + N - K]) / 2
    print(rate)

main()
