from survey import AnonymousSurvey

question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('Enter \033[031mq\033[m at anytime to quit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

print('Thank you to everyone who participated in the survey!')
my_survey.show_results()