"""
Exercise 7
You were tasked with writing two expressions that successfully check whether:
a) A gamer has unlocked a new mission
b) A gamer has unlocked a new weapon
You were given the following sample data to work with:

"""
hurdle_time = 9.95
height_from_road = 10.75

"""
The following criteria was given for the silly side games:
a) Hyper Hurdles should be completed in 10 seconds or under
b) The Car in We Have Lift-off should rise off the ground by more than 11 centimetres
If both criteria are met, a new mission is unlocked. 
The following statement will check if both criteria has been met:
"""
unlock_mission = hurdle_time <= 10 and height_from_road > 11

# If either criteria are met, a new weapon is unlocked.
# The following statement will check if either of the criteria has been met:

unlock_weapon = hurdle_time <= 10 or height_from_road > 11
