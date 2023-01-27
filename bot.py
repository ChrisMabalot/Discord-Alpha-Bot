import datetime
import discord
import os
import responses

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('BOT_TOKEN')

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mention_or('.'), intents=discord.Intents().all())
    
    async def on_ready(self):
        print(f'{client.user} is now running!')
        print('Syncing commands...')
        synced = await client.tree.sync()
        print(f'{str(len(synced))} commands synced successfully!')

client = Client()

@client.tree.command(name = 'hello', description='Test Hello Command')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(content ='hello')

@client.tree.command(name = 'add', description = 'Add Project Command')
async def add(interaction: discord.Interaction):
    await interaction.response.send_message(content = 'add project test')

@client.tree.command(name = 'embed', description = 'Embed Test')
async def embed(interaction: discord.Interaction, member:discord.Member=None):
    if member == None:
        member = interaction.user

    embed = discord.Embed(title='Test Embed', description = f'This is a test embed written by {member.mention}', color = discord.Color.green(), timestamp = datetime.datetime.utcnow())
    await interaction.response.send_message(embed=embed, ephemeral=True)

client.run(TOKEN)




# async def send_message(message, user_message, is_private):
#     try:
#         response = responses.get_response(user_message)
#         await message.author.send(response) if is_private else await message.channel.send(response)

#     except Exception as e:
#         print(e)

# def run_discord_bot():

#     TOKEN = os.environ.get('BOT_TOKEN')
#     intents = discord.Intents.default()
#     intents.message_content = True

#     client = discord.Client(intents = intents)

#     @client.event
#     async def on_ready():
#         print(f'{client.user} is now running!')

#     @client.event
#     async def on_message(message):
#         if message.author == client.user:
#             return
        
#         username = str(message.author)
#         user_message = str(message.content)
#         channel = str(message.channel)

#         print(f'{username} said: "{user_message}" in {channel}')

#         await send_message(message, user_message, is_private=False)
#     client.run(TOKEN)