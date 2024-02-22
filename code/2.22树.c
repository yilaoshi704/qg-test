#include <stdio.h>
#include <stdlib.h>

// 定义二叉树的节点
typedef struct TreeNode {
    int value;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

// 创建一个新节点
TreeNode* createNode(int value) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    if (newNode == NULL) {
        exit(-1);
    }
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// 插入操作
TreeNode* insert(TreeNode* root, int value) {
    if (root == NULL) {
        root = createNode(value);
    } else if (value < root->value) {
        root->left = insert(root->left, value);
    } else {
        root->right = insert(root->right, value);
    }
    return root;
}

void display(TreeNode* root){
	if (root != NULL){
		print("%d ", root->value);
		display(root->left);
		display(root->right);
	}
}
