# include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }

        int ans = 0;
        TreeNode * stack[10001];
        int depth[10001];
        int top = 0;
        int max_depth = 0;
        
        stack[0] = root;
        depth[0] = 1;

        while (top >= 0){
            int cur_depth = depth[top];
            TreeNode * ptr = stack[top];
            top -- ;

            if (ptr->right != NULL) {
                top += 1;
                stack[top] = ptr->right;
                depth[top] = cur_depth + 1;
            }

            if (ptr->left != NULL) {
                top += 1;
                stack[top] = ptr->left;
                depth[top] = cur_depth + 1;
            }

            if (max_depth < cur_depth){
                max_depth = cur_depth;
            }
        }
        
        return max_depth;
    }
};