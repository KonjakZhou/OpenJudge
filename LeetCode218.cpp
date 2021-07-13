# include <vector>
# include <map>
# include <cmath>
# include <set>
# include <algorithm>
# include <iostream>

using namespace std;

struct treeNode
{
    int data = 0 ;
    int left = 0 ;
    int right = 0 ;
};

class Solution {
public:
    void build(vector<treeNode> & tree, int x, int l, int r) {
        tree[x].left = l;
        tree[x].right = r;
        tree[x].data = 0;

        if (l==r) {
            return ;
        }

        int mid = (l+r) >> 1;
        build(tree, x*2, l, mid);
        build(tree, x*2+1, mid+1, r);

        return ;
    }

    void modify(vector<treeNode> & tree, int x, int l, int r, int value) {
        if (tree[x].left == l && tree[x].right == r){
            tree[x].data = max(tree[x].data, value);
            return ;
        }

        int mid = (tree[x].left + tree[x].right) >> 1;

        tree[x*2].data = max(tree[x*2].data, tree[x].data);
        tree[x*2+1].data = max(tree[x*2+1].data, tree[x].data);
        tree[x].data = 0;

        if ( l > mid) {
            modify(tree, x*2+1, l,r, value);
            return ;
        }
        if (r <= mid) {
            modify(tree, x*2, l, r, value);
            return ;
        }
        modify(tree, x*2, l, mid, value);
        modify(tree, x*2+1, mid+1, r, value);
        
        return ;
    }

    int query(vector<treeNode> & tree, int x, int pos) {
        if (tree[x].left == tree[x].right) {
            return tree[x].data;
        }

        int mid = (tree[x].left + tree[x].right) >>1;
        tree[x*2].data = max(tree[x*2].data, tree[x].data);
        tree[x*2+1].data = max(tree[x*2+1].data, tree[x].data);
        tree[x].data = 0;

        if (pos > mid) {
            return query(tree, x*2+1, pos);
        }
        else {
            return query(tree, x*2, pos);
        }
    }

    vector< vector<int> > getSkyline(vector< vector<int> >& buildings) {
        set<long long> coordinates_set;
        map<long long, int> coordinate2id_set;

        for (int k = 0 ; k < buildings.size(); k++) {
            coordinates_set.insert((long long)buildings[k][0] << 1);
            coordinates_set.insert((long long)buildings[k][1] << 1);
        }    

        vector<long long> coordinates(coordinates_set.begin(), coordinates_set.end());

        for (int i=0; i<coordinates.size(); i++) {
            coordinates_set.insert(coordinates[i]-1);
            coordinates_set.insert(coordinates[i]+1);
        }

        coordinates.assign(coordinates_set.begin(), coordinates_set.end());

        for (int i=0; i<coordinates.size(); i++) {
            coordinate2id_set[coordinates[i]] = i;
        }

        int treeLenth = (int)pow(2, (int)(log(coordinates.size()) / log(2)) + 2);
        vector<treeNode> tree(treeLenth + 1 );
        build(tree, 1, 0, coordinates_set.size());
        
        for (int k = 0; k<buildings.size(); k++) {
            modify(tree, 1, coordinate2id_set[(long long)buildings[k][0] << 1], coordinate2id_set[(long long)buildings[k][1] << 1], buildings[k][2]);
        }
        
        int heights[coordinates.size()];
        vector< vector<int> > ans;
        
        for (int k = 0; k < coordinates.size(); k++ ){
            heights[k] = query(tree, 1, k);    
            // cout << coordinates[k] << " "  << heights[k] << endl;
        }

        int k = 0;
        for (; k < coordinates.size() && heights[k] == 0; k++ ) {}

        // vector<int> tmp({coordinates[k], heights[k]});
        int last = heights[k];
        ans.push_back({(int)(coordinates[k] >> 1), heights[k]});

        for (; k < coordinates.size(); k++) {
            if (heights[k] > last) {
                ans.push_back({(int)(coordinates[k] >> 1), heights[k]});
            }
            if ( heights[k] < last) {
                ans.push_back({(int)((coordinates[k]-1) >> 1), heights[k]});
            }

            last = heights[k];
        }

        return ans;
    }
};



int main(void) {
    vector< vector<int> > buildings({{2,9,10},{3,7,15},{5,12,12},{15,20,10},{19,24,8}});
    Solution solution;
    vector< vector<int> > ans = solution.getSkyline(buildings);

    for (int i=0; i<ans.size(); i++) {
        for (int j=0; j<ans[i].size(); j++) {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
}