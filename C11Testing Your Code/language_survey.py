from survey import AnnonymousSurvey

# define a question
question = "What language did you first learn to speak? "
my_survey = AnnonymousSurvey(question)

# show the questions, and store responses to the questions.
my_survey.show_question()
print("Enter 'q' at any time to quit. \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
