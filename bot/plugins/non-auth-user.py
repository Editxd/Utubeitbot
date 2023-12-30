import logging

from pyrogram import filters as Filters
from pyrogram.types import Message

from ..utubebot import UtubeBot
from ..config import Config


log = logging.getLogger(__name__)


@UtubeBot.on_message(
    Filters.private & Filters.incoming 
)
async def (c: UtubeBot, m: Message):
    await m.delete(False)
    log.info(
        f"{Config.AUTH_USERS} Unauthorised user {m.chat} contacted. Message {m} deleted!!"
    )
