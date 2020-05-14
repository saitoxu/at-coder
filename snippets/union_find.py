# UnionFind
# ref. https://atcoder.jp/contests/atc001/tasks/unionfind_a


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.parents[y] = x
        self.sizes[x] += self.sizes[y]
        self.sizes[y] = self.sizes[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.sizes[self.find(x)]


if __name__ == "__main__":
    uf = UnionFind(5)
    uf.unite(0, 1)
    uf.unite(1, 2)
    uf.unite(3, 4)
    print(uf.is_same(0, 2)) # => True
    print(uf.size(3)) # => 2
