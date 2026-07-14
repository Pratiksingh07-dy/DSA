class ListNode:

    def __init__(
        self,
        val=0,
        next=None
    ):

        self.val = val

        self.next = next


class Solution:

    def rotateRight(
        self,
        head,
        k
    ):

        if (

            not head

            or

            not head.next

            or

            k == 0

        ):

            return head

        # Find length

        length = 1

        tail = head

        while tail.next:

            tail = tail.next

            length += 1

        # Remove extra rotations

        k %= length

        if k == 0:

            return head

        # Make circular list

        tail.next = head

        # Find new tail

        steps = length - k - 1

        newTail = head

        for _ in range(steps):

            newTail = newTail.next

        # New head

        newHead = newTail.next

        # Break circle

        newTail.next = None

        return newHead


def createLinkedList(arr):

    dummy = ListNode()

    current = dummy

    for num in arr:

        current.next = ListNode(num)

        current = current.next

    return dummy.next


def printLinkedList(head):

    while head:

        print(

            head.val,

            end=" "

        )

        head = head.next

    print()


head = createLinkedList(

    [1,2,3,4,5]

)

k = 2

obj = Solution()

result = obj.rotateRight(

    head,

    k

)

printLinkedList(result)

# Output:
# 4 5 1 2 3