
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, StartTime
from userbot.utils import admin_cmd
from userbot import bot
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from userbot.helpers.functions import get_readable_time
import time
import os
import datetime
#importing finished
from userbot import botnickname 
BOT = str(botnickname) if botnickname else "Angelina"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "Angelina"
tim = get_readable_time((time.time() - StartTime))
#pic 👇
PIC = os.environ.get("ALIVE_PIC")
#op 
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
#my name 👇
LEGENDX = "[{NAME}](tg://settings)"
#my bots repo 👇
REPO = "[Angelina](tg://user?id=2005063624)"
#grpup👇NAME = "[{MASTER}](tg://user?id={X})"
#yrr isko apne bot me aply krne se pehle mere se pooch lena ok
#aur aage add kruga abhi busy okay 🤔
global ghanti
X = bot.uid
MASTER = f"[{NAME}](tg://user?id={X})"
GROUP = "[SUPPORT GROUP](https://t.me/LEGEND_USERBOT_SUPPORT)"
#itna test h aur aage krte h
#test successful raha ab aage 
ALIVE = "I am Alive 😊"
OP = "I am Angelina..😁 Basically a Sample Userbot Made by My Master...😆"
EMOJI = "🔥"
