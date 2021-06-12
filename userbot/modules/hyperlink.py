# Code By @Mrismanaziz
# FORM Man-Userbot
# t.me/SharingUserbot

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^.hl(.*)")
async def _(event):
    if event.fwd_from:
        return
    string = event.pattern_match.group(1)
    strings = string.split()
    link = strings[-1]
    strings = strings[:-1]
    string = " ".join(strings)
    output = f"[{string}]({link})"
    await event.edit(output)


CMD_HELP.update(
    {
        "hl": "**Plugin : **`hl`\
        \n\n  •  **Syntax :** `.hl <text> <link>`\
        \n  •  **Result : **hyperlink text dengan userbot seperti modules mentions\
    "
    }
)
