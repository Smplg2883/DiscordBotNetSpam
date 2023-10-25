import discord
from discord.ext import commands
import asyncio


class MyBot:

    def __init__(self, TOKEN, channel_id, message):
        self.TOKEN = TOKEN
        self.channel_id = channel_id
        self.message = message

        self.intents = discord.Intents.default()
        self.intents.typing = False
        self.intents.presences = False

        self.bot = commands.Bot(command_prefix='?', intents=self.intents)

    async def run_bot(self):
        @self.bot.event
        async def on_ready():
            print('Bot has connected')
            await self.send_message_with_delay(self.channel_id, self.message)

        await self.bot.start(self.TOKEN)

    async def send_message_with_delay(self, channel_id, message):
        channel = self.bot.get_channel(channel_id)

        while True:
            await channel.send(message)
            await asyncio.sleep(1.5)


 
async def run_bot(bot, token):
    try:
        await bot.start(token)
    except KeyboardInterrupt:
        await bot.close()


