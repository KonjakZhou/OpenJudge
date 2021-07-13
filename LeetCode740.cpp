# include <vector>
# include <algorithm>

using namespace std;

class Solution {
public:

    int deleteAndEarn(vector<int>& nums) {
        int n = nums.size();
        
        int max_num = 0;
        for (int i = 0; i < n; i++) {
            if ( max_num < nums[i]) {
                max_num = nums[i];
            }
        }
        // cout << max_num << endl;

        int bucket[max_num + 1];
        int ans[max_num + 1];
        memset(bucket, 0, (max_num+1) * sizeof(int));
        memset(ans, 0, (max_num+1) * sizeof(int));
        
        for (int i = 0; i < n; i++) {
            bucket[nums[i]] ++ ;    
        }
        // for (int i = 0; i <= max_num; i++) {
        //     cout << bucket[i] << " ";
        // }
        ans[0] = 0;
        ans[1] = bucket[1];
        for (int i = 2; i <= max_num; i++) {
            ans[i] = max(ans[i-1], ans[i-2] + i * bucket[i]);
            // cout << ans[i] << " ";
        }
        return ans[max_num];
    }
};