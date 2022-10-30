# subprocess.run([ which('scrapy'), "crawl", "skypebot", "-a", "url={url_store}"])
# This example requires the 'members' and 'message_content' privileged intents to function.

import json
import os
import sys

import discord
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.all()
# intents.messages=True
# intents.message_content=True

TOKEN = config['token']
PREFIX = config['prefix']
print(PREFIX)

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)
# client = discord.Client()
banned_words = [
    "cc", "blahh", "blahhh"
]


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):

    msg = message.content
    id = message.channel.id
    channel = bot.get_channel(id)
    print(msg, "=======msg")
    if message.author == bot.user or message.author.bot:
        return
    if any(word in msg.lower() for word in banned_words):
        await message.channel.purge(limit=1)
        await channel.send('thang mat day')
    
    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    await ctx.send("hello cc")

@bot.command()
async def pong(ctx):
    await ctx.send("ping")


@bot.command()
async def poll(ctx, *, question):
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```{question} \n✅ = Yes\n❎ = No```")
    await message.add_reaction('❎')
    await message.add_reaction('✅')

bot.run(TOKEN)
