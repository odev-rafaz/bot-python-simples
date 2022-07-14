import nextcord
from nextcord.ext import commands

class Say(commands.Cog):
  def __init__(self, bot, *args, **kwargs):
    self.bot = bot
    
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def say(self, ctx, *, msg):
    await ctx.send(msg)
    await ctx.message.delete()
    
def setup(bot):
  bot.add_cog(Say(bot))
