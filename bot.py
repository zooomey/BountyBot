# bot.py
from cgi import test
import os
from dotenv import load_dotenv
import random
import discord


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

client = discord.Client()
   
class commands(discord.Client):
    async def on_message(self, message):
        #don't have the bot respond to itself
        if message.author == self.user:
            return

        if message.content == "!bounty":
            await message.channel.send('bounty has been placed on {}'.format(message.author.mention))



client = commands()

client.run(TOKEN)