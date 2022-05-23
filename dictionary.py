# dictionary is a collection of key/value pairs
my_car={
    "brand":"Rangerover",
    "model":"hse",
    "year":2015
}

# creating a dictionary with a constructor
mygreens=dict(fruits="green apples",vegitables="kale")

# to change the value for a key in the dictionary 
my_car["year"]=2019

# get is used to retrieve the value for a key in the dictionary
my_car.get("year")

# to add a new key/value pair to the dictionary
my_car.update({"color":"green"})


# to get all the keys in the dictionary
a=my_car.keys()

# to get all the values in the dictionary
b=my_car.values()

# pop method is used to remove a key and its value
my_car.pop(color)

# to empty the dictionary
my_car.clear()

# to delete the dictionary
del(my_car)
