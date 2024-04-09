import random
import discord

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == client.user:
        return

    # Log messages from a specific channel
    if message.channel.id == CHANNEL_ID:
        print(f"Message from {message.author}: {message.content}")
