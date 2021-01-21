import discord
import os
import asyncio
from data.strings import *
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

client = discord.Client()
client = commands.Bot(command_prefix='x!')

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(activity=discord.Game('made by Quanimus'))
    

@client.command()
async def share(ctx, usr="", pw="", rank0="", rank1="", rank2=""):
	if usr == "" or pw == "" or rank0 == "":
		await ctx.send(missingArgs, delete_after=3)
		await ctx.message.delete()
		return
	rank = [rank0, rank1, rank2]
	embed = discord.Embed(title=shareTitle, description=shareDesc, color=0xff5252)
	embed.add_field(name="Username", value=usr, inline=True)
	embed.add_field(name="Password", value=pw, inline=True)
	embed.add_field(name="Rank", value=" ".join(rank), inline=True)
	channel = client.get_channel(799916376537038888)
	await channel.send(embed=embed)
	await ctx.message.delete()

@client.command()
async def announce(ctx, mess):
  embed = discord.Embed(title=announceTitle, description=mess, color=0xff5252)
  await ctx.send(embed=embed)
  await ctx.message.delete()

client.run(os.getenv('TOKEN'))