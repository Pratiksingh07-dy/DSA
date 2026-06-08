class TreeNode:

    def __init__(self, val=0):

        self.val = val

        self.left = None

        self.right = None


class Solution:
    def createBinaryTree(self, descriptions):

        nodes = {}

        children = set()

        for parent, child, isLeft in descriptions:

            if parent not in nodes:
                nodes[parent] = TreeNode(parent)

            if child not in nodes:
                nodes[child] = TreeNode(child)

            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            children.add(child)

        for node in nodes:

            if node not in children:
                return nodes[node]


# Test Code

descriptions = [
    [20,15,1],
    [20,17,0],
    [50,20,1],
    [50,80,0],
    [80,19,1]
]

obj = Solution()

root = obj.createBinaryTree(descriptions)

print("Root Value:", root.val)

#2196. Create Binary Tree From Descriptions

# -----------------------------
# Pattern Used: Trees + HashMap
#
# Why:
# Need to connect parent
# and child nodes and find root.
#
# My thinking:
# 1. Create TreeNode for every value
# 2. Store nodes in dictionary
# 3. Connect parent and child
# 4. Store all child nodes
# 5. Node that never appears
#    as child is root
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------c