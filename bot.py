from discord import channel, embeds
#from discord.ext.commands.core import commandm
from main import download_meme
import discord
from discord.ext import commands
from main import *
import os 

client = commands.Bot(command_prefix = '!')
#bot = commands.Bot(command_prefix = '!')
@client.event
async def on_ready():
    print("Bot Ready")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if "!meme" == message.content.lower() :
        file, title = download_meme()
        embed = discord.Embed(title=title)    
        embed.set_image(url=file)
        
        await message.channel.send(embed=embed)
#     elif "!command" in message.content.lower():
#         m = message.content.lower().split(' ')
#         print(m)
#         print(message.author)
#         if len(m) == 1: m.append('porn')
#         print(len(m))
#         if m[1] not in ['command_option_0', 'command_option_1', 'command_option_2', 'command_option_3', 'command_option_4', "command_option_5", "command_option_6", 'command_option_7', 'command_option_8']:
#             await message.channel.send(content="Wrong m type '!command help' to get all ms", file=discord.File('./rick_roll.gif') )
#         elif m[1] != "help":
            
#             url, title = get_hot(m[1])
#             embed = discord.Embed(title=title)
#             embed.set_image(url=url)
#             print("got porn")
#             await message.channel.send(embed=embed)
#         else:
#             await message.channel.send(content="COMMANTS FOR PORN: \n blonde, redhead, boobs, glasses, ass, milf, japanese,")
    elif "!pun" == message.content.lower():
        title, text = get_pun()
        await message.channel.send(content=title + '\n' + "||" + text + "||")

client.run(os.getenv("token"))
