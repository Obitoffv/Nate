""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)
from config import GROUP_SUPPORT, UPDATES_CHANNEL

def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text=" ᴍᴇɴᴜ", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text=" ᴄʟᴏsᴇ", callback_data=f'cls'),
    ],
    [
      InlineKeyboardButton(text=" ɢʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"),
      InlineKeyboardButton(text=" ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="▢", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="II", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▷", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="• ᴍᴜᴛᴇ •", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="• ᴜɴᴍᴜᴛᴇ •", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data='cls'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "• ᴄʟᴏsᴇ •", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "• ɢᴏ ʙᴀᴄᴋ •", callback_data="cbmenu"
      )
    ]
  ]
)
