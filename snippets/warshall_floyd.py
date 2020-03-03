# ワーシャルフロイド法
# ref. https://qiita.com/okaryo/items/8e6cd73f8a676b7a5d75


# dは隣接行列
def warshall_floyd(d):
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

if __name__ == "__main__":
    inf = float('inf')
    # こういう無向グラフ: (0)-(1)-(2)-(3)-(4)
    d = [
        [  0,   1, inf, inf, inf],
        [  1,   0,   1, inf, inf],
        [inf,   1,   0,   1, inf],
        [inf, inf,   1,   0,   1],
        [inf, inf, inf,   1,   0]
    ]
    warshall_floyd(d)
    print(d)
    # => [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 1, 0, 1, 2], [3, 2, 1, 0, 1], [4, 3, 2, 1, 0]]
