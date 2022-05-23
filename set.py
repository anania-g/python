# set is a collection of values which are not ordered or indexed



fruits={"grapes","apples","berries"}

for x in fruits:
    print(x)


# create a set using a set constructor
# set keyword is used if not it creates a tuple
animals=set(("lion","tiger","bear"))


# add method is to add an item to a set
fruits.add('oranges')

# update method is used add multiple items to a set
fruits.update(['mango','kiwi'])

# remove is to remove an item from a set
fruits.remove('mango')

# clear method is used to clear all elements in a set
fruits.clear()

# del is to delete the set itself
del(fruits)
