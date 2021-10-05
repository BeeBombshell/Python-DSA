def binary_search_tree(root,key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right,key)

    return search(root.left,key)
