import discord
from discord.ext import commands, tasks
from random import choice


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
  embed.add_field(name='invite', value='Gives you the invite link for inviting people to the server and help us grow this server. \nThanks in advance for inviting people 😊')
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













client.run(os.environ['token'])