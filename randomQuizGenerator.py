#! python3
# randomQuizGenerator.py - Creates quizzes w/ questions and answers in 
# random order, along with the answer key.

import random
import os
import capitals_data

# The quiz data. Keys are states and values are their capitals.
if not os.path.isdir('quizes'): os.mkdir('quizes')
if not os.path.isdir('answers'): os.mkdir('answers')

capitals = capitals_data.capitals

for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    num = quizNum + 1
    quizFile = open('quizes/capitalsquiz%s.txt' % (num), 'w')
    answerKeyFile = open('answers/capitalsquiz_ansers%s.txt' % (num), 'w')

    # Write out common header 
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (num))
    quizFile.write('\n\n')
        
    states = []
    for capital in capitals:
       states.append(capital['state'])
    random.shuffle(capitals)

    for questionNum in range(50):
        correctAnswer = capitals[questionNum]['city']
        wrongAnswers = []
        for capital in capitals: 
           wrongAnswers.append(capital['city'])
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]

        random.shuffle(answerOptions)

        quizFile.write('%s. What\'s the capital of %s?\n' % (questionNum + 1, capitals[questionNum]['state']))

        for i in range(4):
           quizFile.write('   %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        
        quizFile.write('\n')

        # Write answer to answer key files
        answerKeyFile.write('%s => %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()

        

