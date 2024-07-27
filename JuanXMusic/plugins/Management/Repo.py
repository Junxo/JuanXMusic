from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from JuanXMusic import app as bot
import requests
from config import BOT_USERNAME
from JuanXMusic.utils.errors import capture_err

start_txt = """**
➤ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴡᴏʀʟᴅ ᥫᩣ
 
 ⦿ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ɴ ᴠᴘs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ !
 
 ⦿ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ !
 
 ⦿ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ !
 
 ⦿ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴅᴍ ᴍᴇ !
**"""

@bot.on_message(filters.command(["repo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⦿ ᴀᴅᴅ ᴍᴇ ⦿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="."),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", url="."),
        ],
        [
          InlineKeyboardButton("ᴠ1 ᴍᴜsɪᴄ", url=f"."),
          InlineKeyboardButton("︎ᴠ2 ᴍᴜsɪᴄ", url=f"."),
        ],
        [
          InlineKeyboardButton("ᴍᴀñᴀɢᴇᴍᴇɴᴛ", url=f"."),
          InlineKeyboardButton("ᴄʜᴀᴛ ʙᴏᴛ", url=f"."),
        ],
        [
          InlineKeyboardButton("sᴛʀɪɴɢ ʙᴏᴛ", url=f"."),
          InlineKeyboardButton("ᴅᴘᴢ sᴛᴏʀᴇ", url=f"."),
        ],
        [
          InlineKeyboardButton("ᴄᴄ ᴄʜᴀᴛ", url="."),
          InlineKeyboardButton("ᴀʟᴏɴᴇ ɢʀᴏᴜᴘ", url=f"."),
        ],
        [
          InlineKeyboardButton("ʟᴀᴛᴇ ɴɪɢʜᴛ︎", url=f"."),
          InlineKeyboardButton("ᴅᴜɴɪʏᴀ", url=f"."),
        ],
        [
          InlineKeyboardButton("ᴅɪʟ ғᴇᴇʟɪɴɢs", url=f"."),
          InlineKeyboardButton("ʟᴏᴠᴇ ғᴇᴇʟɪɴɢs", url=f"."),
        ],
        [
          InlineKeyboardButton("ᴅɪʟ sᴜᴘᴘᴏʀᴛ", url=f"."),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/d3e94fa78cb489c1effbd.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
    )



#-------------------------------------------------------#


@bot.on_message(filters.command("repo", prefixes="@"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/stkeditz/AAROHIxMUSICv2/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[ʀᴇᴘᴏ](https://github.com/stkeditz/AAROHIxMUSICv2) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/alonegroup121)
| ᴄᴏɴᴛʀɪʙᴜᴛᴏʀs |
----------------
{list_of_users}"""
        await bot.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await bot.send_message(message.chat.id, text="Failed to fetch contributors.")

