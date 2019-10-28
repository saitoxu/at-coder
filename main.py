N = int(input())

def main():
    cards = ['1', '2', '3', '4', '5', '6']
    for i in range(0, N % 30):
        cards = swap(cards, i)
    print(''.join(cards))

def swap(cards, i):
    n = i % 5
    m = i % 5 + 1
    tmp = cards[n]
    cards[n] = cards[m]
    cards[m] = tmp
    return cards 

main()
