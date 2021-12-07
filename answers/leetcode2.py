from typing import List, Optional
from math import floor

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """ You are given two non-empty linked lists representing two 
    non-negative integers. The digits are stored in reverse order, and
    each of their nodes contains a single digit. Add the two numbers 
    and return the sum as a linked list.
    
    You may assume the two numbers do not contain any leading zero,
    except the number 0 itself.
    
    === Constraints ===
    - The number of nodes in each linked list is in the range [1, 100]
    - 0 <= Node.val <= 9
    - It is guaranteed that the list represents a number that does not
      have leading zeros
    
    Params
        l1(Optional[ListNode]): [description]
        l2(Optional[ListNode]): [description]
    Return
        Optional[ListNode]: [description]
    """
    first_sum = l1.val + l2.val
    extra = 0
    if first_sum > 9:
        extra = int(str(first_sum)[0])
        first_sum = int(str(first_sum)[1])
    working_node = ListNode()
    final_node = ListNode(first_sum, working_node)
    while l1.next is not None and l2.next is not None:
        l1, l2 = l1.next, l2.next
        sum = l1.val + l2.val + extra
        if sum > 9:
            extra = int(str(sum)[0])
            sum = int(str(sum)[1])
        else:
            extra = 0
        working_node.val = sum
        new_node = ListNode()   # This line causes an extra redundent node
        working_node.next = new_node
        working_node = new_node
    return final_node
        
        
def print_nodes(l):
    num = ''
    while l.next is not None:
        num = str(l.val) + num
        l = l.next
    num = str(l.val) + num
    print(num)
    
if __name__ == '__main__':
    l1_3 = ListNode(3)
    l1_2 = ListNode(4, l1_3)
    l1_1 = ListNode(2, l1_2)
    l2_3 = ListNode(4)
    l2_2 = ListNode(6, l2_3)
    l2_1 = ListNode(5, l2_2)
    print_nodes(add_two_numbers(l1_1, l2_1))