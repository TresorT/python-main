"""
Exercise 3:
You were tasked with modifying the following code snippet so that it does not lead to a runtime
error:
    savings = 1050
    print("You have €" + savings + " in the bank!")
"""

"""
Solution 1:
You can use the str() conversion function to convert the integer value of 1050 to a string.
Concatenation can then be performed:
"""
savings = 1050
print("You have €" + str(savings) + " in the bank!")

"""
Solution 2:
You can individually pass an arbitrary number of comma-separated arguments to the print function.
These arguments do not need to be of the same type:
"""

print("You have €", savings, " in the bank!")

"""
You may have noticed that when you pass multiple arguments to the print function, they are
printed separated by a single space by default. You can change the default behaviour by setting the
sep parameter (short for separator) to an empty string as follows:
"""
print("You have €" + str(savings) + " in the bank!", sep="")

