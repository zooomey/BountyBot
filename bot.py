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

#class hunter: (!bounty collect <user>)
    #initializes when bounty is collected
    #check hunters.csv to see if user exists as hunter
    #if not:
        #if hunter doesn't already exist, initialize hunter in data and assign bounty score
    #if hunter already exists:
        #add bounty score to hunter's score
    #remove bountied individual from board

#class bounty: (!bounty place <user>)
    #check bounties.csv to see if user already has a bounty on them
    #if yes:
        #return error
    #else:
        #add bountied individual to data
        #initialize bounty amount, time

#class bounty board: (!bounty board)
    #display all active bounties and bounty scores on users. 
    #data taken from bounties.csv
    #all bountied individuals will be removed from board after 30 days

#class hunter leaderboard: (!bounty leaderboard)
    #display top 10 bounty hunters and their scores
    #data sorted from hunters.csv
    #if bounty hunters < 10, only display active bounty hunters. 

#class status (!bounty status <user)
    #check if user is in #bounties.csv
        #if not, return error
    #else:
        #display user name, time on board, current bounty


#class error (!bounty <invalid>)


def hunter():
    pass

def bounty():
    pass

def board():
    pass

def leaderboard():
    pass

def status():
    pass

def error():
    pass

def find(x):
    if x == 'collect':
        return hunter()
    elif x == 'place':
        return bounty()
    elif x == 'board':
        return board()
    elif x == 'leaderboard':
        return leaderboard()
    elif x == 'status':
        return status()
    else: 
        return error()


   
class commands(discord.Client):
    async def on_message(self, message):
        #don't have the bot respond to itself
        if message.author == self.user:
            return

        msg = message.split(" ")
        if msg[0].content == "!bounty":
            find(msg[1])

        else:
            pass

        if message.content == "!bounty":
            await message.channel.send('bounty has been placed on {}'.format(message.author.mention))



client = commands()

client.run(TOKEN)