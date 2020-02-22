'''---------------------------------------------------------------------------------------------------------------------
This code's purpose is to test the different data structure types

---------------------------------------------------------------------------------------------------------------------'''
'''----------------------------------------------StringBuilder-------------------------------------------------------'''
from ArraysandStrings.StringBuilder import StringBuilder

print('StringBuilder Example')
string_list = ['This ', 'is ','a ','test.\n']
sentence = StringBuilder(string_list)
print(sentence)

'''------------------------------------------Double Linked List Test-------------------------------------------------'''
from ArraysandStrings.ArrayList import ArrayList
letters = ['a','b','c','d','e','f','g','h','i','j']
print('ArrayList Example')

size = 10
arrayListExample = ArrayList()

for i in range(0,size):
    arrayListExample.append(letters[i])

print('Array Length: ' + str(arrayListExample.len()))

for i in range(0,size):
    print('index ' + str(i) + ': ' + str(arrayListExample.GetItem(i)))


