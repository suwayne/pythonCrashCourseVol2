# how its done
# first you import the file - gotta be saved in the same folder as your project
# the filename.function_name
# that's how the magic works
# note > 'pizza' is the module, and 'make_pizza' is the function
# ..means the functions are inside the 'module' :)
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'plenty extra cheese')


# from pizza import make_pizza

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'plenty extra cheese')

# importing with an alias
# from pizza import make_pizza as mp

# mp(8, 'chicken', 'carrots', 'ketchup')
