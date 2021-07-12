# include <vector>

using namespace std;

class Solution {
public:
    int min(int i, int j) {
        if (i<j) {
            return i;
        }
        return j;
    }

    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();

        int ans0 = 0;
        int ans1 = 0;

        for (int i=2; i<n; i++) {
            int tmp = min(ans0 + cost[i-2], ans1 + cost[i-1]);
            ans0 = ans1;
            ans1 = tmp;
        }

        return ans1;
    }
};