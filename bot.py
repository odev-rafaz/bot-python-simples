import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')

for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")
        
for filename in os.listdir('./events'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{fn[:-3]}")
        
bot.run('token')
