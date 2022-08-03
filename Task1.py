# Python Tasks

#  Version 1: Concatenation

# 1 -define variable name  and assign string
# 2 -reassign variable with your name
# 3 -Use concatenation method
# 4-print welcome message (capitalise first letter and remove whitespaces



name = 'random string' # Assigning variable
firstname = "haider".capitalize()  # using capitalize to make first letter capital
lastname= "abedi".capitalize()
fullname= firstname + " " + lastname # appending two variables together.
print("Welcome"+" " + fullname.strip())  # strip() using this to remove whitepsaces.

# Version 2 - Interpolation Output

full_name = 'random string 2'
first_name = input("first name"+" ")
last_name = input("last name"+" ")
full_name = first_name.capitalize() + " " + last_name.capitalize()
print(f'Hello {full_name}! Welcome')   #using f' interpolate greeting with full name.



