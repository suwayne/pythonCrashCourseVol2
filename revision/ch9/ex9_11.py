"""
Start with your work from Exercise 9-8 (page 173). Store the classes User, 
Privileges, and Admin in one module. Create a separate file, make an Admin 
instance, and call show_privileges() to show that everything is working correctly.
"""
from user import User

admin1 = User('osasu', 'ogbebor', 'male', 'nigeria', 34)
admin1.describe_user()

