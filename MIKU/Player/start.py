import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from MIKU.main import Test, bot as Client
from config import START_PIC, UPDATES_CHANNEL, GROUP_SUPPORT, BOT_USERNAME


ALIVE_PIC = START_PIC
HOME_TEXT = " **ʜᴇʟʟᴏ [{}](tg://user?id={})** \n\n**ᴛʜɪꜱ ʙᴏᴛ ʜᴀꜱ ᴀ ʟᴏᴛ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ʙᴀꜱᴇᴅ ᴏɴ ᴀ.ɪ ᴀɴᴅ ʜɪɢʜ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ ᴏꜰ ꜱᴏɴɢꜱ.** **ᴀɴᴅ ᴛʜɪꜱ ᴍᴜꜱɪᴄ + ꜱᴘᴀᴍ + ᴠᴄʀᴀɪᴅ ʙᴏᴛ ꜱᴍᴀꜱʜ ᴛʜᴇᴍ ᴏꜰ ᴀʟʟ ꜱᴇʀᴠᴇʀ ᴏꜰ ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀꜱꜱ **"
HELP_TEXT = """ᴛʜɪꜱ ʙᴏᴛ ʜᴀꜱ ᴀ ʟᴏᴛ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ʙᴀꜱᴇᴅ ᴏɴ ᴀ.ɪ ᴀɴᴅ ʜɪɢʜ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ᴏꜰ ꜱᴏɴɢꜱ.ᴀɴᴅ ᴛʜɪꜱ ᴍᴜꜱɪᴄ + ꜱᴘᴀᴍ + ᴠᴄʀᴀɪᴅ ʙᴏᴛ ꜱᴍᴀꜱʜ ᴛʜᴇᴍ ᴏꜰ ᴀʟʟ ꜱᴇʀᴠᴇʀ ᴏꜰ ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀꜱꜱ 
» **sᴇᴛᴜᴘ ɢᴜɪᴅᴇ** :

\u2022 sᴛᴀʀᴛ ᴀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
\u2022 ᴀᴅᴅ ʙᴏᴛ ᴀɴᴅ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ɪɴ ᴄʜᴀᴛ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
\u2022 ᴅᴏɴᴇ sᴇᴛᴜᴘ ᴘʀᴏᴄᴇss ʀᴇᴀᴅ ᴄᴏᴍᴍᴀɴᴅs ʙᴇʟᴏᴡ.
"""



USER_TEXT = """
» **ᴜsᴇʀs ᴄᴏᴍᴍᴀɴᴅs** :

\u2022 /play <Query> ᴛᴏ ᴘʟᴀʏ ᴀ sᴏɴɢ.
\u2022 /vplay <Query> ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ.
\u2022 /stream <Live Url> ᴛᴏ ᴘʟᴀʏ ʟɪᴠᴇ sᴛʀᴇᴀᴍs\n /song ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀ ᴀᴜᴅɪᴏ ғɪʟᴇ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ. \n /video ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ\n /lyric ᴛᴏ ғɪɴᴅ ʟʏʀɪᴄs.
"""

SPAM_TEXT = """
» **sᴘᴀᴍ ʜᴇʟᴘ ᴀᴅᴍɪɴs ᴏɴʟʏ** :

\u2022 /spam <Count> ᴛᴇxᴛ ᴛᴏ sᴘᴀᴍ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ.
\u2022 /fspam <Count> ᴛᴇxᴛ ғᴏʀ sᴘᴀᴍᴍɪɴɢ.
\u2022 /delayspam <Count> ᴛᴇxᴛ ғᴏʀ sᴘᴀᴍᴍɪɴɢ.
"""

RAID_TEXT = """
» **ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅs sᴜᴅᴏ ᴏɴʟʏ** :

\u2022 /vcraid <chatid> - ɢᴜᴠᴇ ᴀ ᴄʜᴀᴛ ɪᴅ ᴇʟsᴇ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴠᴏɪᴄᴇ ʀᴀɪᴅ.
\u2022 /vraid <chatid + ʀᴇᴘʟʏ ᴛᴏ ᴠɪᴅᴇᴏ ғɪʟᴇ> - ᴛᴏ ʀᴀɪᴅ ᴠɪᴅᴇᴏ.
\u2022 /raidpause - ᴛᴏ ᴘᴀᴜsᴇ ʀᴀɪᴅ.
\u2022 /raidresume ᴛᴏ ʀᴇsᴜᴍᴇ ʀᴀɪᴅ.
\u2022 /raidend <chatid> ᴛᴏ ᴇɴᴅ ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ ʀᴀɪᴅ.
"""

ADMIN = """
» **ᴀᴅᴍɪɴs ᴄᴏᴍᴍᴀɴᴅs** :

\u2022 /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ.
\u2022 /end ᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍɪɴɢ.
\u2022 /pause ᴛᴏ ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ.
\u2022 /resume ᴛᴏ ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ.
\u2022 /volume ᴛᴏ sᴇᴛ ᴠᴏʟᴜᴍᴇ.
\u2022 /skip ᴛᴏ sᴋɪᴘ ᴛʀᴀᴄᴋs.
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton(" ᴏᴡɴᴇʀ", url="https://t.me/Mr_nack_nack"),
                InlineKeyboardButton(" ᴜꜱᴇʀꜱ", callback_data="users"),
            ],
            [
                InlineKeyboardButton(" ʀᴀɪᴅ", callback_data="raid"),
                InlineKeyboardButton(" sᴘᴀᴍ", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("» ʙᴀᴄᴋ «", callback_data="home"),
                InlineKeyboardButton(" ᴄʟᴏꜱᴇ ", callback_data="close"),
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

    elif query.data=="home":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton(" sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(" ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/Miku_updates"),
            ],
            [
                InlineKeyboardButton(" 【V๏ɪ፝֟𝔡】◈Network◈", url="https://t.me/VoidxNetwork"),
                InlineKeyboardButton(" ᴏᴡɴᴇʀ✨", url="https://t.me/Mr_nack_nack"),
            ],
            [
                InlineKeyboardButton(" ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="users":
        buttons = [
            [
                InlineKeyboardButton("» ʙᴀᴄᴋ «", callback_data="help"),
                InlineKeyboardButton(" ᴄʟᴏꜱᴇ ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                USER_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="admins":
        buttons = [
            [
                InlineKeyboardButton("» ʙᴀᴄᴋ «", callback_data="help"),
                InlineKeyboardButton(" ᴄʟᴏꜱᴇ ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(ADMIN, reply_markup=reply_markup)
        except MessageNotModified:
            pass

    elif query.data=="raid":
        buttons = [
            [
                InlineKeyboardButton("» ʙᴀᴄᴋ «", callback_data="help"),
                InlineKeyboardButton(" ᴄʟᴏꜱᴇ ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                RAID_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="spam":
        buttons = [
            [
                InlineKeyboardButton("» ʙᴀᴄᴋ «", callback_data="help"),
                InlineKeyboardButton(" ᴄʟᴏꜱᴇ ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                SPAM_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

@Client.on_message(filters.command(["void"]) & filters.private)
async def void(client: Client, message: Message):
    PHOTO="https://telegra.ph/file/e5808adf6d1bc748d6440.jpg"
    Text= f"""
Welcome to [【V๏ɪ፝֟𝔡】Network](https://t.me/voidxnetwork)
━━━━━━━━━━━━━━━━━━━━━━
✪ ᴠᴏɪᴅ ɪꜱ ᴀɴ ᴀɴɪᴍᴇ ʙᴀꜱᴇᴅ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴀ ᴍᴏᴛɪᴠᴇ ᴛᴏ ꜱᴘʀᴇᴀᴅ ʟᴏᴠᴇ ᴀɴᴅ ᴘᴇᴀᴄᴇ ᴀʀᴏᴜɴᴅ ᴛᴇʟᴇɢʀᴀᴍ.
✪ ɢᴏ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴊᴏɪɴ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ ɪꜰ ɪᴛ ᴅʀᴀᴡꜱ ʏᴏᴜʀ ᴀᴛᴛᴇɴᴛɪᴏɴ. 
━━━━━━━━━━━━━━━━━━━━━━
"""
    await message.reply_photo(
        photo=PHOTO, caption=Text,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】Network", url="https://t.me/VoidXNetwork")],
                    [
                    InlineKeyboardButton(text="【ᴜꜱᴇʀᴛᴀɢ】", url="https://t.me/VoidxNetwork/136"),
                    InlineKeyboardButton(text="【ɪɴᴅᴇx】", url="https://t.me/VoidxNetwork/15")
                    ],
                ]
            ),
        )
    
@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    get_me = await client.get_me()
    USERNAME = get_me.username
    buttons =  [
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton(" sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(" ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/Miku_updates"),
            ],
            [
                InlineKeyboardButton(" 【V๏ɪ፝֟𝔡】◈Network◈", url="https://t.me/VoidxNetwork"),
                InlineKeyboardButton(" ᴏᴡɴᴇʀ✨", url="https://t.me/Mr_nack_nack"),
            ],
            [
                InlineKeyboardButton(" ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=START_PIC, caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client: Client, message: Message):
    get_me = await client.get_me()
    self.username = get_me.username
    buttons =  [
            [
                InlineKeyboardButton(" ᴏᴡɴᴇʀ", url="https://t.me/Mr_nack_nack"),
                InlineKeyboardButton(" ᴜꜱᴇʀꜱ", callback_data="users"),
            ],
            [
                InlineKeyboardButton(" ʀᴀɪᴅ", callback_data="raid"),
                InlineKeyboardButton(" sᴘᴀᴍ", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("» ʙᴀᴄᴋ «", callback_data="home"),
                InlineKeyboardButton(" ᴄʟᴏꜱᴇ ", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=ALIVE_PIC, caption=HELP_TEXT, reply_markup=reply_markup)
