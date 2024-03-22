from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZelzalMusic import app

@app.on_message(filters.incoming & filters.private, group=-2)
async def MUST_JOINN_channel(bot: Client, msg: Message):
    if not "https://t.me/mr_eirux":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("mr_eirux", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/mr_eirux".isalpha():
                link = "https://t.me/mr_eirux"
            else:
                chat_info = await bot.get_chat("mr_eirux")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"❃︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n❃︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("𝐆𝐫𝐨𝐮𝐩 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOINN chat @mr_eirux !")