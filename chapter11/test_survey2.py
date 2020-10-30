import unittest
from survey import AnnonymousSurvey


class TestAnnonymousSurvey(unittest.TestCase):
    # test for the class AnnonymousSurvey

    def setUp(self):
        # create a survey and a set of responses for use in all test methods.
        question = "What language did you first learn to speak? "
        self.my_survey = AnnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        # test that 3 individual responses are stored properly.
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
