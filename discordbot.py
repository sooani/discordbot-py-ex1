from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author.client: return None
    await client.process_commands(message)
    
    if message.author == client.user:
        return
    
    if message.cotent == '@everyone':
        await messge.channel.send('벨튀당!')

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')
        
@client.command()
async def f'{PREFIX}안녕(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention}메로,하이메로', reference=ctx.message)

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
