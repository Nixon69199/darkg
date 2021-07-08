import discord
from discord import colour
from discord.ext import commands

client = commands.Bot(command_prefix = "+")

@client.event
async def on_ready():
    print("bot is ready ")

@client.command()
async def hello(ctx):
    await ctx.send("HI !")

client.run('ODYyNzE4MTE5NTY2NTA4MDUy.YOca3A._yjO5pHHJR6PzrmcEYmvxhqbbCE')