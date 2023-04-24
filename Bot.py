import discord
from discord import channel
from discord import user
from discord.ext import commands,tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands.core import cooldown
from discord.flags import Intents
from discord.utils import parse_time
import requests
import datetime
import asyncio
import json
from discord.ext.commands.cooldowns import BucketType
import os
from discord.ext import commands
import time
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


async def msg_delete(sent):
    time.sleep(20)
    await sent.delete()

@bot.event
async def on_message(message):
    if not message.author.bot and message.channel.id == 100000000000000:
        yt_v1 = ['https://www.youtube.com/watch?v=', 'https://youtu.be/']
        msg = message.content
        msg_split = msg.split(' ')
        for patterns in yt_v1:
            for all_msg in msg_split:
                if patterns in all_msg:
                    verify = 'pass'
                    break
                else:
                    verify = 'failed'
            if verify == 'pass':
                break
        if verify == 'failed':
            await message.delete()
            sent = await message.channel.send(f'**Warning**: {message.author.mention}. *You are only allowed to share YouTube contents.*')
            asyncio.create_task(msg_delete(sent))

bot.run("Token")