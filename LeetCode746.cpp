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
        vector<int> ans(n);

        ans[0] = cost[0];
        cost[1] = cost[]
    }
};