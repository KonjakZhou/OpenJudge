#include <iostream>

using namespace std;

class Solution {
public:
    int ans[31] = {0, 1};
    int fib(int n) {
        for (int i=2; i<=n; i++) {
            ans[i] = ans[i-1] + ans[i-2] ; 
        }

        return ans[n];
    }
};

int main(void){
    Solution solution;
    cout << solution.fib(5) << endl;
}