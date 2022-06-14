#ctx = context(上下文)
import discord
from discord.ext import commands
import json
import random
import os 

with open('setting.json','r',encoding='utf8') as jfile:
   jdata = json.load(jfile)
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[',intents=intents)

#機器人狀態
@bot.event
async def on_ready():
   print(">> bot is online <<")

#機器人傳圖片
@bot.command()
async def 圖片(ctx):
   random_pic = random.choice(jdata['pic'])
   pic = discord.File(random_pic)
   await ctx.send(random_pic)

#機器人傳網路圖片
@bot.command()
async def web(ctx):
   random_pic = random.choice(jdata['url_pic'])
   await ctx.send(random_pic)

#成員加入訊息
@bot.event
async def on_member_join(member):
   channel = bot.get_channel(int(jdata['Welcome_channel']))
   await channel.send(f'{member} join!')

#成員離開訊息
@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(int(jdata['Leave_channel']))
   await channel.send(f'{member} leave!')


for filename in os.listdir('./cmds'):
   if filename.endswith('.py'):
      bot.load_extension(f'cmds.{filename[:-3]}')


if __name__ == "__main__":

bot.run(jdata['TOKEN'])