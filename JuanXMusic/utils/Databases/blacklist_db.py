
from typing import List
from pyrogram.types import Message
from pyrogram.enums import MessageEntityType
from JuanXMusic.utils.database import mongodb

blackword = mongodb["BLACKWORDSs"]


def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


async def get_bl_words() -> list:
    filters = await blackword.find_one({"filter": "filter"})
    if not filters:
        return []
    return filters["filters"]

async def add_bl_word(trigger) -> bool:
    x = trigger.lower()
    filters = await get_bl_words()
    filters.append(x)
    await blackword.update_one({"filter": "filter"}, {"$set": {"filters": filters}}, upsert=True)
    return True

async def remove_bl_word(trigger) -> bool:
    x = trigger.lower()
    filters = await get_bl_words()
    filters.remove(x)
    await blackword.update_one({"filter": "filter"}, {"$set": {"filters": filters}}, upsert=True)
    return True
