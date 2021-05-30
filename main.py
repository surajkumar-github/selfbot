
import os
import difflib
import sqlite3
#db = sqlite3.connect('poke2auto.db')
#cur = db.cursor()
count = 0
f = open('pokes.txt', 'r')
file = f.read()
file = file.split('\n')
for i in file:
    if len(i) < 2:
        del file[file.index(i)]
mon_list = []
for i in file:
    if len(i) >= 3:
        mon_list.append(i)
import discord
from discord.ext import commands
from discord.ext import tasks
from random import choice
import asyncio
from keep_alive import keep_alive
import requests
from discord_webhook import DiscordWebhook


cid = "822530222153793536"
editing = {

}
req = requests.get("https://discord.com/api/path/to/the/endpoint")



print(req)
import time
#mon_url=input('url')
gg = open('caught.txt', 'a')
import random
#cid = 801907193754288249
import discord
from discord.ext import commands, tasks

from random import choice

client = commands.Bot(command_prefix='_')
client._skip_check = lambda x, y: False
status = ['_help', 'contact: @Rapter#2273']
queue = []

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

hint = ""
@client.event
async def on_message(message):
      
      #if message.channel
     # if message.guild.id not in guilds:
        #return
      def check(m):
          return m.channel == message.channel and m.author != client.user and "The pokémon is" in m.content

      global hint
      global editing
   
    #if "The pokémon is" in message.content:
      #await message.delete()
      global count
      if "The pokémon is" in message.content:
        response = message
        s = response.content.split(" is ")[1].replace(".","")
        #response.delete()
        print(s)
        x = get_mon(s)
        #print(options)
        print(x)
        first_options = x
        if len(first_options) ==0:
          first_options = ["nidoran","farfetch'd"]
       
       
        m = await message.channel.send(first_options[0])
        for i in first_options[1:3]:
          await asyncio.sleep(1)
          await m.edit(content = +i)
        if message.channel.id not in editing.keys():
          editing[message.channel.id] = m

        
      elif "These colors seem unusual" in message.content and message.author.id == 716390085896962058:
        webhook = DiscordWebhook(url="Put url here",content = message.content)
        webhook.execute(message.content)
      elif "You caught a" in message.content:
        count = count +1
        print(count)
      #await client.process_commands(message)
      embeds = message.embeds 
  # await client.process_commands(message)
      if not message.embeds:
        await client.process_commands(message)
        return
      title = (embeds[0].to_dict()['title'])


      
      

        
      
      #print(val)
         

    

def get_mon(val):
  
 
  

  val = val.lower()
  while "\_" in val:
      val = val.replace("\_", "-")
        #print(val)
  length = len(val)
  l = list(val)
  new_chars = []
  
  
  with open('pokes.txt') as f:
       lines = [line.rstrip() for line in f]
  new_names = []
  for i in lines:
    if len(i) == length:
      new_names.append(i)
  #print(new_names)
  final_list = []
  for i in new_names:
    name_list = list(i)
    index = 0
    #print(i)

    flag = False
    for k in l:
      if name_list[index] != k and k != "-":
       # print(name_list[index]+"!="+k)
        flag = True
      index = index+1
    if not flag:
      final_list.append(i)
  #print(final_list)
  return final_list
        


@client.command()
async def catchrate(ctx):
  global count
  count = 0
  print(count)
  await asyncio.sleep(60)
  catch_rate = count/60
  await ctx.send(f'the catch rate is {count} mons per minute')




@client.command()
async def say(ctx, *, args):
 
  
 
  await ctx.send(args)

@client.command(name='ping')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')






keep_alive()
client.run('ODM0NDc5MzY4ODQ3MjI4OTY4.YIBfeQ.jzEYJ9RSJMOTTZUYDpOIwcUNHj0')