# For a grouped list of tree exercises, view: 
# https://leetcode.com/discuss/study-guide/1337373/Tree-question-pattern-oror2021-placement

# Get depth of a node in a binary tree
def get_depth(root, node):
        stack = [(root,0)]
        while stack:
            cur, depth = stack.pop()
            if cur == node: return depth
            if cur.left: stack.append((cur.left, depth+1))
            if cur.right: stack.append((cur.right, depth+1))
        return -1  # Node not found

# Returns max depth of a binary tree
# NOTE: Depth of root is 1
def max_depth(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    if root.left == None:
        return 1+(root.right)
    if root.right == None:
        return 1+max_depth(root.left)
    return 1+max(max_depth(root.left), max_depth(root.right))

