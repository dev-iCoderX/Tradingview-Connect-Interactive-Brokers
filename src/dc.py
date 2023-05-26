import discord
def SendMess(token, message, id):
    try:
        client = discord.Client(intents=discord.Intents.default())
        @client.event
        async def on_ready():  #  Called when internal cache is loaded
            channel = client.get_channel(id) #  Gets channel from internal cache
            await channel.send(message) #  Sends message to channel
            exit()
        client.run(token, reconnect=False, log_handler=None)  # Starts up the bot
    except:
        pass