"""

Exercise 4:

You were tasked with fixing the following code snippet,
as it leads to a runtime error being raised:

    balance = 350.00
    deposit = input("Please enter the amount you wish to deposit")
    balance += deposit
"""

"""
To fix the code snippet, the float() conversion function should be used (you should side with the
float() function over the int() function as we wish to allow the depositing of Cents as well as Euros).
You can use the function in a couple of different places in the code. In the first example below, the
user input is stored in the variable called deposit, which is currently of type string. The next line of
code converts the data type of deposit to be of type float, with the result stored back in the float
variable. The addition can then be carried out on the two floats:
"""

balance = 350.00
deposit = input("Please enter the amount you wish to deposit")
deposit = float(deposit)
balance += deposit

"""   
A shorter and neater way of writing this would be to use the float() conversion function on the line
of code where we take the user input. In the following example, the string returned from the input
function is immediately converted to a float before being stored in the deposit variable. Again, the
addition can now be carried out without any issues:
"""
balance = 350.00
deposit = float(input("Please enter the amount you wish to deposit"))
balance += deposit
