# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hola",
    "Hola Amigo"
])
trainer.train([
    "¿Eres una planta?",
    "No, soy un bot"
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"ChatSalud {chatbot.get_response(query)}")