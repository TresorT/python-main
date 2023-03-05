"""
You were tasked with creating a series of variables that hold the personal
details in an Electronic Medical Records app.
Sample data is shown below. Your data will likely differ from this drastically,
but each variable should be of the same data type:
"""

first_name = "Geoff"
last_name = "Ackroyd"
age = 45
gender = "M"
weight = 70.00
bmi = 25.00
diagnoses = ['Asthma']
medications = ['Inhaler']
next_of_kin = 'Jill Ackroyd'
has_medical_card = True
contact_number = '0721110099'

print(type(first_name), type(last_name), type(age), type(gender), type(weight), type(bmi),
      type(diagnoses), type(medications), type(next_of_kin), type(has_medical_card),
      type(contact_number), sep="\n")

'''
Please note: In reality, we would not be looking to just type in details like this into our
application, as the application will ideally have an interface that allows a user (medical
professional) to enter these personal details and store them for a particular patient. This
exercise does however get you thinking about what it is you want to be stored in a particular
variable, as you will need to handle the data appropriately.
'''