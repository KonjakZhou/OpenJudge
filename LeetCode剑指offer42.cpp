#include <vector>
using namespace std;


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> ans(nums.size());
        ans[0] = nums[0];
        int max_ans = ans[0];
        
        for (int i=1; i<nums.size(); i++) {
            if (ans[i-1] + nums[i] > nums[i]) {
                ans[i] = ans[i-1] + nums[i];
            }
            else {
                ans[i] = nums[i];
            }
            
            if (max_ans < ans[i]) {
                max_ans = ans[i];
            }
        }

        return max_ans;      
        
    }
};