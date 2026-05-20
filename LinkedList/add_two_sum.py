class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        current = dummy

        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)

            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


# Helper function to create linked list
def createList(arr):

    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# Helper function to print linked list
def printList(head):

    while head:
        print(head.val, end=" ")
        head = head.next


# Test Code
l1 = createList([2,5,3])
l2 = createList([5,6,4])

obj = Solution()

answer = obj.addTwoNumbers(l1, l2)

print("Result:")
printList(answer)


# -----------------------------
# Pattern Used: Linked List
#
# Why:
# Need to add digits one by one while caring carry
#
# My thinking:
# 1. Traverse both linked lists
# 2. Add digits + carry
# 3. Create new node
# 4. Update carry
# 5. Return final linked list
#
# -----------------------------