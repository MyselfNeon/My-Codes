import random
from pyrogram import Client, filters
from pyrogram.types import Message

# List of allowed reactions
REACTIONS = [
    "🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩",
    "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡",
    "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"
]

@Client.on_message(filters.command("start") & filters.private)
async def auto_react_handler(client: Client, message: Message):
    # Try to react to the message with a random emoji
    try:
        await message.react(
            emoji=random.choice(REACTIONS),
            big=True # Set to True for the larger animated effect
        )
    except Exception as e:
        print(f"Reaction failed: {e}")
        
    await message.reply_text("Hello! I successfully reacted to your message.")
