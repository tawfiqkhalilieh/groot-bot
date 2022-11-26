import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot_data = dict()

@client.event
async def on_ready():
    bot_data["sw"]: bool = True
    print('I am ready Loopers!!')

@client.event
async def on_message(message):
    if message.content == "switch": bot_data["sw"] = not bot_data["sw"]
    elif bot_data["sw"] and not message.author.bot: await message.reply("I am Groot!")
