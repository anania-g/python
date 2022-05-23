# List is a collection of data which can be of any type
# a list is like an array but holds multiple data types
from itertools import count


animals=['bear','tiger','lion','panda','elephant']
print(animals[0])

# prints out the list starting from 1 to the end using a :
# if there is a number after the colon that index is excluded
print(animals[1:])


fruits=['apple', 'orange', 'banana','grapes']
vegetables=['kale', 'broccoli', 'lettuce']


#extend methd used to join lists (a list starts after the last item of a list)
fruits.extend(vegetables)

#append is used to insert a new item at the end of a list
vegetables.append("beans")

#sort is used to arrange in assending(default) or descending order
vegetables.sort()
vegetables.sort(reverse=true)

#count methods used to count the number of occurence
fruits.count('apple')

#index method returns the index of the item in the list
fruits.index('apple')

#adds an item to the list at a specific location(takes two parameters the index and the item to add)
fruits.insert(0, 'tangirine')

# pop method removes the item from the list (can take an index as a parameter)
fruits.pop()

# remove method removes the item from the list ( takes an item as a parameter)
fruits.remove('apple')

# del method is used to delete a list
del (vegetables)

# nested list is a list inside a list or lists are items of a list
fruit=[
    ['apple', 'orange', 'kiwi'],
    ['mangos','coconuts'],
    ['pinapples']
]
print(fruit[1],[1])


#iterate through a nested list
for row in fruit:
    for col in row:
        print(col)


