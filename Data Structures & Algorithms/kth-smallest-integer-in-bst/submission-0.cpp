/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
	struct node {
		int val;
		node *next = nullptr; 
	};

    int kthSmallest(TreeNode* root, int k) {
		node* head = new node();
        node* current = head;

        inOrder(root, current);

        node* tmp = head->next;
        for (int i = 0; i < k - 1; i++) {
            tmp = tmp->next;
        }

        int result = tmp->val;
        
        return result;
    }

	void inOrder(TreeNode *root, node* &n) {
		if (root == nullptr) return;

		inOrder(root->left, n);
		
		n->next = new node();
		n = n->next;
		n->val = root->val;

		inOrder(root->right, n);
	}
};
