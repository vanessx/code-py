class AnonymousSurvey:
    """coletar respostas anónimas num inquérito"""
    def __init__(self, question):
        """guardar as perguntas e guardar as respostas que virão"""
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print('Survey results:')
        for response in self.responses:
            print(f'- {response}')