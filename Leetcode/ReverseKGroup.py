# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
from collections import deque
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        result_head=ListNode(0);
        result_head.next=head;
        current=result_head;
        pre=current;
        current=current.next;
        stack=deque();
        while(current):
            stack.append(current);
            current=current.next;
            if(len(stack)==k):
                stack.reverse();
                while(stack):
                    pre.next=stack.popleft();
                    pre=pre.next;
                pre.next=current;
        return result_head.next;
        