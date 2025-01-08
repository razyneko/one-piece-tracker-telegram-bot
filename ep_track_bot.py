import telebot
import json
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

api_token = os.getenv("API_TOKEN")
channel_id = os.getenv("CHANNEL_ID")

# instantiate the bot
bot = telebot.TeleBot(api_token)

# Check if episodes.json exists, and create it with default data if not
if not os.path.exists('episodes.json') or os.stat('episodes.json').st_size == 0:
    # initialising current_episode as 1st episode
    episode_data = {'current_episode': 1}
    # dumping episode_data to episodes.json
    with open('episodes.json', 'w') as file:
        json.dump(episode_data, file, indent=4)
else:
    # Load episode data from the existing file
    # reading from episodes.json
    with open('episodes.json', 'r') as file:
        episode_data = json.load(file)

# save_episode_data() saves episode_data to episodes.json
def save_episode_data():
    with open('episodes.json', 'w') as file:
        json.dump(episode_data,file)

# handler for setting current episode
@bot.message_handler(commands=['set_ep'])
def set_ep(message):
    try:
        # retrieving episode entered by user
        episode = int(message.text.split()[1])
        # setting entered episode as current
        episode_data['current_episode'] = episode
        # updating episodes.json
        save_episode_data()
        # reply to user
        bot.reply_to(message, f"Current episode set to {episode}")
    except (IndexError, ValueError):
        bot.reply_to(message, "Usage: /set_ep <episode_number>")

# handler for setting next episode as current
@bot.message_handler(commands=['next'])
def next_episode(message):
    episode_data['current_episode'] += 1
    save_episode_data()
    episode = episode_data['current_episode']
    link = f"https://t.me/c/{channel_id[4:]}/{episode + 6}"
    bot.reply_to(message, f"Next Episode: {episode}\n[Watch Now]({link})", parse_mode="Markdown")

# handler for getting current episode 
@bot.message_handler(commands=['current'])
def current_episode(message):
    episode = episode_data['current_episode']
    link = f"https://t.me/c/{channel_id[4:]}/{episode + 6}"
    bot.reply_to(message, f"Current Episode: {episode}\n[Watch Now]({link})", parse_mode="Markdown")

# Catch-all handler for unrecognized inputs
@bot.message_handler(func=lambda message: True)  # This handles any text message
def handle_invalid_commands(message):
    bot.reply_to(
        message,
        "Sorry, I didn't understand that command. Please use one of the following:\n"
        "/set_ep <episode_number> - Set the current episode\n"
        "/next - Go to the next episode\n"
        "/current - Get the current episode"
    )
    
print("Bot is running...")
bot.polling()
print("Bot has stopped.")
