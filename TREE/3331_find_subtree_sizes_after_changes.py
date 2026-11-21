from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for node in range(1, n):
            children[parent[node]].append(node)

        last_seen = [-1] * 26
        new_parent = [-1] * n

        stack = [(0, True, -1)]

        while stack:
            node, entering, previous = stack.pop()
            char = ord(s[node]) - ord('a')

            if entering:
                previous = last_seen[char]

                if previous != -1:
                    new_parent[node] = previous
                else:
                    new_parent[node] = parent[node]

                last_seen[char] = node

                stack.append((node, False, previous))

                for child in reversed(children[node]):
                    stack.append((child, True, -1))

            else:
                last_seen[char] = previous

        new_children = [[] for _ in range(n)]

        for node in range(1, n):
            new_children[new_parent[node]].append(node)

        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        answer = [1] * n

        for node in reversed(order):
            if new_parent[node] != -1:
                answer[new_parent[node]] += answer[node]

        return answer