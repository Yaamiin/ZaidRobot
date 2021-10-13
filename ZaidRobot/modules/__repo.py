import os
from pyrogram import Client, filters
from pyrogram.types import *

from ZaidRobot.conf import get_str_key
from ZaidRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/b013a5f2c29e18d85a163.mp4) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [Mukesh Solanki](t.me/mkspali) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @BotMasterOfficial «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ ʀᴇᴘᴏꜱɪᴛᴏʀʏ🔥", url=f"https://github.com/BotMasterOfficial/ZaidRobot"),
        InlineKeyboardButton(" ᴊᴏɪɴ 💫", url=f"https://t.me/BotMasterOfficial"),
      ],[
        InlineKeyboardButton("ᴢᴀɪᴅ ᴏᴡɴᴇʀ ❣️", url="https://t.me/mkspali"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/BotMasterOfficial"),
      ],[
        InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ☑️", url="https://t.me/BotMaster_mkspali"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ➡️", url="https://t.me/mkspali"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
