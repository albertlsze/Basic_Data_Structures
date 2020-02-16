from LinkedList.LinkedListClass import ListNode

class Stack():
    def __init__(self):
        self.stack = ListNode(None)

    def isEmpty(self):
        if self.stack.val is not None:
            return False
        else:
            return True

    def push(self,data):
        head = ListNode(data)
        head.next = self.stack
        self.stack = head

    def pop(self):
        if self.stack.val is not None:
            self.stack = self.stack.next

    def peek(self):
        if self.stack.val is not None:
            return self.stack.val
        else:
            return 'None'

