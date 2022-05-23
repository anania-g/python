


g= 'hello world.'


#length of the string
print(len(g))

#the index/position of the string
print(g.index("world"))

# to convert the first character to capital letter
print(g.capitalize())

# convert all the text into upper case
print(g.upper())

# check to see if all the characters are in lower case(true/false)
print(g.isLower())

# check to see if all the characters are in upper case(false/true)
print(g.isupper())

# checks the position of the parameter and the index
print(g.find("world"))

#used to count the occurence of a parameter
print(g.count("w"))

#used to split a string into a python list
print(g.split())

# \n :-used to separate a string into separete line 
print('show me\n d money')

#used to add strings together
print(g+"hope u r k")

#used to replace characters or string..takes 2 parameters the str to replace and str to replace with
print(g.replace("world","people"))



# f-string is an expression that is evaluated at runtime and formatted
name="anania"
age="20"
f'hello, {name}. you are {age} years old.'