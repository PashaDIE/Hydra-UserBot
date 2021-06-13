# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio

from userbot import ALIVE_NAME, CMD_HELP, ICON_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern=r"^\.help(?: |$)(.*)")
async def help(event):
    """For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Masukan Perintah yang Bener Goblokkkk!!**")
            await asyncio.sleep(15)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t{ICON_HELP} "
        await event.edit(
            f"**✦ Daftar Perintah Untuk {ALIVE_NAME}-UserBot :**\n\n"
            f"{ICON_HELP}{string}{ICON_HELP}"
            "\n\n**Support @SharingUserbot**"
        )
        await event.reply(
            f"\n**Ketik Contoh** `.help afk` **Untuk Melihat Informasi Perintah**"
        )
        await asyncio.sleep(1000)
        await event.delete()
