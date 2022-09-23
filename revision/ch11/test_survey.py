import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase): 
    """Tests for the class AnonymousSurvey"""
    def setUp(self):
        """create a survey and a set of responses for use in all test methods."""
        question = "what language did you first learn to speak? "
        self.my_suervey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """test that three individual responses are stored properly."""
        question = "what language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()

