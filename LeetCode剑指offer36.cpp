# include <iostream>

using namespace std;
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};

class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if (root ==  NULL) {
            return root;
        }

        Node * left_head, * right_head, * left_tail, * right_tail;
        int left_head_virtual = false, right_head_virtual = false;

        if (root->left != NULL) {
            left_head = treeToDoublyList(root->left);
        }
        else {
            left_head = new Node(-1);
            left_head->left = left_head;
            left_head->right = left_head;
            left_head_virtual = true;
        }
        left_tail = left_head->left;

        if (root->right != NULL) {
            right_head = treeToDoublyList(root->right);
        }
        else {
            right_head = new Node(-1);
            right_head->left = right_head;
            right_head->right = right_head;
            right_head_virtual = true;
        }
        right_tail = right_head->left;

        root->left = left_tail;
        root->right = right_head;

        left_head->left = right_tail;
        left_tail->right = root;

        right_head->left = root;
        right_tail->right = left_head;

        if (left_head_virtual) {
            root->left = root->left->left;
            root->left->right = root;
            left_head = root;
        }

        if (right_head_virtual) {
            root->right = root->right->right;
            root->right->left = root;
        }
    
        return left_head;
    }
};