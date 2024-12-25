import os
import discord
from discord.ext import commands
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Discord bot setup
bot = commands.Bot(command_prefix='!')

TEMP_DIR = '/path/to/temp/files'  # Update this path to your temporary files directory

@bot.command()
async def manage_temp_files(ctx):
    """Manage temporary files by deleting them and notifying the user."""
    try:
        deleted_files = []
        for filename in os.listdir(TEMP_DIR):
            file_path = os.path.join(TEMP_DIR, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted_files.append(filename)

        if deleted_files:
            await ctx.send(f"Deleted temporary files: {', '.join(deleted_files)}")
            logging.info(f"Deleted temporary files: {', '.join(deleted_files)}")
        else:
            await ctx.send("No temporary files to delete.")
            logging.info("No temporary files to delete.")

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
        logging.error(f"Error managing temporary files: {str(e)}")

# Run the bot with your token
bot.run('YOUR_DISCORD_BOT_TOKEN')  # Replace with your Discord bot token