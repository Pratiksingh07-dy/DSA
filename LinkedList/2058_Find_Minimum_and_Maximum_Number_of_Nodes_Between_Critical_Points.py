class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        min_distance = float('inf')

        while curr and curr.next:
            # Check if curr is a local maximum or minimum
            is_max = curr.val > prev.val and curr.val > curr.next.val
            is_min = curr.val < prev.val and curr.val < curr.next.val

            if is_max or is_min:
                # First critical point
                if first == -1:
                    first = index

                # Distance from previous critical point
                if last != -1:
                    min_distance = min(min_distance, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        # Fewer than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        # Distance between first and last critical points
        max_distance = last - first

        return [min_distance, max_distance]