class script(object):
    START_TXT = """Hᴇʟʟᴏ 👋🙂 {},
My Name Is(ਮੇਰਾ ਨਾਮ ਹੈ) <a href=https://t.me/{}>{}</a>, ਮੈਂ ਤੁਹਾਨੂੰ ਫਿਲਮਾਂ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦਾ ਹਾਂ, ਬੱਸ ਮੈਨੂੰ ਆਪਣੇ ਗਰੁੱਪ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ ਅਤੇ ਮੇਰਾ ਫਾਇਦਾ ਲਓ 😍

I Cᴀɴ Pʀᴏᴠɪᴅᴇ Yᴏᴜ ᴍᴏᴠɪᴇs, Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Eɴᴊᴏʏ​ 😍"""
    HELP_TXT = """Hey {} ✨
ਇੱਥੇ ਮੇਰੇ ਹੁਕਮਾਂ ਲਈ ਮਦਦ.
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs."""
    ABOUT_TXT = """⌁ Mʏ Nᴀᴍᴇ​ (ਮੇਰਾ ਨਾਮ): {}
⌁ Cʀᴇᴀᴛᴏʀ​ (ਮੈਨੂੰ ਬਨਾਉਣ ਵਾਲਾ): <a href=https://t.me/pb_cinemaxpro>Punjabi CinemaXPro</a>"""

ABOUT_TXT = """<b>👑Oᴡɴᴇʀ​</b>:<a href=https://t.me/p4Prnic3><b> 王子​</b></a>
<b>♯ Mʏ Nᴀᴍᴇ​</b>: {}
<b>♯Sᴘᴏɴsᴏʀᴇᴅ Bʏ​</b>: <a href=https://t.me/pb_cinemaxpro><b>Pᴜɴᴊᴀʙɪ CɪɴᴇᴍᴀXᴘʀᴏ​</b></a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- ਫਿਲਟਰ ਉਹ ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ ਜਦੋਂ ਉਪਭੋਗਤਾ ਕਿਸੇ ਖਾਸ ਕੀਵਰਡ ਲਈ ਸਵੈਚਲਿਤ ਜਵਾਬ ਸੈਟ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਜਦੋਂ ਵੀ ਕੋਈ ਕੀਵਰਡ ਸੁਨੇਹਾ ਮਿਲਦਾ ਹੈ ਤਾਂ Pᴜɴᴊᴀʙɪ CɪɴᴇᴍᴀXPʀᴏ Bᴏᴛ ਜਵਾਬ ਦੇਵੇਗਾ।

(Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ  Pᴜɴᴊᴀʙɪ CɪɴᴇᴍᴀXPʀᴏ Bᴏᴛ Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ​)
<b>NOTE:</b>
1. Pᴜɴᴊᴀʙɪ CɪɴᴇᴍᴀXPʀᴏ Bᴏᴛ ਕੋਲ ਪ੍ਰਬੰਧਕੀ ਅਧਿਕਾਰ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ।
Pᴜɴᴊᴀʙɪ CɪɴᴇᴍᴀXPʀᴏ Bᴏᴛ Sʜᴏᴜʟᴅ Hᴀᴠᴇ Aᴅᴍɪɴ Rɪɢʜᴛs​.
2. ਸਿਰਫ਼ ਪ੍ਰਸ਼ਾਸਕ ਹੀ ਚੈਟ ਵਿੱਚ ਫਿਲਟਰ ਜੋੜ ਸਕਦੇ ਹਨ|
Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ​
.
3. ਚੇਤਾਵਨੀ ਬਟਨਾਂ ਦੀ ਸੀਮਾ 64 ਅੱਖਰਾਂ ਦੀ ਹੈ
Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs Hᴀᴠᴇ A Lɪᴍɪᴛ Oꜰ 64 Cʜᴀʀᴀᴄᴛᴇʀs​
.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/pb_cinemaxpro)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>📂ᴛᴏᴛᴀʟ ꜰɪʟᴇs​</b>: <b>{}</b>
<b>👤ᴜsᴇʀs</b>: <b>{}</b>
<b>👥ɢʀᴏᴜᴘs</b>: <b>{}</b>
<b>🗄ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ​</b>: <b>{}</b> Mib
<b>🗃ꜰʀᴇᴇ sᴛᴏʀᴀɢᴇ</b>​: <b>{}</b> Mib"""
    LOG_TEXT_G = """#NewGroup
<b>ɢʀᴏᴜᴘ​​</b> = {}(<code>{}</code>)
<b>ᴛᴏᴛᴀʟ​ ᴍᴇᴍʙᴇʀs​​</b> = <code>{}</code>
<b>ᴀᴅᴅᴇᴅ ʙʏ​​</b> - {}
"""
    LOG_TEXT_P = """#NewUser
<b>ɪᴅ​<b> - <code>{}</code>
<b>ɴᴀᴍᴇ​</b> - <b>{}</b>
"""
