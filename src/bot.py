'''
  _ )  |               __|  |                  |  _ \             
  _ \  |  |  |   -_)  (     |   _ \  |  |   _` |  |  |  -_) \ \ / 
 ___/ _| \_,_| \___| \___| _| \___/ \_,_| \__,_| ___/ \___|  \_/  
'''              

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="wl!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(">> Bot is Online <<")

@bot.event
async def on_member_join(member):
    channel = bot.guild.system_channel

    await channel.send(f"{member.mention} Joined {member.guild.name}")

@bot.event
async def on_member_remove(member):
    channel = bot.guild.system_channel

    await channel.send(f"{member.mention} Leaved {member.guild.name}")

bot.run("ABCDEFG") #Place you Token Here!!!!!!!!!!!!