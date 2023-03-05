"""
Exercise 5

You were tasked with amending the following code snippet so that a whole number with no
decimal places is stored in the temp variable:

temp = 19.9
print('The current temp is', temp, 'degrees')

To amend this code and store just the whole number of 19 in the variable temp, the int()
conversion function should be used.

"""

temp = int(19.9)
print('The current temp is', temp, 'degrees')

"""
Please note that if you attempted to convert the temp variable to an int down in the print function,
this will only convert it for the purposes of printing it out. So the 19.9 is converted to an int ( 19 )
for presentation purposes. No assignment has been made though, so the temp variable will still
hold 19.9 after the print statement has executed:
"""

temp = 19.9
print('The current temp is', int(temp), 'degrees')
print(temp)
