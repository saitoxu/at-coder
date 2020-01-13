# ワーシャルフロイド法
# ref. https://qiita.com/okaryo/items/8e6cd73f8a676b7a5d75


# dは隣接行列
def warshall_floyd(d):
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


# inf = float('inf')
# d = [
#     [  0,   1, inf, inf, inf],
#     [  1,   0,   1, inf, inf],
#     [inf,   1,   0,   1, inf],
#     [inf, inf,   1,   0,   1],
#     [inf, inf, inf,   1,   0]
# ]
# warshall_floyd(d)
# print(d)
