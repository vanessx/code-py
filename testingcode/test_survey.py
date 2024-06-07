import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ teste para a classe AnonymousSurvey """
    def setUp(self):
        """criar um inquérito e um conjunto de respostas para
        usar em todos os testes de métodos"""
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Portuguese']

    def test_store_single_response(self):
        """ testar que uma resposta apenas é guardada corretamente"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """" teste para três respostas """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()