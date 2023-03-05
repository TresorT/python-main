"""
Exercise 6

You were tasked with creating a list of watches. The original list can be created as follows:
watches = ['Compass Watch', 'GPS Watch', 'Stun Watch', 'Nerve Gas Watch', 'Inflatable Dingy
Watch', 'Android Watch', 'Lunchtime Alarm Watch(1:30pm)']

"""

watches = ['Compass Watch', 'GPS Watch', 'Stun Watch', 'Nerve Gas Watch', 'Inflatable Dingy Watch', 'Android Watch', 'Lunchtime Alarm Watch(1:30pm)']

# The additional element can be added to the end of the list by using the append method:
watches.append('Jingly Jangly Watch(for the evening ambiance)')

# Removing 'Android Watch' can be done as follows:
watches.remove('Android Watch')

# The following line of code inserts the 'Apple Watch' at the start of the list:
watches.insert(0, 'Apple Watch')

# The following line of code uses indexing to grab the 'Inflatable Dingy Watch' from
# the list and stores it in the variable current_watch
current_watch = watches[4]

# Below is the rations list for the next part of exercise:
rations = ['Mars Bar', 'Powdered Soup', 'Dry Cereal', 'Trifle']

# We can sort the list item alphabetically using the following line of code:
rations.sort()

# You can pull the last item out of the list in either of the following ways:
# 1. You can pass the index number of the last element manually
lunch = rations[3]

# 2. You can pass in -1 as the index number. This is more dynamic, as it will always
# grab the last element from the list even if the list changes
lunch = rations[-1]

# We can grab the first three elements from the rations list using the following
# slicing syntax:
breakfast_of_champions = rations[:3]

"""
No start has been specified, so we start at the beginning of the list. 
A stop of 3 has been specified, but the stop is exclusive. 
This means that we will retrieve elements from the start of the list, 
up to but not including the element at index 3.
"""
