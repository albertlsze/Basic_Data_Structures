from TreesAndGraphs.Trie import Trie

test = Trie()
addwords=['at','and','an','add']

print('Add words: ')
for word in addwords:
    print('\t'+word)
    test.addWord(word)

print('\nsearch: a')
print('exist: ' + str(test.search('a')))

print('\nsearch: .at')
print('exist: ' + str(test.search('.at')))

print('\nAdd words: ')
print('\tbat\n')
test.addWord('bat')

searchword = [".at","an.","a.d.","b.","a.d","."]
for word in searchword:
    print('search: '+word)
    print('exist: ' + str(test.search(word)))