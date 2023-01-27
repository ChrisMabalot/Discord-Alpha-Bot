import discord
import os
import responses

from dotenv import load_dotenv

load_dotenv()

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = os.environ.get('BOT_TOKEN')
    client = discord.client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    client.run(TOKEN)