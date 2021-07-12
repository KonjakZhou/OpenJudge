# include <vector>
using namespace std;

class Solution {
public:
    int max(int i, int j) {
        if (i>j) {
            return i ;
        }
        return j ;
    }

    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n==1) {
            return nums[0];
        }

        vector<int> rob_this(n);
        vector<int> not_rob_this(n);

        rob_this[0] = nums[0];
        not_rob_this[0] = 0;

        for (int i = 1; i < n; i++) {
            rob_this[i] = not_rob_this[i-1] + nums[i];
            not_rob_this[i] = max(rob_this[i-1], not_rob_this[i-1]);
        }

        return max(rob_this[n-1], not_rob_this[n-1]);
    }
};