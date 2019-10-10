# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def detectLoop(head):
    # Floyd Two Pointer Algorithm (Fast & Slow)
    fast = head.next.next if head.next else None
    slow = head.next
    
    while fast!=slow:
        if fast == None or slow == None:
            return False
            
        fast = fast.next.next if fast.next else None
        slow = slow.next
    return True
