"""
We can reorganize this code by writing two functions, each of which does one 
specific job. Most of the code wont change; were just making it more carefully 
structured. The first function will handle printing the designs, and the second
 will summarize the prints that have been made:
"""

def print_models(unprinted_designs, completed_models): 
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:") 
    for completed_model in completed_models:
        print(completed_model)

