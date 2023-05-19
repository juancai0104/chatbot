# bot.py

from chatterbot import ChatBot
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
            #'default_response': 'Lo siento, pero no te entiendo.',
            #'maximum_similarity_threshold': 0.90
        },
        #'chatterbot.logic.BestMatch'
        ]
)



#trainerGreetings = ChatterBotCorpusTrainer(chatbot)
#trainerGreetings.train("chatterbot.corpus.spanish.greetings")
trainer = ListTrainer(chatbot)
#trainingData = codecs.open('corpus.txt', 'r', "utf-8").read().splitlines()
#trainer.train(trainingData)

def get_feedback():

    text = input()

    if 'Si' in text.lower():
        return True
    elif 'No' in text.lower():
        return False
    else:
        print('Por favor, escriba "Si" or "No"')
        return get_feedback()



"""exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"ChatSalud {chatbot.get_response(query)}")"""