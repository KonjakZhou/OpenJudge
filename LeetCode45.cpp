# include <vector>

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int ans = 0;
        int k = 0;
        int end = 0;
        
        for (int i = 0; i < nums.size()-1; i++) {
            if (i + nums[i] >= k) {
                k = i + nums[i];
                if (k >= nums.size()-1) {
                    return ans + 1;
                }
            }

            if ( i == end ) {
                ans += 1;
                end = k;
            }
            
        }

        return ans;
    }
};