#include <iostream>
using namespace std;

class Solution {
public:
    int tribonacci(int n) {
        int T[3] = {0,1,1};

        if (n<=2) {
            return T[n];
        }

        for (int i = 3; i<=n; i++) {
            int tmp = T[0] + T[1] + T[2];
            T[0] = T[1];
            T[1] = T[2];
            T[2] = tmp;
        }

        return T[2];
    }
};

int main(void){
    Solution solution;

    cout << solution.tribonacci(25) <<endl;
}