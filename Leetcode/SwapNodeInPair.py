# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result_head=ListNode(0);
        result_head.next=head;
        current=result_head;
        while(current.next):
            next=(current.next).next;
            if(next):
                temp=current.next;
                final=next.next;
                current.next=next;
                next.next=temp;
                temp.next=final;
                current=temp;
            else:
                current=current.next;
        return result_head.next;


            
