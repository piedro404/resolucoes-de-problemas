# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def linked_list_to_str(node):
            num = ""
            while node:
                num += str(node.val)
                node = node.next
            return num
        
        def str_to_linked_list(num):
            if num == "":
                return ListNode(0)
            head = None
            for x in num:
                new_node = ListNode(x)
                new_node.next = head
                head = new_node
            return head
        
        num1 = int(linked_list_to_str(l1)[::-1])
        num2 = int(linked_list_to_str(l2)[::-1])

        result = str(num1 + num2)

        return str_to_linked_list(result)

main = Solution()
def int_to_linked_list(num):
    if num == 0:
        return ListNode(0)
    head = None
    while num > 0:
        num, digit = divmod(num, 10)
        new_node = ListNode(digit)
        new_node.next = head
        head = new_node
    return head

def printLinkedList(node):
    p = ""
    if(node != None):
        p += printLinkedList(node.next)
        return str(node.val) + p

    return ""

l1 = int_to_linked_list(243)
l2 = int_to_linked_list(564)

print(printLinkedList(main.addTwoNumbers(l1, l2)))