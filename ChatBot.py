import nltk

from nltk.chat.chatbot import Chatbot

# Create a chatbot named Bard
chatbot = Chatbot('Botify')

# Load the training data
training_data = nltk.corpus.chat.corpus

# Train the chatbot
chatbot.train(training_data)

# Start the chatbot
while True:
    user_input = input('Enter your message: ')
    response = chatbot.get_response(user_input)
    print(response)
