// Last updated: 28/10/2025, 19:43:31
class Solution {
    int dfs(vector<int>& coins, int a, vector<int>& memo) {
        if (a == 0) return 0;
        if (a < 0)  return -1;
        if (memo[a] != -2) return memo[a];

        int best = 1000000000;                  // “infinito” simple
        for (int c : coins) {
            int sub = dfs(coins, a - c, memo);
            if (sub >= 0 && sub + 1 < best) best = sub + 1;
        }
        return memo[a] = (best == 1000000000 ? -1 : best);
    }
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> memo(amount + 1, -2);      // -2 = desconocido, -1 = imposible
        return dfs(coins, amount, memo);
    }
};