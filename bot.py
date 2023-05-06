# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from cleaner import clean_corpus
from chatterbot.conversation import Statement

CORPUS_FILE = "chat.txt"

chatbot = ChatBot(
        "Chatpot",
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        database_uri = 'postgresql://postgres:0000@localhost/db_chatbot',
        logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Lo siento, Pero no entiendos.',
            'maximum_similarity_threshold': 0.90
        },
        'chatterbot.logic.BestMatch'
        ]
)

#chatbot.storage.drop()

trainerGreetings = ChatterBotCorpusTrainer(chatbot)
trainerGreetings.train("chatterbot.corpus.spanish")
trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

def get_feedback():

    text = input()

    if 'Si' in text.lower():
        return True
    elif 'No' in text.lower():
        return False
    else:
        print('Por favor, escriba "Si" or "No"')
        return get_feedback()



exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"ChatSalud {chatbot.get_response(query)}")