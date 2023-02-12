import datetime
import discord
import os

from discord import ui
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

class ProjectModal(ui.Modal, title = 'New Project'):
    project_name = ui.TextInput(label='Project Name', style=discord.TextStyle.short)
    website = ui.TextInput(label='Website', style=discord.TextStyle.short, required=False)
    discord_server = ui.TextInput(label='Discord', style=discord.TextStyle.short, required=False)
    twitter = ui.TextInput(label='Twitter', style=discord.TextStyle.short, required=False)
    additional_info = ui.TextInput(label='Additional Info', style=discord.TextStyle.paragraph, required=False)

    async def on_submit(self, interaction: discord.Interaction, member:discord.Member=None):
        if member == None:
            member = interaction.user

        embed = discord.Embed(title=f'{self.project_name}', description=f'Website: {self.website}\nDiscord: {self.discord_server}\nTwitter: {self.twitter}\n\nAdditional Info: {self.additional_info}', color = discord.Color.red(), timestamp = datetime.datetime.utcnow())
        await interaction.response.send_message(embed=embed)

client = Client()

@client.tree.command(name = 'add', description = 'Add a new project to the channel.')
async def add(interaction: discord.Interaction):
    await interaction.response.send_modal(ProjectModal())

client.run(TOKEN)