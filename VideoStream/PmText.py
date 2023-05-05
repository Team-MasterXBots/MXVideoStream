from time import time
from datetime import datetime
from helpers.filters import command
from helpers.decorators import sudo_users_only
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)
#Code Edited By TurdusMaximus
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)




from config import ASSISTANT_NAME, BOT_USERNAME
from plugins.tr import *
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("「 ᴄᴏᴍᴍᴀɴᴅs | ʜᴇʟᴘ 」", callback_data="help"),
            ],
            [

                 InlineKeyboardButton("「 ɪɴғᴏ 」", callback_data="about"),
            ],
            [
                InlineKeyboardButton("「 ꪑ᥊ ᥇ꪮꪻᦓ 」", url=f"https://t.me/Master_X_Updates"),
                InlineKeyboardButton("「 ᥇ꫀᦓꪻ ᠻ᥅꠸ꫀꪀᦔᦓ 」", url=f"https://t.me/Best_Friends15"),
            ],
            [
               InlineKeyboardButton("「•ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ•」 ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT,
          reply_markup=reply_markup
       )
   else:
      await message.reply(f"** 🍓 ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴇʙᴇ!! ~ @Master_X_Updates**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("「 ʙᴀᴄᴋ 」", callback_data="start"),
                InlineKeyboardButton ("「 sᴜᴘᴘᴏʀᴛ 」", url=f"https://t.me/Best_Friends15"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("「 ʙᴀᴄᴋ 」", callback_data="start"),
                InlineKeyboardButton ("「 sᴜᴘᴘᴏʀᴛ 」", url=f"https://t.me/Best_Friends15"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    #Inline Keyboard By Maximus
    elif query.data=="start":
        buttons = [
           [
                InlineKeyboardButton("「 ᴄᴏᴍᴍᴀɴᴅs | ʜᴇʟᴘ 」", callback_data="help"),
            ],
            [
                
                 InlineKeyboardButton("「 ɪɴғᴏ 」", callback_data="about"),
            ],
            [
                InlineKeyboardButton("「 ꪑ᥊ ᥇ꪮꪻᦓ 」", url=f"https://t.me/Master_X_Updates"),
                InlineKeyboardButton("「 ᥇ꫀᦓꪻ ᠻ᥅꠸ꫀꪀᦔᦓ 」", url=f"https://t.me/Best_Friends15"),
            ],
            [
               InlineKeyboardButton("「•ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ•」", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
