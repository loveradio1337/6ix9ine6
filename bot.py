import discord
from discord.ext import commands
import json
import time
import random

bot = commands.Bot(command_prefix='!')
extensions = ['Commands.leaderboard']

@bot.event
async def on_ready():
    print('Logged in as {} with the ID: {}'.format(bot.user.name, bot.user.id))

@bot.event
async def on_message(message):
    with open("Commands\\users.json", "r") as f:
        users = json.load(f)

        if message.author.bot:
            return
        if message.channel.is_private:
            return
        else:
            await update_data(users, message.author, message.server)
            number = random.randint(5,10)
            await add_experience(users, message.author, number, message.server)
            await level_up(users, message.author, message.channel, message.server)

        with open("Commands\\users.json", "w") as f:
            json.dump(users, f)
    await bot.process_commands(message)

async def update_data(users, user, server):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"] = 0
        users[user.id]["level"] = 1
        users[user.id]["last_message"] = 0

async def add_experience(users, user, exp, server):
    if time.time() - users[user.id]["last_message"] > 1: 
        users[user.id]["experience"] += exp
        users[user.id]["last_message"] = time.time()
    else:
        return

async def level_up(users, user, channel, server):
    experience = users[user.id]["experience"]
    lvl_start = users[user.id]["level"]
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await bot.send_message(channel, f":tada: Congrats {user.mention}, you levelled up to level {lvl_end}!")
        users[user.id]["level"] = lvl_end

if __name__ == '__main__':
    try:

        for extension in extensions:
            bot.load_extension(extension)

    except Exception as error:
        print(error)

bot.run('BOT_TOKEN')