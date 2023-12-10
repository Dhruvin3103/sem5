from bintrees import RBTree, BPlusTree

# Example of B-tree using RBTree
b_tree = RBTree()

# Insert keys into the B-tree
keys_b_tree = [5, 3, 7, 2, 4, 6, 8]
for key in keys_b_tree:
    b_tree.insert(key, key)

# Print the keys in sorted order
print("B Tree keys:", list(b_tree.keys()))

# Example of B+ tree using BPlusTree
bplus_tree = BPlusTree()

# Insert keys into the B+ tree
keys_bplus_tree = [3, 7, 1, 5, 10, 8, 6, 2, 4, 9]
for key in keys_bplus_tree:
    bplus_tree.insert(key, key)

# Print the keys in sorted order
print("B+ Tree keys:", list(bplus_tree.keys()))
