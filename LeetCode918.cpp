# include <iostream>
# include <vector>

using namespace std;

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int max_ans = mSum(nums, true);
        int min_ans = mSum(nums, false);

        // cout << max_ans << " " << min_ans << endl;

        int summ = 0;
        for (int i=0; i<nums.size(); i++) {
            summ += nums[i];
        }

        if (summ == min_ans || max_ans > summ - min_ans){
            return max_ans;
        }
        return summ - min_ans;
    }

    int mSum(vector<int> & nums, bool if_max) {
        int cur_max;
        int ans;
        
        if (if_max) {
            cur_max = -2147483648;
            ans = -2147483648;
        }
        else {
            cur_max = 2147483647;
            ans = 2147483647;
        }

        for (int i=0; i<nums.size(); i++) {
            if (cmp(cur_max, 0, if_max) < 0) {
                cur_max = nums[i];
            }
            else {
                cur_max += nums[i];
            }

            if (cmp(ans, cur_max, if_max) < 0) {
                ans = cur_max;
            }
        }

        return ans;
    }

    int cmp(int i, int j, bool if_larger) {
        
        if ( i > j) {
            if (if_larger){
                return 1;
            }
            else {
                return -1;
            }
        }
        else 
        if (i == j) {
            return 0;
        }
        else {
            if (if_larger) {
                return -1;
            }
            else {
                return 1;
            }
            
        }
        
    }
};