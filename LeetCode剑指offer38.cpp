# include <vector>
# include <set>
# include <string>

using namespace std;

class Solution {
public:
    int total;
    vector<string> permutation(string s) {
        set<string> result;
        string ans = ""; 
        vector<bool> flag(s.size(), false);
        dfs(flag, s, 0, result, ans);
        
        vector<string> results(result.begin(), result.end());

        return results;
    }

    void dfs(vector<bool> & flag, string & s, int k, set<string> & result, string & ans) {
        
        if (flag.size() == k) {
            string ans_tmp(ans);
            result.insert(ans_tmp);
            return ;
        }

        for (int i = 0; i < s.size(); i++) {
            if (not flag[i]) {
                flag[i] = true;
                ans.push_back(s[i]);
                dfs(flag, s, k+1, result, ans);
                ans.pop_back();
                flag[i] = false;
            }
        }
    }

};