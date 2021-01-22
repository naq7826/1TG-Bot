import discord
import os
import asyncio
from data.strings import *
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')


#Variables
client = discord.Client()
client = commands.Bot(command_prefix='!!')
flagTroll = 0
flag = 0
bad_words = []
bad_words_troll = []

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(activity=discord.Game('made by Quanimus'))

@client.event
async def on_message(message):
	if message.author.id == 797491259793997854 and flagTroll == 1:  
		message_content = message.content.lower().split()
		message_joined = "".join(message_content)
		for bad_word_troll in bad_words_troll:
			if bad_word_troll in message_joined :
				await message.delete()
				embed=discord.Embed(title=announceTitle, description=NO_MORE_CK, color=0xff5252)
				embed.set_footer(text=footerCredit)
				await message.channel.send(embed=embed)
				break
	if flag == 1:
		message_content = message.content.lower().split()
		for bad_word in bad_words:
			if bad_word in message_content and "delete" not in message_content:
				await message.delete()
				embed=discord.Embed(title=warningTitle, description=warningDesc.format(message.author.mention), color=0xff5252)
				embed.set_footer(text=footerCredit)
				await message.channel.send(embed=embed)
				break
	await client.process_commands(message)
	

@client.command()
async def filterTroll(ctx, cmd="", word=""):
	global flagTroll
	global bad_words_troll
	await ctx.message.delete()
	if cmd == "":
		await ctx.send(missingArgs, delete_after=3)
	if discord.utils.get(ctx.message.author.roles, name="ADMIN") is None:
		if flagTroll == 1:
			await ctx.send(filterCmdNotAdmin1, delete_after=3)
		if flagTroll == 0:
			await ctx.send(filterCmdNotAdmin0, delete_after=3)
	else:
		if cmd == "on":
			flagTroll = 1
			with open("data/filteredTroll-words.txt", encoding="utf-8") as file:
				bad_words_troll = [bad_word_troll.strip().lower() for bad_word_troll in file.readlines()[1:]]
			await ctx.send(filterTrollOn, delete_after=3)
		elif cmd == "off":
			flagTroll = 0
			await ctx.send(filterTrollOff, delete_after=3)
		elif cmd == "add":
			if word == "":
				await ctx.send(missingArgs, delete_after=3)
			if flagTroll == 0:
				await ctx.send(turnOnFirst, delete_after=3)
			else:
				bad_words_troll.append(word)
				openFile = open("data/filteredTroll-words.txt", mode="a", encoding="utf-8")
				openFile.write("\n{}".format(word))
				await ctx.send('Đã chặn từ "{}**"'.format(word[0]), delete_after=3)
		elif cmd == "delete":
			if word == "":
				await ctx.send(missingArgs, delete_after=3)
			elif flagTroll == 0:
				await ctx.send(turnOnFirst, delete_after=3)
			else:
				if word in bad_words_troll:
					bad_words_troll.remove(word)
					openFile = open("data/filteredTroll-words.txt", mode="a", encoding="utf-8")
					openFile.truncate(0)
					for bad in bad_words_troll:
						openFile.write("\n{}".format(bad))
					await ctx.send('Đã xoá từ "{}**"'.format(word[0]), delete_after=3)
				else:
					await ctx.send(deleteNone, delete_after=3)
		elif cmd == "help":
			embed = discord.Embed(title=filterTitle, description=filterDesc, color=0xff5252)
			embed.add_field(name="on/off", value=on_offVal, inline=True)
			embed.add_field(name="add/delete <abc>", value=add_delVal, inline=True)
			embed.add_field(name='throw <ID>', value=throwVal, inline=True)
			embed.set_footer(text=footerCredit)
			await ctx.send(embed=embed)	
		elif cmd == "throw":
			sentChannel = client.get_channel(ctx.message.channel.id)
			msg = await sentChannel.history().find(lambda m: m.id == int(word))
			if msg is None:
				await ctx.send(throwWrongID, delete_after=3) 
			else:
				await msg.delete()
				embed=discord.Embed(title=warningTitle, description=warningDesc.format(msg.author.mention), color=0xff5252)
				embed.set_footer(text=footerCredit)
				await ctx.channel.send(embed=embed)
		else:
			await ctx.send(RECHECK_ARGS, delete_after=3)

@client.command()
async def filter(ctx, cmd="", word=""):
	global flag
	global bad_words
	await ctx.message.delete()
	if cmd == "":
		await ctx.send(missingArgs, delete_after=3)
	if discord.utils.get(ctx.message.author.roles, name="ADMIN") is None:
		await ctx.send(filterCmdNotAdmin0)
	else:
		if cmd == "on":
			flag = 1
			with open("data/filtered-words.txt", encoding="utf-8") as file:
				bad_words = [bad_word.strip().lower() for bad_word in file.readlines()[1:]]
			await ctx.send(filterOn, delete_after=3)
		elif cmd == "off":
			flag = 0
			await ctx.send(filterOff, delete_after=3)
		elif cmd == "add":
			if word == "":
				await ctx.send(missingArgs, delete_after=3)
			if flag == 0:
				await ctx.send(turnOnFirst, delete_after=3)
			else:
				bad_words.append(word)
				openFile = open("data/filtered-words.txt", mode="a", encoding="utf-8")
				openFile.write("\n{}".format(word))
				await ctx.send('Đã chặn từ "{}**"'.format(word[0]), delete_after=3)
		elif cmd == "delete":
			if word == "":
				await ctx.send(missingArgs, delete_after=3)
			if flag == 0:
				await ctx.send(turnOnFirst, delete_after=3)
			else:
				if word in bad_words:
					bad_words.remove(word)
					openFile = open("data/filtered-words.txt", mode="a", encoding="utf-8")
					openFile.truncate(0)
					for bad in bad_words:
						openFile.write("\n{}".format(bad))
					await ctx.send('Đã xoá từ "{}**"'.format(word[0]), delete_after=3)
				else:
					await ctx.send(deleteNone, delete_after=3)
		elif cmd == "help":
			embed = discord.Embed(title=filterTitle, description=filterDesc, color=0xff5252)
			embed.add_field(name="on/off", value=on_offVal, inline=True)
			embed.add_field(name="add/delete <abc>", value=add_delVal, inline=True)
			embed.add_field(name='throw <ID>', value=throwVal, inline=True)
			embed.set_footer(text=footerCredit)
			await ctx.send(embed=embed)	
		elif cmd == "throw":
			sentChannel = client.get_channel(ctx.message.channel.id)
			msg = await sentChannel.history().find(lambda m: m.id == int(word))
			if msg is None:
				await ctx.send(throwWrongID, delete_after=3) 
			else:
				await msg.delete()
				embed=discord.Embed(title=warningTitle, description=warningDesc.format(msg.author.mention), color=0xff5252)
				embed.set_footer(text=footerCredit)
				await ctx.channel.send(embed=embed)
		else:
			await ctx.send(RECHECK_ARGS, delete_after=3)

@client.command()
async def share(ctx, usr="", pw="", *rank):
	await ctx.message.delete()
	if usr == "" or pw == "" or len(rank) == 0:
		await ctx.send(missingArgs, delete_after=3)
		return
	embed = discord.Embed(title=shareTitle, description=shareDesc, color=0xff5252)
	embed.add_field(name="Username", value=usr, inline=True)
	embed.add_field(name="Password", value=pw, inline=True)
	embed.add_field(name="Rank", value=" ".join(rank), inline=True)
	embed.set_footer(text=footerCredit)
	channel = client.get_channel(799916376537038888)
	await channel.send(embed=embed)	

@client.command()
async def announce(ctx, *mess):
	await ctx.message.delete()
	embed = discord.Embed(title=announceTitle, description=" ".join(mess), color=0xff5252)
	embed.set_footer(text=footerCredit)
	await ctx.send(embed=embed)

client.run(os.getenv('TOKEN'))