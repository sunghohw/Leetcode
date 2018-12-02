# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1l2 = l1.val + l2.val
        if l1.next == None and l2.next == None:
            if l1l2 >= 10:
                temp = ListNode(l1l2 % 10)
                temp.next = ListNode(1)
                return temp
            else:
                return ListNode(l1l2)
        elif l1.next == None:
            if l1l2 >= 10:
                temp = ListNode(l1l2 % 10)
                temp.next = self.addTwoNumbers(ListNode(1),l2.next)
                return temp
            else:
                temp = ListNode(l1l2 % 10)
                temp.next = self.addTwoNumbers(ListNode(0),l2.next)
                return temp
        elif l2.next == None:
            if l1l2 >= 10:
                temp = ListNode(l1l2 % 10)
                temp.next = self.addTwoNumbers(l1.next,ListNode(1))
                return temp
            else:
                temp = ListNode(l1l2 % 10)
                temp.next = self.addTwoNumbers(l1.next,ListNode(0))
                return temp
        else:
            if l1l2 >= 10:
                temp = ListNode(l1l2 % 10)
                tempNext = l1.next
                tempNext.val += 1
                try:
                    temp.next = self.addTwoNumbers(tempNext,l2.next)
                except:
                    print "exception in else"
                return temp
            else:
                temp = ListNode(l1l2)
                temp.next = self.addTwoNumbers(l1.next,l2.next)
                return temp
            
            