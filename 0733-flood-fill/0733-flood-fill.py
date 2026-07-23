class Solution:
    def floodFill(self, image, sr, sc, color):

        row = len(image)
        col = len(image[0])

        old = image[sr][sc]

        if old == color:
            return image

        direction = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(x, y):

            image[x][y] = color

            for dx, dy in direction:

                new_x = x + dx
                new_y = y + dy

                if (0 <= new_x < row and
                    0 <= new_y < col and
                    image[new_x][new_y] == old):

                    dfs(new_x, new_y)

        dfs(sr, sc)

        return image