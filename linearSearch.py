# Unordered linear search

mylist = [5, 87, 2, 100, -1, 22, 4000, 34, 23, 19, 567]
myterm = 5


def search(unordered_list, term):
    unordered_list_size = len(unordered_list)
    for i in range(unordered_list_size):
        if term == unordered_list[i]:
            print('Index of search item = ' + ' ' + str(i))
            print('Number you searched for = ' + ' ' + str(mylist[i]))

            return False

search(mylist, myterm)
