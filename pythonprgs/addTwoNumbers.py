# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = None
        x = None
        temp = 0
        while True:
            
            if not root:
                total = l1.val + l2.val
                answer =  ListNode(total%10)
                root = answer
                temp = 1 if total >= 10 else 0
            else:
                total = l1.val + l2.val
                answer.next =   ListNode( (temp + total)%10)
                temp = 1 if (temp + total) >= 10 else 0
                answer = answer.next
            if not l1.next and l2.next:
                x = l2.next
                break
            elif not l2.next and l1.next:
                x = l1.next
                break
            elif l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
            else:
                break

        print(x, temp)
        while True:
            if x:
                total = x.val + temp
                temp = 1 if total >= 10 else 0
                x.val = total%10
                answer.next =  x
                answer = answer.next
                x = x.next
            else:
                break
        if temp:
            answer.next = ListNode(1)

        return root