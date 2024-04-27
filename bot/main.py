"""
Discord Bot
"""

import os.path
import os
from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord import Intents
from .hello import Hello

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot = Bot(command_prefix="!", intents=Intents.all())
hello = Hello()

@bot.event
async def on_member_join(member):
    """Runs when a new member joins the Discord"""
    print(f"New Member Joined! Member Info: {member}")

@bot.event
async def on_ready():
    """Run when the bot initially loads"""
    try:
        hello.print_message("Hello World")
    except RuntimeError as err:
        print(err)


def main():
    bot.run(TOKEN)