import unittest
from survey import AnnonymousSurvey


class TestAnnonymousSurvey(unittest.TestCase):
    # test for the class AnnonymousSurvey
    def test_store_single_response(self):
        # test that a single response is stored properly.
        question = "what language did you first learn to speak? "
        my_survey = AnnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        # test that 3 individual responses are stored properly
        question = "What language did you first learn to speak? "
        my_survey = AnnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
