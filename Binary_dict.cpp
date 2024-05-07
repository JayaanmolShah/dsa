#include <iostream>
#include <string>
using namespace std;

class TreeNode {
public:
    string keyword;
    string meaning;
    TreeNode* left;
    TreeNode* right;

    TreeNode(string key, string value) : keyword(key), meaning(value), left(NULL), right(NULL) {}
};

class Dictionary {
private:
    TreeNode* root;

    void insert(TreeNode*& node, string key, string value) {
        if (node == NULL) {
            node = new TreeNode(key, value);
        } else if (key < node->keyword) {
            insert(node->left, key, value);
        } else if (key > node->keyword) {
            insert(node->right, key, value);
        } else {
            // Handle duplicate keys
            node->meaning = value;
        }
    }

    TreeNode* search(TreeNode* node, string key, int& comparisons) {
        comparisons++;
        if (node == NULL || node->keyword == key) {
            return node;
        }

        if (key < node->keyword) {
            return search(node->left, key, comparisons);
        } else {
            return search(node->right, key, comparisons);
        }
    }

    TreeNode* findMin(TreeNode* node) {
        while (node->left != NULL) {
            node = node->left;
        }
        return node;
    }

    TreeNode* remove(TreeNode*& node, string key) {
        if (node == NULL) {
            return NULL;
        }

        if (key < node->keyword) {
            node->left = remove(node->left, key);
        } else if (key > node->keyword) {
            node->right = remove(node->right, key);
        } else {
            // Node with only one child or no child
            if (node->left == NULL) {
                TreeNode* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == NULL) {
                TreeNode* temp = node->left;
                delete node;
                return temp;
            }

            // Node with two children: Get the inorder successor (smallest in the right subtree)
            TreeNode* temp = findMin(node->right);

            // Copy the inorder successor's content to this node
            node->keyword = temp->keyword;
            node->meaning = temp->meaning;

            // Delete the inorder successor
            node->right = remove(node->right, temp->keyword);
        }
        return node;
    }

    void displayInOrder(TreeNode* node) {
        if (node == NULL) {
            return;
        }
        displayInOrder(node->left);
        cout << "Keyword: " << node->keyword << ", Meaning: " << node->meaning << endl;
        displayInOrder(node->right);
    }

public:
    Dictionary() : root(NULL) {}

    void add(string key, string value) {
        insert(root, key, value);
    }

    void display() {
        if (root == NULL) {
            cout << "Dictionary is empty." << endl;
            return;
        }
        displayInOrder(root);
    }

    bool search(string key) {
        int comparisons = 0;
        TreeNode* result = search(root, key, comparisons);
        if (result == NULL) {
            cout << "Keyword not found." << endl;
            return false;
        } else {
            cout << "Keyword found. Number of comparisons: " << comparisons << endl;
            cout << "Meaning: " << result->meaning << endl;
            return true;
        }
    }

    void update(string key, string newValue) {
        int comparisons = 0;
        TreeNode* result = search(root, key, comparisons);
        if (result != NULL) {
            result->meaning = newValue;
            cout << "Meaning updated successfully." << endl;
        } else {
            cout << "Keyword not found." << endl;
        }
    }

    void remove(string key) {
        root = remove(root, key);
    }
};

int main() {
    Dictionary dict;
    int choice;
    string key, value;

    do {
        cout << "\nMenu\n1. Add a keyword\n2. Display all keywords\n3. Search for a keyword\n4. Update meaning\n5. Remove a keyword\n6. Exit\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter keyword: ";
                cin >> key;
                cout << "Enter meaning: ";
                cin >> value;
                dict.add(key, value);
                break;
            case 2:
                dict.display();
                break;
            case 3:
                cout << "Enter keyword to search: ";
                cin >> key;
                dict.search(key);
                break;
            case 4:
                cout << "Enter keyword to update: ";
                cin >> key;
                cout << "Enter new meaning: ";
                cin >> value;
                dict.update(key, value);
                break;
            case 5:
                cout << "Enter keyword to remove: ";
                cin >> key;
                dict.remove(key);
                break;
            case 6:
                cout << "Exiting program." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 6);

    return 0;
}