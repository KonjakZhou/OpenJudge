# include <vector>
using namespace std;

# define min_int (-2147483648)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_ans = min_int;
        int tmp = min_int;

        for (int i = 0; i < nums.size(); i++) {
            if (tmp < 0 ) {
                tmp = nums[i];
            }
            else {
                tmp += nums[i];
            }
            if (max_ans < tmp) {
                max_ans = tmp;
            }
        }

        return max_ans;
    }
};