import discord
from discord.ext import commands, tasks
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
queuers = []
mans_channel_ID = 1048570045757935636


#bot setup
bot = commands.Bot(command_prefix='*', intents=intents)       

@bot.event
async def on_ready():
    print(f"Let's get tropical - {bot.user.name}")
    clear_queue.start()


#clear queue function
@tasks.loop(hours=1)
async def clear_queue():
    channel = bot.get_channel(mans_channel_ID)
    message = f""
    if len(queuers) > 0:
        for queuer in queuers:
            message = message + f"{queuer.mention}. "
        embedVar = discord.Embed(
            title='Release Yer Dutch Rudders, Mateys',
            description = "Kicked for jorkin it raw",
            color = discord.Color.red()
        )
        queuers.clear()
        await channel.send(message, embed=embedVar)

#funny, person-specific easter eggs
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'koolhof' in message.content.lower():
        await message.channel.send("Lame")
    elif 'jerry' in message.content.lower():
        await message.channel.send('goat.')
    elif 'jury' in message.content.lower():
        await message.channel.send('anything for my big th#####ng dicktator.')
    elif 'bobby' in message.content.lower():
        await message.channel.send("ew old. old perv. bobby looked up my skirt once. I was standing on a ladder in front of him in a mini-skirt, but I knew he was looking.")
    elif 'myte' in message.content.lower():
        await message.channel.send("tsun tsun tsun tsun tsun tsun tsun tsun. where dere?")
    await bot.process_commands(message)    

#stops losers from editing comments
@bot.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    await after.reply(f"Look at this virgin editing messages. Jury is gonna spank you with his punishment noodle.\nOriginal message '{before.content}'.\nYou disgust me.")


#join queue handler
@bot.command()
async def queue(ctx):
    if ctx.message.author in queuers:
        await ctx.send(f"*qUEuE. \nstfu. you're in the queue, fucker.")
    else:
        queuers.append(ctx.message.author)
        if len(queuers) == 6:
            embedVar = discord.Embed(
                title='POP POP. Quit jorkin it and play some RL',
                description='Queue popped',
                color=discord.Color.green()
            )
            await ctx.send(f"{queuers[0].mention}, {queuers[1].mention}, {queuers[2].mention}, {queuers[3].mention}, {queuers[4].mention}, {queuers[5].mention}.", embed=embedVar)
            queuers.clear()          
        else:
            names = ""
            for queuer in queuers:
                names = names+f"{queuer.display_name}. "
            embedVar = discord.Embed(
                title='Chronic Masturbaters Waiting:',
                description=f"{names} just jorkin and waiting",
                color=discord.Color.green()
            )
            await ctx.send(embed=embedVar)
            #await ctx.send(f"Queued... fucker \n\n{names}\nin queue.")
   

#leave queue handler
@bot.command()
async def leave(ctx):
    if ctx.message.author in queuers:
        queuers.remove(ctx.message.author)
        if len(queuers) > 0:
            names = ""
            for queuer in queuers:
                names = names+f"{queuer.display_name}. "
            embedVar = discord.Embed(
                title='Chronic Masturbaters Waiting:',
                description=f"{names} just jorkin and waiting",
                color=discord.Color.green()
            )
            await ctx.send(embed=embedVar)
        else:
            await ctx.send("Later loser\nQueue empty.")
    else:
        await ctx.send("You aren't even in the queue, butthole.")

@bot.command()
async def remove(ctx):
    to_remove = ctx.message.content.split(" ", maxsplit=1)[1].lower()
    for queuer in queuers:
        if queuer.display_name.lower() == to_remove:
            if len(queuers) > 1:
                queuers.remove(queuer)
                names = ""
                for q in queuers:
                    names = names+f"{q.display_name}. "
                embedVar = discord.Embed(
                    title='Chronic Masturbaters Waiting:',
                    description=f"{names} just jorkin and waiting",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embedVar)
            else:
                await ctx.send("Later loser\nQueue empty.")

@bot.command()
async def status(ctx):
    names = ""
    if len(queuers) > 0:
        for queuer in queuers:
            names = names+f"{queuer.display_name}. "
        embedVar = discord.Embed(
                title='Chronic Masturbaters Waiting:',
                description=f"{names} just jorkin and waiting",
                color=discord.Color.green()
            )
        await ctx.send(embed=embedVar)
    else:
        await ctx.send("Empty af. Just waiting for ahqwa to start some shit.")

#turns bot on uwu
bot.run(token, log_handler=handler, log_level=logging.DEBUG)

