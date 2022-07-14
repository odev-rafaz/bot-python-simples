import nextcord
import time
from nextcord.ext import commands

class Ping(commands.Cog):
  def __init__(self, bot, *args, **kwargs):
    self.bot = bot
  
  @commands.command()
  async def ping(self, ctx):
    i = time.time()
    f = time.time()
    p = i - f
    
    await ctx.send(f':pong: Pong!\n\n:robot: API: {round(p)}ms')
    
def setup(bot):
  bot.add_cog(Ping(bot))
