
import asyncio
import re

from pyrogram import filters
from pyrogram.types import ChatPermissions
from pyrogram.errors import ChatAdminRequired
from pyrogram.errors import FloodWait, MessageDeleteForbidden, UserNotParticipant
from JuanXMusic.utils.Databases.blacklist_db import (
    remove_bl_word,
    get_bl_words,
    add_bl_word,
    get_arg,
)
from JuanXMusic import app
from JuanXMusic.utils.errors import capture_err
from JuanXMusic.utils.admin_check import admin_filter
from JuanXMusic.misc import SUDOERS as SUDO

__MODULE__ = "Blacklist"
__HELP__ = """
/blacklisted - Get All The Blacklisted Words In The Chat.
/blacklist [WORD|SENTENCE] - Blacklist A Word Or A Sentence.
/whitelist [WORD|SENTENCE] - Whitelist A Word Or A Sentence.
"""


@app.on_message(filters.command(["addbl"]) & filters.group & admin_filter)
async def addblmessag(_, message):
    trigger = get_arg(message)
    if message.reply_to_message:
        trigger = message.reply_to_message.text or message.reply_to_message.caption

    xxnx = await message.reply(f"`Menambahakan` {trigger} `ke dalam blacklist..`")
    try:
        await add_bl_word(trigger.lower())
    except BaseException as e:
        return await xxnx.edit(f"Error : `{e}`")

    try:
        await xxnx.edit(f"{trigger} `berhasil di tambahkan ke dalam blacklist..`")
    except:
        await app.send_message(message.chat.id, f"{trigger} `berhasil di tambahkan ke dalam blacklist..`")

    await asyncio.sleep(2)
    await xxnx.delete()
    await message.delete()


@app.on_message(filters.command(["unbl"]) & filters.group & admin_filter)
async def deldblmessag(_, message):
    trigger = get_arg(message)
    if message.reply_to_message:
        trigger = message.reply_to_message.text or message.reply_to_message.caption

    xxnx = await message.reply(f"`Menghapus` {trigger} `ke dalam blacklist..`")
    try:
        await remove_bl_word(trigger.lower())
    except BaseException as e:
        return await xxnx.edit(f"Error : `{e}`")

    try:
        await xxnx.edit(f"{trigger} `berhasil di hapus dari blacklist..`")
    except:
        await app.send_message(message.chat.id, f"{trigger} `berhasil di hapus dari blacklist..`")

    await asyncio.sleep(2)
    await xxnx.delete()
    await message.delete()
