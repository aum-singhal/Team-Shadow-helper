import discord
from discord.ext import commands, tasks
from random import choice
import os

# BotLink = 'https://discord.com/api/oauth2/authorize?client_id=810896982037233664&permissions=2147483639&scope=bot'


client = commands.Bot(command_prefix=commands.when_mentioned_or("%"), description='A simple helping bot for Team Shadow!')
client.remove_command('help')
status = ['Listening to %help','Drinking Water 🥤','🍩 Eating Doughnut']

def colour():
  l = [
    1752220, 3066993, 3447003, 10181046, 15844367,
    15105570, 15158332, 3426654, 1146986, 2067276,
    2123412, 7419530, 12745742, 11027200, 10038562,
    2899536, 16580705, 12320855
  ]
  return choice(l)


@client.event
async def on_ready():
  change_status.start()
  print("The Bot is online!")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


@client.command()
async def help(ctx):
  embed = discord.Embed(
    title = 'Help',
    description = 'Following are the commands available for you to use with this bot.',
    colour = colour()
  )
  embed.add_field(name='ping', value='Helps you check the latency. type `%ping` to use the command',inline=False)
  embed.add_field(name='invite', value='Gives you the invite link for inviting people to the server and help us grow this server. \nThanks in advance for inviting people 😊', inline=False)
  embed.add_field(name='bam', value='You get BAMMED!!. Type `%bam` to use the command.',inline=False)
  embed.add_field(name='bam', value="Are you a POGGER!!? Let's see. Type `%pog`. ",inline=False)
  embed.set_footer(icon_url=ctx.author.avatar_url, text=f"This message was requested by {ctx.author.name}")
  await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
  embed = discord.Embed(
    title = f'Latency: {round(client.latency *1000)}ms',
    colour = colour()
    )
  await ctx.send(embed=embed)


@client.command()
async def invite(ctx):
  embed = discord.Embed(
    title = 'Invite to Server',
    description = 'https://discord.gg/9mbMuGpQHm',
    colour = colour()
    )
  embed.set_footer(text='Help Us grow by inviting people.')
  await ctx.send(embed=embed)


@client.command()
async def bam(ctx):
  embed = discord.Embed(
    title = f"{ctx.author.name} Got Bammed!!",
    colour = colour()
  )
  embed.set_image(url = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/447790b1-04f1-4ed2-9001-15e6b6f2dfaf/d6yin79-b9e8723a-4866-4cb1-9706-19670676e5f6.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNDQ3NzkwYjEtMDRmMS00ZWQyLTkwMDEtMTVlNmI2ZjJkZmFmXC9kNnlpbjc5LWI5ZTg3MjNhLTQ4NjYtNGNiMS05NzA2LTE5NjcwNjc2ZTVmNi5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.w_vE88Hd7ju-bsXRPm3DMGLl4G0Rzr-fn70i-x3Iq8U')
  await ctx.send(embed = embed)


@client.command()
async def pog(ctx):
  embed = discord.Embed(
    title = f"{ctx.author.name}, Hello Pogger",
    colour = colour()
  )
  embed.set_image(url = 'https://i.redd.it/4vba1tggcb351.jpg')
  await ctx.send(embed = embed)














client.run(os.environ['token'])