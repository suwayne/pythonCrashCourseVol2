def __init__(self, question):
    # store a question, and prepare to store responses.
    self.question = question
    self.responses = []


def show_question(self):
    # show survey question.
    print(self.question)


def store_response(self, new_response):
    # store single response to a survey.
    self.responses.append(new_response)


def show_results(self):
    # show all responses that have been given.
    print("survey results:")
    for response in self.responses:
        print(f"- {response}")
