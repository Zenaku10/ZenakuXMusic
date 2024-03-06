
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text=" ᴄʟᴏsᴇ ", callback_data="close")]]
),
close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text=" ᴅᴇᴠᴇʟᴏᴩᴇʀ ", callback_data="ᴅᴇᴠᴇʟᴏᴩᴇʀ")]]
)

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb|{chat_id}""),
            InlineKeyboardButton(text="II", callback_data="pause_cb|{chat_id}""),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb|{chat_id}""),
            InlineKeyboardButton(text="▢", callback_data="end_cb|{chat_id}""),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text=" ᴄʜᴀɴɴᴇʟ ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text=" sᴜᴩᴩᴏʀᴛ ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text=" sᴏᴜʀᴄᴇ ", url="https://t.me/FoRBIDDen_FeeLinG5/4"
        ),
        InlineKeyboardButton(text=" ᴅᴇᴠᴇʟᴏᴩᴇʀ ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text=" ᴄʜᴀɴɴᴇʟ ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text=" sᴜᴩᴩᴏʀᴛ ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text=" sᴏᴜʀᴄᴇ ", url="https://t.me/FoRBIDDen_FeeLinG5/4"
        ),
        InlineKeyboardButton(text=" ᴅᴇᴠᴇʟᴏᴩᴇʀ ", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="ᴇᴠᴇʀʏᴏɴᴇ",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="sᴜᴅᴏ", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="fallen_home"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text=" sᴜᴩᴩᴏʀᴛ ", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="fallen_help"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
    ],
]
