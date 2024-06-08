class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = TreeNode(key)
            else:
                self._insert_recursive(root.left, key)
        else:
            if root.right is None:
                root.right = TreeNode(key)
            else:
                self._insert_recursive(root.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.val:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete_recursive(root.right, temp.val)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.val, end=" ")

# Example usage:
bt = BinaryTree()
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    bt.insert(key)

print("Inorder traversal:")
bt.inorder_traversal(bt.root)
print("\nPreorder traversal:")
bt.preorder_traversal(bt.root)
print("\nPostorder traversal:")
bt.postorder_traversal(bt.root)

# Search operation
search_key = 40
if bt.search(search_key):
    print(f"\n{search_key} found in the binary tree.")
else:
    print(f"\n{search_key} not found in the binary tree.")

# Delete operation
delete_key = 30
bt.delete(delete_key)
print(f"\nAfter deleting {delete_key}, Inorder traversal:")
bt.inorder_traversal(bt.root)
