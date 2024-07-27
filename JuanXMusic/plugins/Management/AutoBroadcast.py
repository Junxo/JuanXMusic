import asyncio
import datetime
from JuanXMusic import app
from pyrogram import Client
from JuanXMusic.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_IMG_URL = "https://telegra.ph//file/658b1b51b6e16fd600d5c.jpg"


MESSAGE = f"""Hi Saya Bot Musik Yang Bisa Menghibur Anda"

🛒𝗦𝗧𝗢𝗥𝗘 » [✘ ᴄʟɪᴄᴋ ᴍᴇ ✘](https://t.me/junastorenih) <√ᴊᴏɪɴ ɢʀᴏᴜᴘ.^>

🚩 ʙᴏᴛ »|| @{app.username}||"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("» ᴀᴅᴅ ᴍᴇ «", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                    await asyncio.delete(20)
                except Exception as e:
                    pass  
    except Exception as e:
        pass  

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(5000)  
        
asyncio.create_task(continuous_broadcast())
