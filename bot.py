# bot.py

from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import codecs

chatbot = ChatBot(
        "Alicia",
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        database_uri = 'postgresql://postgres:0000@localhost/db_chatbot',
        logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Todavía no estoy tan entrenado para poder responder a esta pregunta',
            'maximum_similarity_threshold': 0.65
        },
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.BestMatch'
        ]
)



#trainerGreetings = ChatterBotCorpusTrainer(chatbot)
#trainerGreetings.train("chatterbot.corpus.spanish.greetings")
#trainer = ListTrainer(chatbot)
#trainingData = codecs.open('corpus.txt', 'r', "utf-8").read().splitlines()
#trainer.train(trainingData)


"""def get_feedback(pregunta, respuestaCorrecta):
    
    correct_response = Statement(respuestaCorrecta)
    chatbot.learn_response(correct_response, pregunta)
    return "Respuesta añadida a la base de datos de Alicia"""

def get_feedback():

    text = input()

    if 'si' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Por favor, escriba "Si" o "No"')
        return get_feedback()



print('Por favor, haz una regunta')



"""exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"ChatSalud {chatbot.get_response(query)}")
        print('\n Is "{}" a coherent response to "{}"? \n'.format(
            chatbot.get_response(query).text,
            query
        ))
        if get_feedback() is False:
            print('please input the correct one: ')
            correct_response = text=input()
            chatbot.learn_response(correct_response, query)
            print('Responses added to bot!')"""

while True:
    try:
        input_statement = Statement(text=input())
        response = chatbot.get_response(
            input_statement
        )

        print('\n ¿Es "{}" una respuesta coherente a "{}"? \n'.format(
            response.text,
            input_statement.text
        ))
        if get_feedback() is False:
            print('Por favor, escriba la correcta: ')
            correct_response = Statement(text=input())
            chatbot.learn_response(correct_response, input_statement)
            print('Respuesta añadida a la base de datos de Alicia')

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break