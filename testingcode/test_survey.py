import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ teste para a classe AnonymousSurvey """
    def test_store_single_response(self):
        """ testar que uma resposta apenas é guardada corretamente"""
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    
    def test_store_three_responses(self):
        """" teste para três respostas """
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Portuguese']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()