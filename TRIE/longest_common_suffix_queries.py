# 3093 Longest commpn suffix queries

class TrieNode:
    def __init__(self):

        self.children = {}

        self.index = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):

        root = TrieNode()

        best_index = 0

        for i in range(len(wordsContainer)):

            if len(wordsContainer[i]) < len(wordsContainer[best_index]):
                best_index = i

        root.index = best_index

        for i, word in enumerate(wordsContainer):

            node = root

            rev = word[::-1]

            for ch in rev:

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if (
                    node.index == -1 or
                    len(wordsContainer[i]) <
                    len(wordsContainer[node.index])
                ):
                    node.index = i

        answer = []

        for word in wordsQuery:

            node = root

            rev = word[::-1]

            for ch in rev:

                if ch not in node.children:
                    break

                node = node.children[ch]

            answer.append(node.index)

        return answer


# Test Code
wordsContainer=["abcd","bcd","xbcd"]
wordsQuery=["cd","bcd","xyz"]

obj=Solution()

answer=obj.stringIndices(
    wordsContainer,
    wordsQuery
)

print(answer)


# -----------------------------
# Pattern Used: Trie
#
# Why:
# Need fast suffix matching.
# Reverse strings converts
# suffix into prefix.
#
# My thinking:
# 1. Reverse all words
# 2. Build trie
# 3. Store best index at nodes
# 4. Reverse query word
# 5. Traverse trie
# 6. Return matched index
#
# Time Complexity: O(total characters)
# --------