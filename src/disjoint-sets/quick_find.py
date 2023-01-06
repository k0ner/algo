class QuickFind:

    def __init__(self, n):
        self._array = [i for i in range(n)]

    def union(self, x, y):

        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            for i in range(len(self._array)):
                if self._array[i] == y_root:
                    self._array[i] = x_root

    def find(self, x):
        return self._array[x]

    def check(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    ds = QuickFind(10)
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
