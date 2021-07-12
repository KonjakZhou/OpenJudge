# include <iostream>
# include <vector>

using namespace std;

int main(void) {
    vector<int> v1 = {1,2,3,4};
    vector<int> v2(v1.begin(), v1.begin() + 2);
    
    cout << v2.size() << endl;
}