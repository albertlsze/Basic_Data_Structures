from LinkedList.LinkedListClass import ListNode

class Queues():
    def __init__(self):
        self.head = ListNode(None)
        self.tail = self.head

    def isEmpty(self):
        if self.head.val is not None:
            return False
        else:
            return True

    def push(self,data):
        if self.head.val is None:
            self.tail.val = data
        else:
            self.tail.next = ListNode(data)
            self.tail = self.tail.next

    def pop(self):
        if self.head.next is not None:
            self.head = self.head.next
        else:
            self.head.val = None

    def peek(self):
        if self.head.val is not None:
            return self.head.val
        else:
            return 'None'

