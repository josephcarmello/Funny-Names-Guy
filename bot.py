import disnake
from disnake.ext import commands
import re
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
JLEES_CHANNEL_ID = int(os.getenv("JLEES_CHANNEL_ID"))
COMMAND_PROMPT_CHANNEL_ID = int(os.getenv("COMMAND_PROMPT_CHANNEL_ID"))

IMAGE_URL_REGEX = r"(https?://[^\s]+(?:\.jpg|\.jpeg|\.png|\.gif|\.bmp|\.webp))"

intents = disnake.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.InteractionBot(intents=intents)  # No command prefix

@bot.event
async def on_ready():
    print(f"Bot is online and logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id in {JLEES_CHANNEL_ID, COMMAND_PROMPT_CHANNEL_ID}:
        target_channel_id = (
            JLEES_CHANNEL_ID if message.channel.id == COMMAND_PROMPT_CHANNEL_ID else COMMAND_PROMPT_CHANNEL_ID
        )
        target_channel = bot.get_channel(target_channel_id)
        if not target_channel:
            print(f"Could not find target channel ID: {target_channel_id}")
            return

        attribution = f"**Message from `{message.author.display_name}` in `{message.guild.name}`:**"

        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type and attachment.content_type.startswith("image/"):
                    await target_channel.send(
                        content=f"{attribution}\n{message.content}",
                        file=await attachment.to_file(),
                    )

        image_links = re.findall(IMAGE_URL_REGEX, message.content)
        if image_links:
            links_text = "\n".join(image_links)
            await target_channel.send(content=f"{attribution}\n{message.content}\n{links_text}")

bot.run(BOT_TOKEN)
