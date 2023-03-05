"""
Solutions – Operations using Data Types and Operators
Exercise 1
Problem 1: message = "He said "There are some who call me... Tim""

The above error can be fixed in one of two ways:
"""
# Solution 1:
message = "He said \"There are some who call me... Tim\""

"""
Here we have used the backslashes just in front of each of the double quotes in the string. The
backslash escapes the special meaning of those characters, meaning that they are treated as
standard quotes and not as string delimiters.
"""

# Solution 2:
message = 'He said "There are some who call me... Tim"'

"""
Here we have just switched the outer quotes (the string delimiters) to single quotes. It is perfectly
fine then to have double quotes within the string.
"""

"""
Problem 2: message = 'He's not the messiah-he's a very naughty boy!'
"""

"""
Again, this error can be fixed in one of two ways:
Solution 1:
"""

message = 'He\'s not the messiah-he\'s a very naughty boy!'

"""
Here we have used the backslashes just in front of each of the single quotes/apostrophes in the
string. The backslash escapes the special meaning of those characters, meaning that they are
treated as apostrophes and not as string delimiters.
"""

# Solution 2:
message = "He's not the messiah-he's a very naughty boy!"

"""
Here we have just switched the outer quotes (the string delimiters) to double quotes. It is perfectly
fine then to have single quotes within the string.
"""

"""
Please note: It is recommended that you avoid using the backslash where possible, as it does hurt
readability. If you can solve the string delimiter issue by just switching the outer quotes, then that is
the best plan. If both apostrophes and speech marks reside inside your string though, then it will
not be possible just to switch the outer quotes and you will need to use the backslash.
"""