# message = input("Tell me something, and I will repat it back to you: ")
# print(message)

# message = input("Please enter your name: ")
# print(message)

#when you have prompts on several lines, do it this way
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nwhat is your first name: "

#storing the prompts inside a variable.
name = input(prompt)
print(f"Hello, {name}")


