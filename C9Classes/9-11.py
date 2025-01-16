import user_98
osasu = user_98.Admin('osasumwen', 'ogbebor', 32, 'April 2020')

osasu.describe_user()

osasu_privileges = [
    'post',
    'delete',
    'copy'
]

osasu.privileges.privileges = osasu_privileges
print(f"The admin {osasu.first_name} has these privileges:")
osasu.privileges.show_privileges()
