# include <vector>
# include <algorithm>

using namespace std;

class Solution {
public:
    const int mod = 1000000007;

    int bisearch(vector<int> & nums, int target, int l, int r) {
        if ( r - l <= 1) {
            if (target - nums[l] < nums[r] - target) {
                return l;
            }
            return r;
        }

        int mid = (l + r) >> 1;

        if ( nums[mid] == target) {
            return mid;
        }
        
        if ( nums[mid] > target ) {
            return bisearch(nums, target, l, mid);
        }

        return bisearch(nums, target, mid, r);
        
    }

    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        int ans = 0;
        int min_pos2 = -1, min_pos1 = -1;
        int max_diff = 0;
        
        vector<int> nums1_copy(nums1);
        sort(nums1_copy.begin(), nums1_copy.end());
        
        for (int i = 0; i < nums1.size(); i ++ ) {
            int nearest = bisearch(nums1_copy, nums2[i], 0, nums2.size()-1);
            if (max_diff < abs(nums1[i] - nums2[i]) - abs(nums1_copy[nearest] - nums2[i])) {
                max_diff = abs(nums1[i] - nums2[i]) - abs(nums1_copy[nearest] - nums2[i]);
                min_pos2 = i;
                min_pos1 = nearest;
            }
            // cout << nums1[i] << " " << nums2[i] << " " << nums1_copy[nearest] << endl;
        }

        for (int i = 0; i < nums1.size(); i++ ) {
            if ( i == min_pos2) {
                ans = ( ans + abs(nums1_copy[min_pos1] - nums2[i]) ) % mod;
                continue;
            }

            ans = ( ans + abs(nums1[i] - nums2[i]) ) % mod;
        }
        return ans;
        
    }
};