# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    vector<int> ans;
    
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        if (k==0) {
            vector<int> ans(0);
            return ans;
        }
        quickSearch(arr, k, 0, arr.size()-1);
        vector<int> ans(arr.begin(), arr.begin()+k);
        return ans;
    }

    void quickSearch(vector<int>& arr, int k, int l, int r) {
        // cout << l << " " << r << endl;
        int j = l;
        for (int i = l+1; i <= r; i++) {
            if (arr[i] < arr[l]) {
                j++ ;
                int t = arr[j];
                arr[j] = arr[i];
                arr[i] = t;
            }
        }

        int t = arr[j];
        arr[j] = arr[l];
        arr[l] = t;

        if (k == j+1) {
            return ;
        }
        if (k < j+1 ) {
            quickSearch(arr, k, l, j);
            return ;
        }
        if (k > j+1) {
            quickSearch(arr, k, j+1, r);
            return ;
        }
    }
};
int main(void) {
    vector<int> arr = {3,2,1};
    int k = 2;
    Solution solution;
    vector<int> ans = solution.getLeastNumbers(arr, k);
    
    for (int i = 0; i<ans.size(); i++) {
        cout << ans[i];
    }
    cout << endl;
}