#include <bits/stdc++.h>

using namespace std;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            } else {
                Node* cur;
                if(data <= root->data) {
                    cur = insert(root->left, data);
                    root->left = cur;
                } else {
                    cur = insert(root->right, data);
                    root->right = cur;
               }

               return root;
           }
        }

/*The tree node has data, left child and right child
class Node {
    int data;
    Node* left;
    Node* right;
};

*/

    Node *lca(Node *root, int v1,int v2) {
		    // Write your code here.
        if(root->right != NULL && root->left != NULL){
            if( (root->right->data == v1 && root->left->data == v2) ||
                (root->right->data == v2 && root->left->data == v1) ){
                  return root;
            }else{
                if( v1 > root->data && v2 > root->data ){
                    return lca(root->right, v1, v2);
                }else{
                    if( v1 < root->data && v2 < root->data ){
                        return lca(root->left, v1, v2);
                    }else{
                        return root;
                    }
                }
            }
        }else{
            if(root->right != NULL){
                if( root->data == min(v1,v2) && root->right->data == max(v1, v2) ){
                    return root;
                }else{
                    return lca(root->right, v1, v2);
                }
            }else{
                if( root->data == max(v1,v2) && root->left->data == min(v1, v2) ){
                    return root;
                }else{
                    return lca(root->left, v1, v2);
                }
            }
        }
    }

}; //End of Solution

int main() {

    Solution myTree;
    Node* root = NULL;

    int t;
    int data;

    std::cin >> t;

    while(t-- > 0) {
        std::cin >> data;
        root = myTree.insert(root, data);
    }

  	int v1, v2;
  	std::cin >> v1 >> v2;

    Node *ans = myTree.lca(root, v1, v2);

  	std::cout << ans->data;

    return 0;
}
