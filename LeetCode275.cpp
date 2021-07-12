# include <vector>
using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        int total = citations.size();
        int l = 0, r = total-1;
        
        if (total==0) {
            return 0;
        }
    
        while (l<=r) {
            // cout << l << " " << r << endl;
            int mid = (l + r) >> 1;
            if (citations[mid] == (total - mid)){
                return citations[mid];
            }
            if (citations[mid] > (total - mid)) {
                r = mid-1;
            }
            else {
                l = mid + 1;
            }
        }

        return total - l ;

    }
};