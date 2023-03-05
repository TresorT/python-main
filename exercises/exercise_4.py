"""
Exercise 2
You were tasked with determining a value for each of the following 4 data types (int, float, string,
boolean) that is considered both truthy (evaluates to True) and falsy (evaluates to False).
The following four statements evaluate to False:
"""

print(bool(False))
print(bool(0.00))
print(bool(0))
print(bool(""))

"""
The boolean value of False is the only obvious one here, which evaluates to False.
A numeric value equal to zero (so the integer 0 and the floating point value 0.00) evaluate to False.
An empty string is the only string that evaluates to False.
The following four statements evaluate to True:
"""

print(bool(True))
print(bool(0.00001))
print(bool(-1))
print(bool(" "))

"""
The boolean value True is the obvious one here, evaluating to True.
Any numeric value that is not zero evaluates to True.
Any non-empty string evaluates to True. This string only has a space in it, but that is a valid
character and means that the string is not empty.
"""
