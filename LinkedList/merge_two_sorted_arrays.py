class ListNode:

    def __init__(
        self,
        val=0,
        next=None
    ):

        self.val = val

        self.next = next


class Solution:

    def mergeTwoLists(
        self,
        list1,
        list2
    ):

        dummy = ListNode()

        current = dummy

        while (

            list1

            and

            list2

        ):

            if (

                list1.val

                <=

                list2.val

            ):

                current.next = list1

                list1 = list1.next

            else:

                current.next = list2

                list2 = list2.next

            current = current.next

        if list1:

            current.next = list1

        else:

            current.next = list2

        return dummy.next


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


list1 = createLinkedList(

    [1,2,4]

)

list2 = createLinkedList(

    [1,3,4]

)

obj = Solution()

result = obj.mergeTwoLists(

    list1,

    list2

)

printLinkedList(result)

# Output:
# 1 1 2 3 4 4