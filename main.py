import discord
import os
import asyncio
from data.strings import *
from discord.ext import commands
#from dotenv import load_dotenv
#load_dotenv(dotenv_path='.env')


### Variables ###
client = discord.Client()
client = commands.Bot(command_prefix='!!')
flagTroll = 0
flag = 0
bad_words = []
bad_words_troll = []
banned_users = []

### EVENTS HERE ###
@client.event
async def on_ready():
	global banned_users
	with open("data/banned-users.txt", encoding="utf-8") as file:
		banned_users = [user.strip().lower() for user in file.readlines()[1:]]
	print('We have logged in as {0.user}'.format(client))
	#channel = client.get_channel(802668401951768606)
	#msg = await channel.fetch_message(802670938155647036)
	#reaction = client.get_emoji(819675505841406022)
	#await msg.add_reaction(reaction)
	await client.change_presence(activity=discord.Game('made by Quanimus'))

@client.event
async def on_message(message):
	print(message.author.id)
	print(banned_users[0])
	if message.author == client.user:
		return
	if message.author.bot:
		return
	message_content = message.content.lower().split()
	if message.author.id == 797491259793997854 and flagTroll == 1:  
		message_joined = "".join(message_content)
		for bad_word_troll in bad_words_troll:
			if bad_word_troll in message_joined :
				await message.delete()
				embed=discord.Embed(title=announceTitle, description=NO_MORE_CK, color=0xff5252)
				embed.set_footer(text=footerCredit)
				await message.channel.send(embed=embed)
				break
	if flag == 1:
		for bad_word in bad_words:
			if bad_word in message_content and "delete" not in message_content:
				await message.delete()
				embed=discord.Embed(title=warningTitle, description=warningDesc.format(message.author.mention), color=0xff5252)
				embed.set_footer(text=footerCredit)
				await message.channel.send(embed=embed)
				break
	for user in banned_users:
		if message.author.id == int(user):
			await message.delete()
			embed=discord.Embed(title=announceTitle, description=bannedDesc.format(message.author.mention), color=0xff5252)
			embed.set_footer(text=footerCredit)
			await message.channel.send(embed=embed)
			break
	await client.process_commands(message)

@client.event
async def on_raw_reaction_add(payload):
	#print(payload.emoji)
	user = await client.fetch_user(payload.user_id)
	if user == client.user:
		return
	if user.bot:
		return
	if payload.message_id == 802404871294025749:
		if str(payload.emoji) == "✅":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "Members")
			await payload.member.add_roles(role)
		else:
			channel = client.get_channel(payload.channel_id)
			message = await channel.fetch_message(payload.message_id)
			user = await client.fetch_user(payload.user_id)
			if payload.emoji.id is None:
				await message.remove_reaction(payload.emoji.name, user)
			else:
				reaction = client.get_emoji(payload.emoji.id)
				await message.remove_reaction(reaction, user)	
	elif payload.message_id == 802670938155647036:
		if str(payload.emoji) == "<:valorant:802666303298338876>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "Valorant")
			await payload.member.add_roles(role)
	
		elif str(payload.emoji) == "<:csgo:802666608568958978>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "CSGO")
			await payload.member.add_roles(role)

		elif str(payload.emoji) == "<:fo4:802667507638730813>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "FIFA Online 4")
			await payload.member.add_roles(role)

		elif str(payload.emoji) == "<:amongus:802667860919844914>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "Among Us")
			await payload.member.add_roles(role)

		elif str(payload.emoji) == "<:ark:802668235010736168>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "ARK")
			await payload.member.add_roles(role)

		elif str(payload.emoji) == "<:GenshinImpact:819675505841406022>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "Genshin Impact")
			await payload.member.add_roles(role)

		else:
			channel = client.get_channel(payload.channel_id)
			message = await channel.fetch_message(payload.message_id)
			user = await client.fetch_user(payload.user_id)
			if payload.emoji.id is None:
				await message.remove_reaction(payload.emoji.name, user)
			else:
				reaction = client.get_emoji(payload.emoji.id)
				await message.remove_reaction(reaction, user)	

@client.event
async def on_raw_reaction_remove(payload):
	if payload.message_id == 802404871294025749 and str(payload.emoji) == "✅":
		guild = await client.fetch_guild(payload.guild_id)
		user = await guild.fetch_member(payload.user_id)
		role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "Members")
		await user.remove_roles(role)
	elif payload.message_id == 802670938155647036:
		guild = await client.fetch_guild(payload.guild_id)
		user = await guild.fetch_member(payload.user_id)
		if str(payload.emoji) == "<:valorant:802666303298338876>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "Valorant")
			await user.remove_roles(role)
	
		elif str(payload.emoji) == "<:csgo:802666608568958978>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "CSGO")
			await user.remove_roles(role)

		elif str(payload.emoji) == "<:fo4:802667507638730813>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "FIFA Online 4")
			await user.remove_roles(role)

		elif str(payload.emoji) == "<:amongus:802667860919844914>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "Among Us")
			await user.remove_roles(role)

		elif str(payload.emoji) == "<:ark:802668235010736168>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "ARK")
			await user.remove_roles(role)

		elif str(payload.emoji) == "<:GenshinImpact:819675505841406022>":
			role = discord.utils.get(client.get_guild(payload.guild_id).roles, name = "Genshin Impact")
			await user.remove_roles(role)



### COMMANDS HERE ###
@client.command()
async def filterTroll(ctx, cmd="", *word):
	global flagTroll
	global bad_words_troll
	await ctx.message.delete()
	if cmd == "":
		await ctx.send(missingArgs, delete_after=3)
	elif discord.utils.get(ctx.message.author.roles, name="Administrators") is None and discord.utils.get(ctx.message.author.roles, name="OWNER") is None:
		if flagTroll == 1:
			await ctx.send(filterCmdNotAdmin1)
		if flagTroll == 0:
			await ctx.send(filterCmdNotAdmin0)
	else:
		if cmd == "on":
			flagTroll = 1
			with open("data/filteredTroll-words.txt", encoding="utf-8") as file:
				bad_words_troll = [bad_word_troll.strip().lower() for bad_word_troll in file.readlines()[1:]]
			await ctx.send(filterTrollOn)
		elif cmd == "off":
			flagTroll = 0
			await ctx.send(filterTrollOff)
		elif cmd == "add":
			if len(word) == 0:
				await ctx.send(missingArgs, delete_after=3)
			if flagTroll == 0:
				await ctx.send(turnOnFirst, delete_after=3)
			else:
				openFile = open("data/filteredTroll-words.txt", mode="a", encoding="utf-8")
				for w in word:
					bad_words_troll.append(w)
					openFile.write("\n{}".format(w))
				await ctx.send('Đã chặn từ "{}" :)'.format(" ".join(word)))
		elif cmd == "delete":
			f=0
			if len(word) == 0:
				await ctx.send(missingArgs, delete_after=3)
			elif flagTroll == 0:
				await ctx.send(turnOnFirst, delete_after=3)
			else:
				for w in word:
					if w in bad_words_troll:
						bad_words_troll.remove(w)
						f=1
				openFile = open("data/filteredTroll-words.txt", mode="a", encoding="utf-8")
				openFile.truncate(0)
				for bad in bad_words_troll:
					openFile.write("\n{}".format(bad))
				await ctx.send('Đã xoá từ "{}" :)'.format(" ".join(word)))
				if f == 0:
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
async def filter(ctx, cmd="", *word):
	global flag
	global bad_words
	await ctx.message.delete()
	if cmd == "":
		await ctx.send(missingArgs, delete_after=3)
	elif discord.utils.get(ctx.message.author.roles, name="Administrators") is None and discord.utils.get(ctx.message.author.roles, name="OWNER") is None:
		await ctx.send(filterCmdNotAdmin0)
	else:
		if cmd == "on":
			flag = 1
			with open("data/filtered-words.txt", encoding="utf-8") as file:
				bad_words = [bad_word.strip().lower() for bad_word in file.readlines()[1:]]
			await ctx.send(filterOn)
		elif cmd == "off":
			flag = 0
			await ctx.send(filterOff)
		elif cmd == "add":
			if len(word) == 0:
				await ctx.send(missingArgs, delete_after=3)
			if flag == 0:
				await ctx.send(turnOnFirst, delete_after=3)
			else:
				openFile = open("data/filtered-words.txt", mode="a", encoding="utf-8")
				for w in word:
					bad_words.append(w)
					openFile.write("\n{}".format(w))
				await ctx.send('Đã chặn từ "{}**"'.format(word[0][0]))
		elif cmd == "delete":
			f=0
			if len(word) == 0:
				await ctx.send(missingArgs, delete_after=3)
			if flag == 0:
				await ctx.send(turnOnFirst, delete_after=3)
			else:
				for w in word:
					if w in bad_words:
						bad_words.remove(w)
						f=1
				openFile = open("data/filtered-words.txt", mode="a", encoding="utf-8")
				openFile.truncate(0)
				for bad in bad_words:
					openFile.write("\n{}".format(bad))
				await ctx.send('Đã xoá từ "{}**"'.format(word[0][0]))
			if f == 0:
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
async def ban(ctx, cmd="", userID=""):
	global banned_users
	await ctx.message.delete()
	if cmd == "" or userID=="":
		await ctx.send(missingArgs, delete_after=3)
	elif discord.utils.get(ctx.message.author.roles, name="Administrators") is None and discord.utils.get(ctx.message.author.roles, name="OWNER") is None:
		await ctx.send(filterCmdNotAdmin0)
	else:
		if cmd == "add":
			if len(userID) == 0:
				await ctx.send(missingArgs, delete_after=3)
			else:
				openFile = open("data/banned-users.txt", mode="a", encoding="utf-8")
				banned_users.append(userID)
				openFile.write("\n{}".format(userID))
				await ctx.send('<@!{}> Khỏi chat nữa nha cđ ơi'.format(userID))
		elif cmd == "delete":
			if len(userID) == 0:
				await ctx.send(missingArgs, delete_after=3)
			else:
				if userID in banned_users:
					banned_users.remove(userID)
					f=1
					openFile = open("data/filtered-words.txt", mode="a", encoding="utf-8")
					openFile.truncate(0)
					for user in banned_users:
						openFile.write("\n{}".format(user))
					await ctx.send('Đã unban <@!{}>'.format(userID))
				else:
					await ctx.send(deleteNone2, delete_after=3)
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

@client.command()
async def ruleEdit(ctx, *mess):
	await ctx.message.delete()
	newmess = ["**ĐỌC KỸ NỘI QUY VÀ TICK ĐỒNG Ý ĐỂ THAM GIA SERVER**\n\n",mess[0]]
	embed = discord.Embed(title=announceTitle, description="".join(newmess), color=0xff5252)
	embed.set_footer(text=footerCredit)
	channel = client.get_channel(794369918429954058)
	msg = await channel.fetch_message(802404871294025749)
	await msg.edit(embed=embed)

@client.command()
async def msgEdit(ctx, msgID, *mess):
	await ctx.message.delete()
	embed = discord.Embed(title=announceTitle, description=" ".join(mess), color=0xff5252)
	embed.set_footer(text=footerCredit)
	channel = ctx.channel
	msg = await channel.fetch_message(msgID)
	await msg.edit(embed=embed)

@client.command()
async def accEdit(ctx, msgID, usr="", pw="", *rank):
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
	msg = await channel.fetch_message(msgID)
	await msg.edit(embed=embed)

client.run(os.getenv('TOKEN'))