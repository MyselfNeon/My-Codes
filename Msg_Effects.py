from pyrogram import Client, filters
from pyrogram.types import Message

# Example Effect ID (e.g., Fire effect, Sparkles, etc.)
# You have to fetch the specific string ID for the effect you want.
MSG_EFFECT = "5104841245755180586" 

@Client.on_message(filters.command("effect"))
async def send_effect_message(client: Client, message: Message):
    
    # You can apply 'message_effect_id' to reply_text, reply_photo, etc.
    await message.reply_text(
        text="This message has a special premium effect attached to it! 🎉",
        message_effect_id=MSG_EFFECT
    )
