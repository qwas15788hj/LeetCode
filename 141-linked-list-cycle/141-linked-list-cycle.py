# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        rabbit = head
        turtle = head

        while rabbit != None and rabbit.next != None:
            rabbit = rabbit.next.next
            turtle = turtle.next
            if rabbit== turtle:
                return True
        return False