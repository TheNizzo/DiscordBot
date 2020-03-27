import os
import traceback
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from corona import get_lebanon, get_world, get_top
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user.name:
        return
    elif re.match("^\.[a-zA-Z]+", message.content):
        print("Im here")
        response = "Hey there, " + message.author.mention + ". I see you are using Moe's bot (lame). Why dont you try typing '!help' for a list of (USEFUL) commands from my part. :)"
        print(message.author.name + " just used moe's command. Get him!")
        await message.channel.send(response)
        #await message.channel.send("Hey there, " + message.author + ". I see you are using Moe's bot (lame).\nWhy dont you try typing '!help' for a list of (USEFUL) commands from my part ;)")
    elif message.content == 'speak!':
        response = "Okay please dont hurt me ya zghirrrrrrrr"
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
    await bot.process_commands(message)

@bot.command(name='speak', help='Tells you that the bot is speaking.')
async def speak_bot(ctx):
    response = "```I am speaking wle```"
    await ctx.send(response)

@bot.command(name='roll_dice', help='Roll two dice.')
async def roll(ctx):
    dice = [
        str(random.choice(range(1, 7)))
        for _ in range(2)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='corona', help='Displays corona numbers today')
async def corona(ctx, country='Lebanon'):
    if country == 'world':
        list = get_world()
        response = "``` Showing Corona numbers for the entire fucking planet:\n - Total cases: {}.\n - Total deaths: {}.\n - Total recovered: {}.```".format(list[0], list[1], list[2])
        await ctx.send(response)
        print("CORONA: " + ctx.message.author.name + " search: " + country)
        return
    elif country == 'top':
        list = get_top()
        response = "``` Showing top 10 countries with corona cases:\n - {0:<11}: {1:>9} cases.\n".format(list[0][0], list[0][1])
        tmp1 = " - {0:<11}: {1:>9} cases.\n".format(list[1][0], list[1][1])
        tmp2 = " - {0:<11}: {1:>9} cases.\n".format(list[2][0], list[2][1])
        tmp3 = " - {0:<11}: {1:>9} cases.\n".format(list[3][0], list[3][1])
        tmp4 = " - {0:<11}: {1:>9} cases.\n".format(list[4][0], list[4][1])
        tmp5 = " - {0:<11}: {1:>9} cases.\n".format(list[5][0], list[5][1])
        tmp6 = " - {0:<11}: {1:>9} cases.\n".format(list[6][0], list[6][1])
        tmp7 = " - {0:<11}: {1:>9} cases.\n".format(list[7][0], list[7][1])
        tmp8 = " - {0:<11}: {1:>9} cases.\n".format(list[8][0], list[8][1])
        tmp9 = " - {0:<11}: {1:>9} cases.\n".format(list[9][0], list[9][1])
        await ctx.send(response + tmp1 + tmp2 + tmp3 + tmp4 + tmp5 + tmp6 + tmp7 + tmp8 + tmp9 + "```")
        print("CORONA: " + ctx.message.author.name + " search: " + country)
        return
    try:
        list = get_lebanon(country.capitalize())
    except Exception:
        print("==================================")
        print("CORONA: "+ctx.message.author.name + " tried typing: "+ country+ "\n but resulted in:\n")
        traceback.print_exc()
        print("==================================")
        await ctx.send("Error Occured: Country format not valid")
        return
    
    response = "```diff\nShowing Corona numbers for {}:\n - Total cases: {}.\n {} since yesterday\n - Total deaths: {}.\n {} since yesterday\n - Total recovered: {}.\n```".format(country, list[1], list[2], list[3], list[4], list[5])
    print("CORONA: " + ctx.message.author.name + " search: " + country)
    await ctx.send(response)


@bot.command(name="suits", help="Displays random quotes from SUITS.")
async def suits(ctx):
    list = [
        "Harvey Specter:  “Let them hate, just make sure they spell your name right.",
        "Harvey Specter: “They think you care, they’ll walk all over you.",
        "Harvey Specter: “Win a no win situation by rewriting the rules.",
        "Harvey Specter: “Winners don’t make excuses.",
        "Louis : I found your weak spot. So I am going to keep hammering on her until you break.",
        "Harvey Specter:  I want you to tell me the worst mistake you ever made as a therapist.",
        "Harvey Specter: “I don’t play the odds I play the man.",
        "Louis : How dare you defile Game of Thrones by comparing Harvey to Jon Snow.",
        "Donna: I don’t want the money. I want something more, and I’ve never said that out loud but I can’t pretend that’s not true anymore.",
        "Louis: Give me a mountain, I’ll climb it. Give me a Katy Perry song, I’ll sing it.",
        "Harvey Specter: “Anyone can do my job, but no one can be me.",
        "Harvey Specter: When someone twists a knife in your gut, I feel like I want to twist one right back.",
        "Harvey Specter:  I’m emotionally vested in me.",
        "Dr. Agard : It wasn’t weakness that made you break your word. It was love.",
        "Harvey Specter: “That’s the difference between you and me. You wanna lose small, I wanna win big.",
        "Harvey Specter: The wheels of Justice turn slowly, Tommy. Which means even if you win, you won’t be here to see it.",
        "Harvey : Take the drama down a notch, Juliet.",
        "Frank: You owe me thirteen years. I’m going to collect!",
        "George Costanza: I’m the judge and the jury, pal. And the verdict is…guilty!",
        "Louis:  Unless you have Photoshopped my head onto a dragon, do not interrupt me.",
        "Harvey Specter: “I don’t pave the way for people… people pave the way for me.",
        "Rachel : How do I tell a man he’s going to die?",
        "Harvey Specter:  I’m not here for your absolution, I’m here for your redemption.",
        "Samantha: If you think I couldn’t turn you into a puddle, you are wildly mistaken.",
        "Harvey Specter: “It’s not bragging if it’s true.",
        "Harvey Specter: “I’m not about caring, I’m about winning.",
        "Donna: I’m sorry I don’t have a photographic memory but my brain is too busy being awesome.",
        "Harvey Specter:  Captain Kirk is the man and I don’t want to hear another word about it.",
        "Harvey Specter: “You always have a choice.",
        "Louis: You better pull up a seat for me at the table or I will break the whole god damn thing in two.",
        "Harvey Specter:  The next move you’re going to make behind my back is finding another job.",
        "Donna: I’ve already had seventeen oysters. Who says I can’t have an eighteenth?",
        "Mike Ross: Sometimes I like to hang out with people who aren’t that bright, you know, just to see how the other half lives.",
        "Harvey Specter: “Ever loved someone so much, you would do anything for them? Yeah, well make that someone yourself and do whatever the hell you want.",
        "Harvey : “When you are backed against the wall, break the goddamn thing down.",
        "Harvey :  “I’m against having emotions, not against using them.",
        "Harvey :  Winners stick it out when the other side plays the game.",
        "Harvey :  First impressions last. Start behind the eight ball and you’ll never get in front.",
        "Brian : My job may be to push back, but it’s also to have your back, and from now on I will.",
        "Harvey Specter: “I don’t have dreams, I have goals.",
        "Mike Ross: I thought you liked it when I breached your borders?",
        "Harvey Specter: “Sorry, I can’t hear you over the sound of how awesome I am.",
        "Harvey Specter:  “I believe in work, I don’t fuck with luck.",
        "Harvey Specter: It's going to happen because I am going to make it happen."
    ]

    response = random.choice(list)
    tmp = response.split(":")
    await ctx.send("" + tmp[0] + " : ``" + tmp[1] + "``")

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)
