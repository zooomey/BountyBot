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

#class bounty:
#initialize time as 0
#initialize points as 100

#class hunter:
#hunter only exists if they collect bounty
#initialize hunter and assign bounty score
#remove bountied individual from board

#class passday:
#if time = 30 -> remove from bounty board
#users bounty increases by + 50
#increase all user time by 1

#class board:
#display top 10 highest bounties on users
#if less than 10 users exist, only display what's there

#class leaderboard:
#display top 10 bounty hunters
#
   
class commands(discord.Client):
    async def on_message(self, message):
        #don't have the bot respond to itself
        if message.author == self.user:
            return

        if message.content == "!bounty":
            await message.channel.send('bounty has been placed on {}'.format(message.author.mention))



client = commands()

client.run(TOKEN)