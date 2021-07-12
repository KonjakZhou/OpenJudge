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

        vector<int> rob_this(n-1);
        vector<int> not_rob_this(n-1);

        rob_this[0] = nums[0];
        not_rob_this[0] = 0;

        for (int i = 1; i < n-1; i++) {
            rob_this[i] = not_rob_this[i-1] + nums[i];
            not_rob_this[i] = max(rob_this[i-1], not_rob_this[i-1]);
        }

        int ans1 =  max(rob_this[n-2], not_rob_this[n-2]);

        rob_this[0] = nums[1];
        not_rob_this[0] = 0;

        for (int i = 2; i < n; i++) {
            rob_this[i-1] = not_rob_this[i-2] + nums[i];
            not_rob_this[i-1] = max(rob_this[i-2], not_rob_this[i-2]);
        }

        int ans2 =  max(rob_this[n-2], not_rob_this[n-2]);

        return max(ans1, ans2);
    }
};