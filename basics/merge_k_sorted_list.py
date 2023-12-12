import heapq

"""
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def mergeKLists(lists):
        min_heap = []
        header = ListNode()
        cur = header
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        return header.next


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6, ListNode(7, ListNode(9))))
    lists = [list1, list2, list3]

    solution = Solution()

    merged = solution.mergeKLists(lists)
    cur = merged
    while cur:
        print(cur.val)
        cur = cur.next