class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int n = word1.size(), m = word2.size();

        vector<int> suf(m, -1);

        int j = n - 1;
        for (int i = m - 1; i >= 0; i--) {
            while (j >= 0 && word1[j] != word2[i]) j--;
            if (j < 0) break;
            suf[i] = j;
            j--;
        }

        vector<int> ans;
        bool used = false;
        int p = 0;

        for (int i = 0; i < m; i++) {
            while (p < n) {
                if (word1[p] == word2[i]) {
                    ans.push_back(p++);
                    break;
                }

                if (!used &&
                    (i == m - 1 || (suf[i + 1] != -1 && suf[i + 1] > p))) {
                    used = true;
                    ans.push_back(p++);
                    break;
                }

                p++;
            }

            if ((int)ans.size() != i + 1)
                return {};
        }

        return ans;
    }
};