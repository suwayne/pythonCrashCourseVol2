"""
Modified slightly, the function greet_user() can not only tell the user Hello! but also greet them by name. 
For the function to do this, you enter username in the parentheses of the functios definition at def greet_user(). 
By add- ing username here you allow the function to accept any value of username you specify. The function now expects 
you to provide a value for username each time you call it. When you call greet_user(), you can pass it a name, such as 
'jesse', inside the parentheses:
"""
#this example shows how to pass information into a function:
#parameter: piece of information a function needs to do its job
#artument: the string 'jesse' is an argument. A piece of information that's passed from a function "greet user" to call the function "greet user"
def greet_user(username):       #the variable 'usename' is a parameter
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

