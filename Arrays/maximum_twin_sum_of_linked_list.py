class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = next


class Solution:

    def pairSum(self, head):

        values = []

        current = head

        while current:

            values.append(current.val)

            current = current.next

        left = 0

        right = len(values) - 1

        maximum = 0

        while left < right:

            maximum = max(
                maximum,
                values[left] + values[right]
            )

            left += 1

            right -= 1

        return maximum


# Test Code

head = ListNode(
    5,
    ListNode(
        4,
        ListNode(
            2,
            ListNode(1)
        )
    )
)

obj = Solution()

print(
    obj.pairSum(head)
)


# -----------------------------
# Pattern Used:
# Linked List + Two Pointers
#
# Why:
# Need first node and last node
# together, but linked list only
# moves forward.
#
# My thinking:
# 1. Store linked list values
#    in array
# 2. Use two pointers
# 3. Calculate twin sums
# 4. Track maximum sum
# 5. Return answer
#
# Example:
# [5,4,2,1]
#
# 5 + 1 = 6
# 4 + 2 = 6
#
# Maximum = 6
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------