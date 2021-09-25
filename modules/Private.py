from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/d5c53489744b645f94344.jpg")
    await message.reply_text(
        f"""**Hey, ι'αм αℓιzα ρяσ вσт 🥀⚡

ι cαη ρℓαү мυsιc ιη үσυя sεxү gяσυρ's vσιc cнαт crαtє вү [cσвяα](https://t.me/XD_LIF)

αdd мε тσ үσυя gяσυρ αηd ρℓαү мυsιc ησ ℓαg αηd ησηsтσρ🔥✨!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "cяαтεя", url="https://t.me/XD_LIF")
                  ],[
                    InlineKeyboardButton(
                        "💝 sυρρσят gяσυρ 💝", url="https://t.me/MISTY_SUPORTER"
                    ),
                ],[ 
                    InlineKeyboardButton(
                        "мαт dεнкσ αdd кαяℓσ αвв👿", url="https://t.me/AXEL_MUSICBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**αℓιzα мυsιc ιs ωσякιηg**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 cσммαηds 📚", url="https://t.me/MISTY_SUPORT/46")
                ]
            ]
        )
   )


