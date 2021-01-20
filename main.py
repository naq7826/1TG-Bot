import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

client = discord.Client()
client = commands.Bot(command_prefix='x!')

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(activity=discord.Game('cái loz'))
    

@client.command()
async def share(ctx, usr, pw, rank0, rank1="", rank2=""):
	rank = [rank0, rank1, rank2]
	embed = discord.Embed(title="Share account Valorant", description="Hỏi kỹ chủ acc trước khi thay đổi settings! Rank có thể thay đổi so với hiện tại!", color=0xff5252)
	embed.add_field(name="Username", value=usr, inline=True)
	embed.add_field(name="Password", value=pw, inline=True)
	embed.add_field(name="Rank", value=" ".join(rank), inline=True)
	await ctx.send(embed=embed)
	await ctx.message.delete()

@client.command()
async def announce(ctx, mess):
  embed = discord.Embed(title="THÔNG BÁO, THÔNG BÁO, ALO ALO ALOOO", description=mess, color=0xff5252)
  await ctx.send(embed=embed)
  await ctx.message.delete()

client.run(os.getenv('TOKEN'))