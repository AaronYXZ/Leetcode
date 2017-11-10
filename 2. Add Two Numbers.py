'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        ret = ListNode(0)
        cur = ret

        sum = 0
        while True:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next

            cur.val = sum % 10
            sum /= 10
            if l1 != None or l2 != None or sum != 0:
                cur.next = ListNode(0)
                cur = cur.next
            else:
                break

        return ret
