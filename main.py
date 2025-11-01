import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")  # Replit secret later

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Example slash command for test
@bot.tree.command(name="ping", description="Ping test")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

bot.run(TOKEN)
