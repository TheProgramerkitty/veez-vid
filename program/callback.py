# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""β¨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
π­ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Κα΄α΄ α΄α΄Ι΄ α΄sα΄ α΄α΄ α΄Κα΄Κ α΄α΄sΙͺα΄ α΄Κ α΄ Ιͺα΄α΄α΄s ΙͺΙ΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ α΄ Ιͺα΄α΄α΄ α΄Κα΄α΄.!**

π‘ **κ°ΙͺΙ΄α΄ α΄α΄α΄ α΄ΚΚ α΄Κα΄ Κα΄α΄'s α΄α΄α΄α΄α΄Ι΄α΄s α΄Ι΄α΄ Κα΄α΄‘ α΄Κα΄Κ α΄‘α΄Κα΄ ΚΚ α΄ΚΙͺα΄α΄ΙͺΙ΄Ι’ α΄Ι΄ α΄Κα΄ [β€](https://telegra.ph/file/b3d4b8e9ee627436c3684.jpg) π α΄α΄α΄α΄α΄Ι΄α΄s Κα΄α΄α΄α΄Ι΄!**

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Aα΄α΄ Mα΄ Tα΄ UΚ GΚα΄α΄α΄ π",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("AΚα΄α΄α΄ Mα΄ π₯°", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("Cα΄α΄α΄α΄Ι΄α΄s π", callback_data="cbcmds"),
                    
                ],
                [
                    InlineKeyboardButton(
                        "β€οΈ π­ππ πΎππππππ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "π­ππ πππππππ π", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Dα΄α΄ Κα΄α΄α΄Κ π¨βπ»", url="https://t.me/AttitudefuckerXD"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""Κα΄α΄ Ι΄α΄α΄α΄ α΄α΄ α΄Ι΄α΄α΄‘ α΄Κα΄α΄α΄ α΄α΄ ? 

π¨βπ» MΚ Mα΄sα΄α΄Κ: [ππππππππ πΈπππ](https://t.me/Attitude_king_vj)
πΎ Bα΄α΄ Vα΄ΚsΙͺα΄Ι΄: `v0.6.2`\nπ₯ PΚΚα΄Ι’Κα΄α΄ Vα΄ΚsΙͺα΄Ι΄: `1.4.1`
π PΚα΄Κα΄Ι΄ Vα΄ΚsΙͺα΄Ι΄: `3.10.2`
β¨ PΚα΄Ι’α΄α΄ΚΚs Vα΄ΚsΙͺα΄Ι΄: `0.8.5`
π Sα΄α΄α΄α΄s: `Running`

α΄ΚΙͺα΄α΄ α΄α΄α΄α΄α΄Ι΄α΄s Κα΄α΄α΄α΄Ι΄ α΄α΄ α΄Ι΄α΄α΄‘ α΄Κ α΄ΚΚ α΄α΄α΄α΄α΄Ι΄α΄s!

ΙͺΙ΄α΄ Ιͺα΄α΄ @{ASSISTANT_NAME} α΄α΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ α΄Κ α΄Κα΄α΄ /α΄sα΄ΚΚα΄α΄α΄α΄ΙͺΙ΄ α΄α΄ ΙͺΙ΄α΄ Ιͺα΄α΄ Κα΄Κ (α΄Ι΄κ°α΄Κα΄α΄Ι΄α΄α΄α΄ΚΚ α΄Κα΄ α΄sα΄ΚΚα΄α΄ α΄‘ΙͺΚΚ α΄α΄ΙͺΙ΄α΄α΄ ΚΚ Ιͺα΄sα΄Κκ° α΄‘Κα΄Ι΄ Κα΄α΄ α΄Κα΄α΄ /α΄Κα΄Κ (sα΄Ι΄Ι’ Ι΄α΄α΄α΄) α΄Κ /α΄ α΄Κα΄Κ (sα΄Ι΄Ι’ Ι΄α΄α΄α΄)).

π‘ If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""β¨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

Β» Choose the menu below to read the explanation & see the list of available Commands !

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("π·π» Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("π§π» Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("π Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("π Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""π? here is the basic commands:

Β» /play (song name/link) - play music on video chat
Β» /vplay (video name/link) - play video on video chat
Β» /vstream - play live video from yt live/m3u8
Β» /playlist - show you the playlist
Β» /video (query) - download video from youtube
Β» /song (query) - download song from youtube
Β» /lyric (query) - scrap the song lyric
Β» /search (query) - search a youtube video link

Β» /ping - show the bot ping status
Β» /uptime - show the bot uptime status
Β» /alive - show the bot alive info (in Group only)

β‘οΈ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""π? here is the admin commands:

Β» /pause - pause the stream
Β» /resume - resume the stream
Β» /skip - switch to next stream
Β» /stop - stop the streaming
Β» /vmute - mute the userbot on voice chat
Β» /vunmute - unmute the userbot on voice chat
Β» /volume `1-200` - adjust the volume of music (userbot must be admin)
Β» /reload - reload bot and refresh the admin data
Β» /userbotjoin - invite the userbot to join group
Β» /userbotleave - order userbot to leave from group

β‘οΈ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""π? here is the sudo commands:

Β» /gban (`username` or `user id`) - for global banned people
Β» /ungban (`username` or `user id`) - for un-global banned people
Β» /speedtest - run the bot server speedtest
Β» /sysinfo - show the system information
Β» /update - update your bot to latest version
Β» /restart - restart your bot
Β» /leaveall - order userbot to leave from all group
Β» /leavebot (`chat id`) - order bot to leave from the group you specify

Β» /eval - execute any code
Β» /sh - run any command

Β» /broadcast (`message`) - send a broadcast message to all groups entered by bot
Β» /broadcast_pin (`message`) - send a broadcast message to all groups entered by bot with the chat pin

β‘ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("π Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"βοΈ **Settings of** {chat}\n\nβΈ : pause stream\nβΆοΈ : resume stream\nπ : mute userbot\nπ : unmute userbot\nβΉ : stop stream",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("β nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("π‘ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()
