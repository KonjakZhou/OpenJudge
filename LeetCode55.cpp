# include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        if (n==1) {
            return true;
        }

        vector<int> d(n);
        if (nums[0] == 0) {
            return false;
        }

        d[0] ++ ;
        if (nums[0] + 1 < n){
            d[nums[0] + 1] --;
        }
        
        for (int i = 1; i < n; i++) {

            d[i] = d[i] + d[i-1];
            if (d[i] <= 0) {
                return false;
            }

            if (nums[i] == 0){
                continue;
            }

            d[i] ++ ;
            if (i + nums[i] + 1 < n)
                d[i+nums[i]+1] -- ;
        }

        return true;
    }
};