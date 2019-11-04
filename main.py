def main():
    N, A, B = map(lambda i: int(i), input().split())
    numbers = []
    for i in range(N):
        num = sum(list(map(lambda i: int(i), list(str(i + 1)))))
        if num >= A and num <= B:
            numbers.append(i + 1)

    print(sum(numbers))

main()
