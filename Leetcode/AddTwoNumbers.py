# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        head=ListNode(0)
        end=head
        while((l1!=None) and (l2 !=None)):
            total=carry+l1.val+l2.val
            carry=total/10
            total=total%10
            end.next=ListNode(total)
            end=end.next
            l1=l1.next
            l2=l2.next
        if(l1==None):
            while(l2!=None):
                total=carry+l2.val
                carry=total/10
                total=total%10
                end.next=ListNode(total)
                end=end.next
                l2=l2.next
            if(carry):
                end.next=ListNode(carry)
                end=end.next
            return head.next
        else:
            while(l1!=None):
                total=carry+l1.val
                carry=total/10
                total=total%10
                end.next=ListNode(total)
                end=end.next
                l1=l1.next
            if(carry):
                end.next=ListNode(carry)
                end=end.next
            return head.next



