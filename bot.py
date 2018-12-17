import discord

from discord.ext import commands

from discord.ext.commands import Bot

import youtube_dl

import random

from os import environ

import asyncio

import time

import random

import datetime

import math

import requests


import random


import datetime

import math

import sys

import base64

import hashlib

import traceback

import string

import inspect

import json

import aiohttp

import websockets

import urllib.request

import logging

from collections import Counter

import os

import colorsys

import socket
from os import environ
from lxml import html
import asyncio
import time
import random
import datetime
import math
import requests
import sys
import base64
import hashlib
import traceback
import string
import inspect
import json
from cleverwrap import CleverWrap
import config
import utils
import aiohttp
import websockets
from bs4 import BeautifulSoup
import urllib.request
import logging
import colorsys
import socket


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

bot.run(os.environ['BOT_TOKEN'])