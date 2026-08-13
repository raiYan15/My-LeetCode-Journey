class Solution:
    def combine(self, n, k):
        res = []
        self.backtrack(res, [], n, k, 1)
        return res

    def backtrack(self, res, path, n, k, start):
        if len(path) == k:
            res.append(list(path))
            return

        for i in range(start, n + 1):
            path.append(i)
            self.backtrack(res, path, n, k, i + 1)
            path.pop()