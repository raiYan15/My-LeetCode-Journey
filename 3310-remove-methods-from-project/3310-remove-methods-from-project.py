from collections import defaultdict
class Solution:
    def remainingMethods(self, n, k, invocations):
        g = defaultdict(list)
        u = defaultdict(list)
        for a, b in invocations:
            g[a].append(b)
            u[a].append(b)
            u[b].append(a)
        bad = [False] * n
        def dfs(x):
            bad[x] = True
            for y in g[x]:
                if not bad[y]:
                    dfs(y)
        dfs(k)
        vis = [False] * n
        def dfs2(x):
            vis[x] = True
            bad[x] = False
            for y in u[x]:
                if not vis[y]:
                    dfs2(y)
        for i in range(n):
            if not bad[i] and not vis[i]:
                dfs2(i)
        ans = []
        for i in range(n):
            if not bad[i]:
                ans.append(i)
        return ans