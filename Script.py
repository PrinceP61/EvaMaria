class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ 👋🙂 {},
ਮੇਰਾ ਨਾਮ ਹੈ(ᴍʏ ɴᴀᴍᴇ ɪs) <a href=https://t.me/{}>{}</a>,\nਮੈਂ ਤੁਹਾਨੂੰ ਫਿਲਮਾਂ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦਾ ਹਾਂ, ਬੱਸ ਮੈਨੂੰ ਆਪਣੇ ਗਰੁੱਪ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ ਅਤੇ ਮੇਰਾ ਫਾਇਦਾ ਲਓ 😍\n(I Cᴀɴ Pʀᴏᴠɪᴅᴇ Yᴏᴜ ᴍᴏᴠɪᴇs, Jᴜsᴛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Eɴᴊᴏʏ​ 😍)</b>"""
    HELP_TXT = """<b>Hey {} ✨
ਇੱਥੇ ਮੇਰੇ ਹੁਕਮਾਂ ਲਈ ਮਦਦ.
(Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.)</b>"""
    
    ABOUT_TXT = """<b>👑Oᴡɴᴇʀ​</b>:<a href=https://t.me/p4Prnic3><b> 王子​</b></a>
<b>♯ Mʏ Nᴀᴍᴇ​</b>: {}
<b>♯Sᴘᴏɴsᴏʀᴇᴅ Bʏ​</b>: <a href=https://t.me/pb_cinemaxpro><b>Pᴜɴᴊᴀʙɪ CɪɴᴇᴍᴀXᴘʀᴏ​</b></a>"""

    IMDBB_TXT = """<b>IMDB</b>

<b>IMDB ਤੋਂ ਫਿਲਮ ਦੀ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ।</b>
<b>(Gᴇᴛ Tʜᴇ Fɪʟᴍ Iɴꜰᴏʀᴍᴀᴛɪᴏɴ Fʀᴏᴍ IMDB sᴏᴜʀᴄᴇ.​)</b>
<b>ਹੁਕਮ ਅਤੇ ਵਰਤੋਂ:</b>
<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
<b>/IMDB(ਫਿਲਮ ਦਾ ਨਾਮ)(Mᴏᴠɪᴇ Nᴀᴍᴇ​)</b>"""

    SEARCHME_TXT = """<b>ਖੋਜ ਇੰਜਣ</b>
<b>SEARCH ENGINE</b>

<b>ਵੱਖ-ਵੱਖ ਸਰੋਤਾਂ ਤੋਂ ਫਿਲਮ ਦੀ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਇੱਕ ਮੋਡੀਊਲ (Gᴇᴛ Tʜᴇ Fɪʟᴍ Iɴꜰᴏʀᴍᴀᴛɪᴏɴ Fʀᴏᴍ Vᴀʀɪᴏᴜs Sᴏᴜʀᴄᴇs.​)</b>

<b>ਹੁਕਮ ਅਤੇ ਵਰਤੋਂ (ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ):</b>
<b>•/Search (ਫਿਲਮ ਦਾ ਨਾਮ)(Mᴏᴠɪᴇ Nᴀᴍᴇ​)</b>"""

    INFOME_TXT =  """<b>ਵਿਅਕਤੀ ਦੀ ਜਾਣਕਾਰੀ
Person’s Information 

ਟੈਲੀਗ੍ਰਾਮ ਉਪਭੋਗਤਾ ਦੀ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਇੱਕ ਮੋਡੀਊਲ(A Mᴏᴅᴜʟᴇ Tᴏ Fᴇᴛᴄʜ Tᴇʟᴇɢʀᴀᴍ Usᴇʀ Iɴꜰᴏ)
   
ਹੁਕਮ ਅਤੇ ਵਰਤੋਂ(ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ):

• /Info -(ਜਵਾਬ ਵਜੋਂ ਭੇਜੋ ਅਤੇ ਕਿਸੇ ਉਪਭੋਗਤਾ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ)
• /Info - (sᴇɴᴅ ᴀs ʀᴇᴘʟʏ ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ)</b>"""

    IDME_TXT = """<b>ਗਰੁੱਪ/ਯੂਜ਼ਰ ਆਈ.ਡੀ
CHAT/USER ID 

ਟੈਲੀਗ੍ਰਾਮ ਗਰੁੱਪ ਆਈਡੀ ਅਤੇ ਯੂਜ਼ਰ ਆਈਡੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਇੱਕ ਮੋਡੀਊਲ(A Mᴏᴅᴜʟᴇ Tᴏ Fᴇᴛᴄʜ Tᴇʟᴇɢʀᴀᴍ Cʜᴀᴛ Iᴅ & Usᴇʀ Iᴅ)

ਹੁਕਮ ਅਤੇ ਵਰਤੋ(ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ):

•/Id - (ਉਪਭੋਗਤਾ ਆਈਡੀ ਲਈ ਉਪਭੋਗਤਾ ਦੇ ਸੰਦੇਸ਼ ਨੂੰ ਰਿਪਲਾਈ ਵਜੋਂ ਭੇਜੋ ਅਤੇ ਚੈਟ ਆਈਡੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਸਮੂਹ ਵਿੱਚ ਭੇਜੋ।)
• /Id - (ᴜsᴇ ᴘʀɪᴠᴀʀᴛ ꜰᴏʀ ᴜsᴇʀ ɪᴅ ᴀɴᴅ sᴇɴᴅ ᴛᴏ ɢʀᴏᴜᴘ ꜰᴏʀ ɢᴇᴛ ᴄʜᴀᴛ ɪᴅ)</b>"""

    MANUELFILTER_TXT = """<b>ਮੈਨੁਅਲ ਫਿਲਟਰ:\n\nਮੈਨੁਅਲ ਫਿਲਟਰ ਉਹ ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ ਜਦੋਂ ਉਪਭੋਗਤਾ ਕਿਸੇ ਖਾਸ ਕੀਵਰਡ ਲਈ ਸਵੈਚਲਿਤ ਜਵਾਬ ਸੈਟ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਜਦੋਂ ਵੀ ਕੋਈ ਕੀਵਰਡ ਸੁਨੇਹਾ ਮਿਲਦਾ ਹੈ ਤਾਂ Pᴜɴᴊᴀʙɪ CɪɴᴇᴍᴀXPʀᴏ Bᴏᴛ ਜਵਾਬ ਦੇਵੇਗਾ।\n\nਨੋਟ:\n1.Pᴜɴᴊᴀʙɪ CɪɴᴇᴍᴀXPʀᴏ Bᴏᴛ ਕੋਲ ਪ੍ਰਬੰਧਕੀ ਅਧਿਕਾਰ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ.\n.2.ਸਿਰਫ਼ ਪ੍ਰਸ਼ਾਸਕ ਹੀ ਚੈਟ ਵਿੱਚ ਫਿਲਟਰ ਜੋੜ ਸਕਦੇ ਹਨ.\n3.ਚੇਤਾਵਨੀ ਬਟਨਾਂ ਦੀ ਸੀਮਾ 64 ਅੱਖਰਾਂ ਦੀ ਹੈ.\n\n ਹੁਕਮ ਅਤੇ ਵਰਤੋਂ:\n•/Filter - ਚੈਟ ਵਿੱਚ ਇੱਕ ਫਿਲਟਰ ਸ਼ਾਮਲ ਕਰੋ.\n•/Filters - ਇੱਕ ਚੈਟ ਦੇ ਸਾਰੇ ਫਿਲਟਰਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ\n•/del - ਚੈਟ ਵਿੱਚ ਇੱਕ ਖਾਸ ਫਿਲਟਰ ਨੂੰ ਮਿਟਾਓ\n•/delall - ਇੱਕ ਚੈਟ ਵਿੱਚ ਪੂਰੇ ਫਿਲਟਰਾਂ ਨੂੰ ਮਿਟਾਓ (ਸਿਰਫ਼ ਚੈਟ ਮਾਲਕ)</b>\n\n<a href=https://telegra.ph/ᴊᴏɪɴ-ᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-PB-CɪɴᴇᴍᴀXᴘʀᴏ-07-29-2><b>Rᴇᴀᴅ ɪɴ ᴇɴɢʟɪsʜ​​</b></a>
"""
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
    AUTOFILTER_TXT = """<b>ਆਟੋ ਫਿਲਟਰ\n\nਨੋਟ:\n1.ਮੈਨੂੰ ਆਪਣੇ ਚੈਨਲ ਦਾ ਪ੍ਰਸ਼ਾਸਕ ਬਣਾਓ ਜੇਕਰ ਇਹ ਨਿੱਜੀ ਹੈ।\n2. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਚੈਨਲ ਵਿੱਚ ਕੈਮਰਿਪਸ, ਪੋਰਨ ਅਤੇ ਜਾਅਲੀ ਫਾਈਲਾਂ ਨਹੀਂ ਹਨ।\n3.ਹਵਾਲਿਆਂ ਦੇ ਨਾਲ ਮੇਰੇ ਲਈ ਆਖਰੀ ਸੰਦੇਸ਼ ਅੱਗੇ ਭੇਜੋ।
 ਮੈਂ ਉਸ ਚੈਨਲ ਦੀਆਂ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਆਪਣੇ ਡੀਬੀ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਾਂਗਾ।</b>\n\n<a href=https://telegra.ph/ᴊᴏɪɴ-ᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-PB-CɪɴᴇᴍᴀXᴘʀᴏ-07-29><b>Rᴇᴀᴅ ɪɴ ᴇɴɢʟɪsʜ​​</b></a>"""

    OTHERS_TXT = """<b>ਹੋਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ:</b>
<b>1.ਬੈਚ ਲਿੰਕ</b>
<b>ਇਕ ਤੋਂ ਜ਼ਿਆਦਾ ਫਾਈਲਾਂ ਦਾ ਲਿੰਕ ਬਣਾਉਣ ਲਈ ਇੱਕ ਮੋਡੀਊਲ</b>
<b>ਹੁਕਮ ਅਤੇ ਵਰਤੋਂ:</b>
<b>•/batch - ਪਹਿਲੇ ਅਤੇ ਆਖਰੀ ਸੁਨੇਹਿਆਂ ਨੂੰ ਭੇਜੋ ਅਤੇ ਲਿੰਕ ਪ੍ਰਾਪਤ ਕਰੋ</b>
<b>ਨੋਟ: ਜੇਕਰ ਤੁਹਾਡਾ ਫਾਈਲ ਸ਼ੇਅਰਿੰਗ ਚੈਨਲ ਪ੍ਰਾਈਵੇਟ ਚੈਨਲ ਹੈ, ਤਾਂ ਅੱਗੇ ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ ਉਸ ਚੈਨਲ ਵਿੱਚ ਮੈਨੂੰ ਐਡਮਿਨ ਬਣਾਓ।</b>

<b>2.ਪੋਸਟ ਲਿੰਕ</b>
<b>ਫ਼ਾਇਲ ਦਾ ਲਿੰਕ ਬਣਾਉਣ ਲਈ ਇੱਕ ਮੋਡੀਊਲ</b>
<b>ਹੁਕਮ ਅਤੇ ਵਰਤੋਂ:</b>
<b>•/Link - ਜਵਾਬ ਵਜੋਂ ਭੇਜੋ</b>

<b>3.ਸਪੈਲਿੰਗ</b>
<b>ਗੂਗਲ ਤੋਂ ਸਪੈਲਿੰਗ ਚੈੱਕ ਕਰਨ ਲਈ ਇੱਕ ਮੋਡੀਊਲ ਵਰਤੋਂ:</b>
<b>ਜੇਕਰ ਤੁਸੀਂ ਗਲਤ ਸਪੈਲਿੰਗ ਨਾਲ ਖੋਜ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਬੋਟ ਤੁਹਾਡੀ ਸਪੈਲਿੰਗ ਦੀ ਜਾਂਚ ਕਰੇਗਾ ਅਤੇ ਸਹੀ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰੇਗਾ</b>
<a href=https://telegra.ph/ᴊᴏɪɴ-ᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-PB-CɪɴᴇᴍᴀXᴘʀᴏ-07-19-2><b>Rᴇᴀᴅ ɪɴ ᴇɴɢʟɪsʜ​​</b></a>"""

    CONNECTION_TXT = """<b>ਕੁਨੈਕਸ਼ਨ:\n\n- ਫਿਲਟਰਾਂ ਦੇ ਪ੍ਰਬੰਧਨ ਲਈ ਬੋਟ ਨੂੰ ਪੀਐਮ ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ\n- ਇਹ ਸਮੂਹਾਂ ਵਿੱਚ ਸਪੈਮਿੰਗ ਤੋਂ ਬਚਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।\n\nਨੋਟ:\n1. ਸਿਰਫ਼ ਪ੍ਰਸ਼ਾਸਕ ਹੀ ਕਨੈਕਸ਼ਨ ਜੋੜ ਸਕਦੇ ਹਨ।\n2. ਮੈਨੂੰ ਤੁਹਾਡੇ ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਨਾਲ ਜੁੜਨ ਲਈ ਭੇਜੋ/ਕਨੈਕਟ ਕਰੋ\n\nਹੁਕਮ ਅਤੇ ਵਰਤੋਂ:\n•/Connect - ਕਿਸੇ ਖਾਸ ਚੈਟ ਨੂੰ ਆਪਣੇ ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਨਾਲ ਕਨੈਕਟ ਕਰੋ\n•/Disconnect - ਇੱਕ ਚੈਟ ਤੋਂ ਡਿਸਕਨੈਕਟ ਕਰੋ\n•/Connection- ਤੁਹਾਡੇ ਸਾਰੇ ਕੁਨੈਕਸ਼ਨਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ</b>\n\n<a href=https://telegra.ph/ᴊᴏɪɴ-ᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-PB-CɪɴᴇᴍᴀXᴘʀᴏ-07-29-4><b>Rᴇᴀᴅ ɪɴ ᴇɴɢʟɪsʜ​​</b></a>"""
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
