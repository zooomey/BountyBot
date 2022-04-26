# bot.py
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import json


from pkg_resources import parse_version


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='&', intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

################

def add_score(member: discord.Member, amount: int):
    if os.path.isfile("file.json"):
        with open("file.json", "r") as fp:
            data = json.load(fp)
        try:
            data[f"{member.id}"]["score"] += amount
        except KeyError:
            data[f"{member.id}"] = {"score": amount} 
    else:
        data = {f"{member.id}": {"score": amount}}
    with open("file.json", "w+") as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


def add_loss(member: discord.Member, amount: int):
    if os.path.isfile("loss.json"):
        with open("loss.json", "r") as fp:
            data = json.load(fp)
        try:
            data[f"{member.id}"]["loss"] += amount
        except KeyError:
            data[f"{member.id}"] = {"loss": amount} 
    else:
        data = {f"{member.id}": {"loss": amount}}
    with open("loss.json", "w+") as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


def get_score(member: discord.Member):
    with open("file.json", "r") as fp:
        data = json.load(fp)
    return data[f"{member.id}"]["score"]

def get_loss(member: discord.Member):
    with open("loss.json", "r") as fp:
        data = json.load(fp)
    return data[f"{member.id}"]["loss"]

################

@bot.command()
async def bounty(ctx, arg: discord.Member):
    person = ctx.author.mention
    add_score(ctx.author, 1)
    add_loss(arg, 1)
    await ctx.send('Bounty has collected for {} by {}!'.format(arg, ctx.author.name))

@bot.command()
async def fry(ctx, members: commands.Greedy[discord.Member]):
    person = ", ".join(x.name for x in members)
    add_score(ctx.author, 10)
    await ctx.send('Bounty has collected for Daddy Fry by {}!'.format(ctx.author))

@bot.command()
async def info(ctx):
    await ctx.send('**Bounty Hunter Commands**: \n\n&bounty - collect a bounty on an individual\n&leader - display hunter leaderboard\n&lowest - display most hunted individuals')

################

async def get_win_data():
    with open("file.json", "r") as f:
        users = json.load(f)
    return users

@bot.command()
async def leader(ctx):
    embed = discord.Embed(title=f"Bounty Leaderboard", colour=discord.Colour.purple())
    embed.add_field(name="Top Hunters", value=f"\n".join([f"{await bot.fetch_user(member[0])}: {member[1]['score']} snipes" for member in sorted((await get_win_data()).items(), key=lambda x: x[1]['score'], reverse=True)]))
    await ctx.send(embed=embed)

async def get_loss_data():
    with open("loss.json", "r") as f:
        users = json.load(f)
    return users

@bot.command()
async def loss(ctx):
    embed = discord.Embed(title=f"Bounty Loserboard", colour=discord.Colour.purple())
    embed.add_field(name="Most Hunted Users", value=f"\n".join([f"{await bot.fetch_user(member[0])}: {member[1]['loss']} losses" for member in sorted((await get_loss_data()).items(), key=lambda x: x[1]['loss'], reverse=True)]))
    await ctx.send(embed=embed)


bot.run(TOKEN)
