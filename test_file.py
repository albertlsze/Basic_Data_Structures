'''---------------------------------------------------------------------------------------------------------------------
This code's purpose is to test the different data structure types

---------------------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------Linked LIst Test----------------------------------------------------'''
from LinkedList.LinkedListClass import ListNode

print('Testing Linked List:')
head = ListNode(0)
tail = head

for i in range(1,5):
    tail.next = ListNode(i)
    tail = tail.next

head_copy = head

for i in range(0,5):
    print('\t Node ' + str(i) + ': ' + str(head_copy.val))
    head_copy = head_copy.next
'''------------------------------------------Double Linked LIst Test-------------------------------------------------'''
from LinkedList.DoubleLinkedListClass import DoubLinkedList

print('Testing Double Linked List:')
head = DoubLinkedList(0)
tail = head

for i in range(1,5):
    tail.next = DoubLinkedList(i)
    tail.next.prev = tail
    tail = tail.next
tail.next = head
tail.next.prev = tail

for i in range(0,5):
    print('\tNode '+ str(i) + ':')
    print('\t\tPrev: '+ str(head.prev.val))
    print('\t\tCurr: ' + str(head.val))
    print('\t\tNext: ' + str(head.next.val))
    print('\n')
    head = head.next



test = ListNode(0)
head = ListNode(1)
head.next = test
test = head
head = ListNode(2)
head.next = test
test = head

print(test.val)
print(test.next.val)
print(test.next.next.val)
