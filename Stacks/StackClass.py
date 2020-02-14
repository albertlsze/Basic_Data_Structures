from LinkedList.LinkedListClass import ListNode

class Stack:
    def __init__(self,):
        self = ListNode(None)

    def isEmpty(self):
        if self.val:
            return False
        else:
            return True

    def push(self,data):
        head = ListNode(data)
        head.next = self
        self = head

    def pop(self):
        if self.next:
            self = self.next

    def peek(self):
        return self.val
