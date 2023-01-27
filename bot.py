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
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().all())
    
    async def on_ready(self):
        print(f'{client.user} is now running!')
        print('Syncing commands...')
        synced = await client.tree.sync()
        print(f'{str(len(synced))} commands synced successfully!')

class project_modal(discord.ui.Modal, title = 'Add New Project'):
    project_name = discord.ui.TextInput(label='Project Name')
    website = discord.ui.TextInput(label='Website')
    discord_server = discord.ui.TextInput(label='Discord')
    twitter = discord.ui.TextInput(label='Twitter')
    additional_info = discord.ui.TextInput(label='Additional Info', style=discord.TextStyle.paragraph)

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