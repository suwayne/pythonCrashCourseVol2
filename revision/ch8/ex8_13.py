"""
Start with a copy of user_profile.py from page 149. Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you.
"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('osasu', 'ogbebor', stateof_origin='edo', carrer='cyber security')
print(user_profile)

