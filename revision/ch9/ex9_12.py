"""
Store the User class in one module, and store the Privileges and Admin classes in a 
separate module. In a separate file, create an Admin instance and call show_privileges() 
to show that everything is still working correctly.
"""

# from user1 import User


# admin1 = User('osasu', 'ogbebor', 'male', 'nigeria', 34)
# admin1.describe_user()
# admin1.greet_user()

from priv_admin import Admin

user1 = Admin('osasu', 'ogbebor', 'male', 'nigeria', 34, ['write', 'edit'])
user1.describe_user()
user1.privileges.show_privileges()