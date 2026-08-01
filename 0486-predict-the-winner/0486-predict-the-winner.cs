public class Solution
{
    public bool PredictTheWinner(int[] nums)
    {
        int n = nums.Length;
        int[] dp = new int[n];

        for (int i = n - 1; i >= 0; i--)
        {
            dp[i] = nums[i];
            for (int j = i + 1; j < n; j++)
            {
                dp[j] = Math.Max(nums[i] - dp[j], nums[j] - dp[j - 1]);
            }
        }

        return dp[n - 1] >= 0;
    }
}