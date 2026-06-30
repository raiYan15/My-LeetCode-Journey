class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        int left = 0, ans = 0;
        vector<int> cnt(3, 0);

        for (int right = 0; right < n; right++) {
            cnt[s[right] - 'a']++;

            while (cnt[0] > 0 && cnt[1] > 0 && cnt[2] > 0) {
                ans += n - right;
                cnt[s[left] - 'a']--;
                left++;
            }
        }

        return ans;
    }
};