# Funny Names Guy

This bot forwards images and image links posted in the `#funny-names` channel of one Discord server to the `#funny-names` channel of another server. 
It uses the `disnake` library and listens for image uploads or links in specific channels.

## Features
- Monitors designated channels for image uploads and image links.
- Forwards the images and links to the corresponding channel in another server.
- Preserves the message content and provides attribution to the original sender.

## Prerequisites
1. Python 3.11 or later.
2. A bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
3. `disnake` library installed.
4. `.env` file for configuration.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/josephcarmello/Funny-Names-Guy
   cd Funny-Names-Guy
   ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add the following variables:
    ```env
    BOT_TOKEN=your-bot-token
    JLEES_CHANNEL_ID=channel-id-for-jlees-server
    COMMAND_PROMPT_CHANNEL_ID=channel-id-for-command-prompt-server
    ```

    - Replace `your-bot-token` with your Discord bot token.
    - Replace `channel-id-for-jlees-server` with the channel ID for the `#funny-names` channel in "JLees Discord".
    - Replace `channel-id-for-command-prompt-server` with the channel ID for the `#funny-names` channel in "Command Prompt".

4. Run the bot:
    ```bash
    python bot.py
    ```

## Configuration
- Make sure the bot has **Message Read**, **Message Send**, and **Message Attachments** permissions in the monitored channels.
- To find channel IDs, enable Developer Mode in Discord under **User Settings > Advanced**, then right-click on a channel and select **Copy ID**.

## How It Works
1. The bot monitors two specific channels in the configured Discord servers.
2. When an image or image link is detected in one channel, it forwards it to the other channel.
3. The forwarded message includes:
    - The original message content.
    - Attributed information about the sender and server.
    - Attached images or links.

## Troubleshooting
- If the bot doesn’t start, verify the `.env` file and ensure the bot token and channel IDs are correct.
- Ensure the bot has sufficient permissions in the designated channels.
- Check the logs for any error messages.
