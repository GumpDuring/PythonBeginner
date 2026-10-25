# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        count = 0
        dummy = ListNode(0)
        curr = dummy
        while True:
            if carry == 0:
                sum1 = l1.val + l2.val
            else:
                sum1 = l1.val + l2.val + carry
                carry = 0
            if len(list(str(sum1))) == 2:
                carry = int(list(str(sum1))[0])
                now = int(list(str(sum1))[1])
            else:
                carry = 0
                now = int(list(str(sum1))[0])
            curr.next = ListNode(now)
            curr = curr.next
            count += 1
            l1 = l1.next
            l2 = l2.next
            if l1 == None and l2 == None:
                return dummy.next
            if l1 == None:
                l1 = 0
            if l2 == None:
                l2 = 0
#Fuck off!!!
