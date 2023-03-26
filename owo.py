import discord
from discord.ext import commands

with open(".token", "r") as f:
    TOKEN = f.readline().strip()

class OwO(commands.Bot):
    def __init__(self, command_prefix):
        intents = discord.Intents.default()
        intents.message_content = True

        commands.Bot.__init__(self, command_prefix=command_prefix, intents=intents)

        self.register_commands()

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        
    def owo(str):
      while(str.find("l") != -1):
          str = str[:str.index("l")] + "w" + str[str.index("l")+1:]
      while(str.find("r") != -1):
          str = str[:str.index("r")] + "w" + str[str.index("r")+1:]
      return str
    
    def register_commands(self):
        @self.event
        async def on_message(messsage):
            await message.channel.send(owo(message.content))
            

client = OwO("!owo ")
client.run(TOKEN)
