import telebot

# Create a Telegram bot object
bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# Define a command handler for the /word_count command
@bot.message_handler(commands=["word_count"])
def count_words(message):
    # Get the text of the user's message
    text = message.text

    # Split the text into words
    words = text.split()

    # Count the number of words in the message
    word_count = len(words)

    # Send the word count to the user
    bot.send_message(message.chat.id, f"Your message has {word_count} words.")

# Start polling for Telegram messages
bot.polling()
