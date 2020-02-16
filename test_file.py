'''---------------------------------------------------------------------------------------------------------------------
This code's purpose is to test the different data structure types

---------------------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------Linked List Test----------------------------------------------------'''
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

'''------------------------------------------Double Linked List Test-------------------------------------------------'''
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

'''------------------------------------------------Stack Test--------------------------------------------------------'''
from StacksAndQueues.StackClass import Stack

print('Stack Example')
stack_item = Stack()

print('\tIs empty: ' + str(stack_item.isEmpty()))

for i in range(0,4):
    print('\tadding: ' + str(i))
    stack_item.push(i)

print('\n')
for i in range(0,5):
    print('\tIs empty: ' + str(stack_item.isEmpty()))
    print('\t' + str(stack_item.peek()))
    stack_item.pop()

print('\n')

'''------------------------------------------------Queues Test--------------------------------------------------------'''
from StacksAndQueues.QueuesClass import Queues

print('Queues Example')
queues_item = Queues()

print('\tIs empty: ' + str(queues_item.isEmpty()))

for i in range(0,4):
    print('\tadding: ' + str(i))
    queues_item.push(i)

print('')
for i in range(0,3):
    print('\tIs empty: ' + str(queues_item.isEmpty()))
    print('\t' + str(queues_item.peek()))
    queues_item.pop()

print('')
for i in range(4,7):
    print('\tadding: ' + str(i))
    queues_item.push(i)

print('')
while(not queues_item.isEmpty()):
    print('\tIs empty: ' + str(queues_item.isEmpty()))
    print('\t' + str(queues_item.peek()))
    queues_item.pop()

print('\n')