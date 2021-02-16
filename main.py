import discord
from discord.ext import commands, tasks
from random import choice
import os

# BotLink = https://discord.com/api/oauth2/authorize?client_id=810896982037233664&permissions=2147483639&scope=bot


client = commands.Bot(command_prefix=commands.when_mentioned_or("%"), description='A simple helping bot for Team Shadow!')
client.remove_command('help')
status = ['Listening to %help','Watching Team Shadows','🍩 Eating Doughnut']

def colour():
  l = [ 1752220, 3066993, 3447003, 10181046, 15844367, 15105570, 15158332, 3426654, 16580705 ]
  return choice(l)


@client.event
async def on_ready():
  change_status.start()
  print("The Bot is online!")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


@client.command()
async def help(ctx, com = None):
  if com == None:
    em = discord.Embed(
      title = 'Help',
      description = 'Following are the commands available for you to use with this bot.',
      colour = colour()
    )
    em.add_field(name='ping', value='Helps you check the latency. type `%ping` to use the command',inline=False)
    em.add_field(name='invite', value='Gives you the invite link for inviting people to the server and help us grow this server. \nThanks in advance for inviting people 😊', inline=False)
    em.add_field(name='bam', value='You get BAMMED!!. Type `%bam` to use the command.',inline=False)
    em.add_field(name='pog', value="Are you a POGGER!!? Let's see. Type `%pog`. ",inline=False)
    em.add_field(name='kick', value="Helps you kick a member. Type `%kick [mention user] [reason]`. ",inline=False)
    em.add_field(name='ban', value="Helps you ban a member. Type `%ban [mention user] [reason]`. ",inline=False)
    em.add_field(name='unban', value="Helps you unban a member. Type `%unban [mention user] [reason]`. Make sure to mention the user as `name#discriminator` for example `sample#8643`",inline=False)
    em.add_field(name='mute', value="Helps you mute a member. Type `%mute [mention user] [reason]`",inline=False)
    em.add_field(name='unmute', value="Helps you unmute a member. Type `%unmute [mention user]`",inline=False)
    em.add_field(name='warn', value="Helps you warn a member. Type `%warn [mention user] [reason]`. ",inline=False)
    em.add_field(name='welcome', value="Welcome the new user 😊 \nType `%help welcome` for more details.",inline=False)
    em.set_footer(icon_url=ctx.author.avatar_url, text=f"This message was requested by {ctx.author.name}")
    await ctx.send(embed=em)
  elif (com == 'welcome') or (com == 'wel'):
    em = discord.Embed(
      title = "Welcome Command Help Box",
      colour = colour()
    )
    em.add_field(name='Usage', value="type `%welcome` or `%welcome [mention the user]` \nFor Example: \n `%welcome @team_shadow_members`", inline=False)
    em.add_field(name ='Alias', value="`%wel`", inline=False)
    await ctx.send(embed=em)
  else:
    embed = discord.Embed(
    title = "You have entered a wrong command.",
    description = "Type `%help` to see the help box or type `%help welcome` to see more about the welcome command.",
    colour = discord.Colour.red()
    )
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


@client.command(aliases=['wel'])
async def welcome(ctx, user : discord.Member = None):
  if user == None:
    embed = discord.Embed(
      title = 'Welcome to the Server!!',
      description = "Hello Everyone, Welcome to the server. \nWe hope to build a better community with you 😊",
      colour = colour()
    )
    embed.set_image(url = 'https://media.giphy.com/media/14aa5GbbHT3bHO/giphy.gif')
    await ctx.send(embed = embed)
  else:
    embed = discord.Embed(
      title = 'Welcome to the Server!!',
      description = f"Hello {user.mention}, Welcome to the server. \nWe hope to build a better community with you 😊",
      colour = colour()
    )
    embed.set_image(url = 'https://media.giphy.com/media/14aa5GbbHT3bHO/giphy.gif')
    await ctx.send(embed = embed)


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user : discord.Member = None, *,reason = "No reason provided"):
  if user == None:
    em = discord.Embed(
      title = "Whom you want to kick",
      description = "Please try again but this time give me the name of the person to kick. \nExample of the usage: \n `%kick [Mention the person] [give a reason]`",
      colour = discord.Colour.red()
    )
    await ctx.send(embed = em)
  else:
    try:
      try:
        await user.send(f"You have been **kicked** out of the **{ctx.guild.name}**!!\nBecause: **{reason}** ")
        await user.kick(reason = reason)
        em = discord.Embed(
          title = f"Kicked {user.name} out of the server!!",
          description = "We hope now there will be PEACE in the server!",
          colour = discord.Colour.green()
        )
        await ctx.send(embed = em)
      except:
        await user.kick(reason = reason)
        em = discord.Embed(
          title = f"Kicked {user.name} out of the server!!",
          description = "We hope now there will be PEACE in the server!",
          colour = discord.Colour.green()
        )
        await ctx.send(embed = em)
    except:
      em = discord.Embed(
        title = "You don't have the permission to use this command!",
        description = "You need to have administrator permission to use this command",
        colour = discord.Colour.red()
      )
      await ctx.send(embed = em)


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user : discord.Member = None, *,reason = "No reason provided"):
  if user == None:
    em = discord.Embed(
      title = "Whom you want to Ban",
      description = "Please try again but this time give me the name of the person to ban. \nExample of the usage: \n `%ban [Mention the person] [give a reason]`",
      colour = discord.Colour.red()
    )
    await ctx.send(embed = em)
  else:
    try:
      try:
        await user.send(f"You have been **Banned** from **{ctx.guild.name}**!!\nBecause: **{reason}** ")
        await user.ban(reason = reason)
        em = discord.Embed(
          title = f"Banned {user.name} from the server!!",
          description = "We hope now there will be PEACE in the server!",
          colour = discord.Colour.green()
        )
        await ctx.send(embed = em)
      except:
        await user.ban(reason = reason)
        em = discord.Embed(
          title = f"Banned {user.name} from the server!!",
          description = "We hope now there will be PEACE in the server!",
          colour = discord.Colour.green()
        )
        await ctx.send(embed = em)
    except:
      em = discord.Embed(
        title = "You don't have the permission to use this command!",
        description = "You need to have administrator permission to use this command",
        colour = discord.Colour.red()
      )
      await ctx.send(embed = em)


@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, user : discord.Member = None, *,reason = "No reason provided"):
  if user == None:
    em = discord.Embed(
      title = "Whom you want to warn",
      description = "Please try again but this time give me the name of the person to warn. \nExample of the usage: \n `%warn [Mention the person] [give a reason]`",
      colour = discord.Colour.red()
    )
    await ctx.send(embed = em)
  else:
    try:
      try:
        await user.send(f"You have been **Warned** by **{ctx.author.name}** in the **{ctx.guild.name}** for the reason: **{reason}** ")
        em = discord.Embed(
          title = f"Warned {user.name}!!",
          colour = discord.Colour.red()
        )
        await ctx.send(embed = em)
      except:
        em = discord.Embed(
          title = f"Can't send the message to {user.name}",
          colour = discord.Colour.green()
        )
        await ctx.send(embed = em)
        await ctx.send(f"{user.mention} You have been WARNED!!!!")
    except:
      em = discord.Embed(
        title = "You don't have the permission to use this command!",
        description = "You need to have administrator permission to use this command",
        colour = discord.Colour.red()
      )
      await ctx.send(embed = em)


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, user= None):
  if user == None:
    em = discord.Embed(
      title = "Whom you want to UnBan",
      description = "Please try again but this time give me the name of the person to ban. \nExample of the usage: \n `%unban [Mention the person]` \nRemember that you need to specify [user name]#[user discriminator] for exmaple `sample#7834`",
      colour = discord.Colour.red()
    )
    await ctx.send(embed = em)
  else:
    try:
      try:
        banned = await ctx.guild.bans()
        memberName , memberDisc = user.split('#')
        for entry in banned:
          users = entry.user
          if(users.name, users.discriminator) == (memberName, memberDisc):
            await ctx.guild.unban(users)
            await user.send(f"You have been **UnBanned** from **{ctx.guild.name}** !! 🎉")
            em = discord.Embed(
              title = f"UnBanned {user.name}!! 🎉",
              description = "We hope now there will be PEACE in the server!",
              colour = discord.Colour.green()
            )
            await ctx.send(embed = em)
            return
        await ctx.send(f"{user} not found \nPlease try again but this time give me the name of the person to ban. \nExample of the usage: \n `%unban [Mention the person]` \nRemember that you need to specify [user name]#[user discriminator] for exmaple `sample#7834`")
      except:
        banned = await ctx.guild.bans()
        memberName , memberDisc = user.split('#')
        for entry in banned:
          users = entry.user
          if(users.name, users.discriminator) == (memberName, memberDisc):
            await ctx.guild.unban(users)
            em = discord.Embed(
              title = f"UnBanned {user.name}!! 🎉",
              description = "We hope now there will be PEACE in the server!",
              colour = discord.Colour.green()
            )
            await ctx.send(embed = em)
            return
        await ctx.send(user+" not found!! \nPlease try again but this time give me the name of the person to ban. \nExample of the usage: \n `%unban [Mention the person]` \nRemember that you need to specify [user name]#[user discriminator] for exmaple `sample#7834`")
    except:
      em = discord.Embed(
        title = "You don't have the permission to use this command!",
        description = "You need to have administrator permission to use this command",
        colour = discord.Colour.red()
      )
      await ctx.send(embed = em)


@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member = None, reason = "No Reason provided"):
  if member == None:
    em = discord.Embed(
      title = "Whom you want to mute",
      description = "Please try again but this time give me the name of the person to mute. \nExample of the usage: \n `%mute [Mention the person] [reason]`",
      colour = discord.Colour.red()
    )
    await ctx.send(embed = em)
    return

  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")

  if not mutedRole:
    mutedRole = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, add_reactions=False)

  await member.add_roles(mutedRole, reason=reason)
  try:
    await member.send(f"You were **MUTED** in the server **{guild.name}** for **{reason}**")
    em = discord.Embed(
      title = f"{member.name} Muted",
      colour = discord.Colour.green()
    )
    await ctx.send(embed = em)
  except:
    em = discord.Embed(
      title = f"{member.name} Muted",
      colour = discord.Colour.green()
    )
    await ctx.send(embed = em)


@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
  if member == None:
    em = discord.Embed(
      title = "Whom you want to Unmute",
      description = "Please try again but this time give me the name of the person to unmute. \nExample of the usage: \n `%unmute [Mention the person]`",
      colour = discord.Colour.red()
    )
    await ctx.send(embed = em)
    return

  guild = ctx.guild
  mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
  if not mutedRole:
    mutedRole = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole, speak=False, send_messages=False, add_reactions=False)
    
    em = discord.Embed(
      title = f"{member.name} Already Unnuted",
      colour = discord.Colour.green()
    )
    await ctx.send(embed = em)
    return
    

  await member.remove_roles(mutedRole)
  try:
    await member.send(f"You were unmuted in the server {ctx.guild.name}")
    em = discord.Embed(
      title = f"{member.name} Unmuted",
      colour = discord.Colour.green()
    )
    await ctx.send(embed = em)
  except:
    em = discord.Embed(
      title = f"{member.name} Unmuted",
      colour = discord.Colour.green()
    )
    await ctx.send(embed = em)
    












client.run(os.environ['token'])