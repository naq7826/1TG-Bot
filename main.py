import discord
import os
import asyncio
from data.strings import *
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

client = discord.Client()
client = commands.Bot(command_prefix='x!')

with open("data/filtered-words.txt") as file:
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(activity=discord.Game('made by Quanimus'))

flag = 0

@client.event
async def on_message(message):
	if message.author.id == 797491259793997854 and flag == 1:
		message_content = message.content.strip().lower()
		if any(bad_word in message.content.lower() for bad_word in bad_words):
			embed=discord.Embed(title=announceTitle, description=NO_MORE_CK, color=0xff5252)
			await message.channel.send(embed=embed)
			await message.delete()
	await client.process_commands(message)

@client.command()
async def filter(ctx, text):
	global flag
	if discord.utils.get(ctx.message.author.roles, name="ADMIN") is None:
		if flag == 1:
			await ctx.send(filterCmdNotAdmin1)
		if flag == 0:
			await ctx.send(filterCmdNotAdmin0)
	else:
		if text == "on":
			flag = 1
			await ctx.send(filterOn)
			
		if text == "off":
			flag = 0
			await ctx.send(filterOff)

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