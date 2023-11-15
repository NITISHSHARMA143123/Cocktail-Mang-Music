from pyrogram import filters

from LG import app
from LG.core.decorators.errors import capture_err
from LG.utils.http import get

__MODULE__ = "❌Rᴇᴘᴏ❌"
__HELP__ = "/repo - To Get My Github Repository Link " "And Support Group Link"


@app.on_message(filters.command("repo") & ~filters.edited)
@capture_err
async def repo(_, message):
    users = await get(
        "http://t.me/its_arryan"
    )
    list_of_users = ""
    count = 1
    for user in users:
        list_of_users += (
            f"**{count}.** [{user['login']}]({user['html_url']})\n"
        )
        count += 1

    text = f"""[BOT REPO](http://t.me/its_arryan) | [More Bots](t.me/lily_x_bots) | [Bot Repos](t.me/Lily_support_chat)
```----------------
| ᴠᴇɴᴏᴍ ᴘᴀᴘᴀ ʙᴏʟᴛᴇ |
----------------```
{list_of_users}"""
    await app.send_message(
        message.chat.id, text=text, disable_web_page_preview=True
    )
