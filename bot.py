import discord
import os
import responses

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('BOT_TOKEN')
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    print('Syncing commands...')
    synced = await client.tree.sync()
    print(f'{str(len(synced))} commands synced successfully!')

@client.tree.command(name = 'hello', description='Test Hello Command')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(content='hello')
    await client.close()

@client.command()
async def add(ctx):
    await ctx.send("add project test")

@client.command()
async def embed(ctx, member:discord.Member=None):
    if member == None:
        member = ctx.message.author
    
    embed = discord.Embed(title='Test Embed', description = f'This is a test embed written by {member.name}', color = discord.Color.green(), timestamp = ctx.message.created_at)
    await ctx.send(embed=embed)

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