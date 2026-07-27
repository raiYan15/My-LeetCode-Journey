class Solution:
    def maxCoins(self, nums):

        arr = [1] + nums + [1]
        n = len(arr)

        dp = [[0] * n for _ in range(n)]

        # length of interval
        for length in range(1, n - 1):

            # starting index
            for i in range(1, n - length):

                j = i + length - 1

                ans = 0

                # last balloon
                for k in range(i, j + 1):

                    coins = (
                        dp[i][k - 1]
                        + arr[i - 1] * arr[k] * arr[j + 1]
                        + dp[k + 1][j]
                    )

                    ans = max(ans, coins)

                dp[i][j] = ans

        return dp[1][n - 2]