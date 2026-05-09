from pyrogram import Client, filters
from pyrogram.types import Message, BotCommand

# Put your owner ID here to restrict usage
OWNER_ID = 123456789 

# Format: command - Description
COMMANDS_TEXT = """
start - 🚀 Start the bot
help - ❓ Get help and instructions
settings - ⚙️ Customize your bot settings
ping - 🏓 Check bot latency
"""

@Client.on_message(filters.command("setcmd") & filters.user(OWNER_ID))
async def set_commands(client: Client, message: Message):
    commands = []
    
    # Parse the text block into commands
    for line in COMMANDS_TEXT.strip().split("\n"):
        if "-" in line:
            cmd, desc = line.split("-", 1)
            commands.append(BotCommand(cmd.strip(), desc.strip()))

    if not commands:
        return await message.reply_text("❌ No commands found in the configuration list.")

    try:
        # Push the commands to Telegram
        await client.set_bot_commands(commands)
        await message.reply_text(f"✅ **Success!** Updated {len(commands)} commands.")
    except Exception as e:
        await message.reply_text(f"❌ **Error:** `{e}`")
