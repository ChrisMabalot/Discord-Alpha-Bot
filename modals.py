import discord

class project_modal(discord.ui.Modal, title = 'Add New Project'):
    project_name = discord.ui.TextInput(label='Project Name')
    website = discord.ui.TextInput(label='Website')
    discord_server = discord.ui.TextInput(label='Discord')
    twitter = discord.ui.TextInput(label='Twitter')
    additional_info = discord.ui.TextInput(label='Additional Info', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{project_modal}', ephemeral=True)