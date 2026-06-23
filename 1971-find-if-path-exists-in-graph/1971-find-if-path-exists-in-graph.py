class Solution:
    def validPath(self, n, edges, source, destination):

        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis, st = {source}, [source]

        while st:
            x = st.pop()

            if x == destination:
                return True

            for y in g[x]:
                if y not in vis:
                    vis.add(y)
                    st.append(y)

        return False