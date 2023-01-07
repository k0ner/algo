class QuickUnionOptimized:

    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def union(self, x, y):

        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.root[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.root[x_root] = y_root
            else:
                self.root[y_root] = x_root
                self.rank[x_root] += 1

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def check(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    ds = QuickUnionOptimized(10)
    ds.union(0, 1)
    ds.union(0, 2)
    ds.union(1, 3)
    ds.union(4, 8)
    ds.union(5, 6)
    ds.union(5, 7)
    ds.union(4, 7)
    ds.union(7, 4)

    print(ds.check(0, 3))
    print(ds.check(1, 5))
    print(ds.check(7, 8))
    print(ds.check(5, 7))
