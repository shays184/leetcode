# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # method: id(node) -- UNIQUE for each node
        # data structure:
            # 1. list (append: O(1), is_exist: O(n))
            # 2. set (append: O(1), is_exist: O(1)) -- CHOSEN

        node = head
        if node is None:
            return False
        visited_nodes=set()
        visited_nodes.add(id(node))
       
        while  node.next is not None:
            node = node.next
            node_id = id(node)
            if node_id in visited_nodes:
                return True
            visited_nodes.add(node_id)
        return False
            

           
    

            
