# include <iostream>
# include <vector>

using namespace std;

int main(void) {
    vector<int> v1(10);
    
    for (int i; i<v1.size(); i++)
        cout << v1[i] << endl;
}