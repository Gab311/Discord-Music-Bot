from nextcord.ext import commands
import wavelink



def hello(bot):
  @bot.command()
  async def hello(ctx):
    await ctx.reply("Hello")

def play(bot):
  @bot.command()
  async def play(ctx: commands.Context, *, search: wavelink.YouTubeTrack):
    if not ctx.voice_client:
      vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    elif not getattr(ctx.author.voice, "channel", None):
      return await ctx.reply("Please join a voice chat")
    else:
      vc: wavelink.Player = ctx.voice_client
      
    if vc.queue.is_empty and not vc.is_playing():
      await vc.play(search)
      await ctx.send("%s has been playing" % (search.title))
    else:
      await vc.queue.put_wait(search)
      await ctx.send("%s was added to the queue" % (search.title))
    vc.ctx = ctx
    setattr(vc, "loop", False)

def pause(bot):
  @bot.command()
  async def pause(ctx):
    if not ctx.voice_client:
      await ctx.send("Hey %s you are not connected to a voice channel" % (ctx.message.author.mention))
    else:
        vc: wavelink.Player = ctx.voice_client
    await vc.pause()
    await ctx.send("The music has been paused")

def resume(bot):
  @bot.command()
  async def resume(ctx):
    if not ctx.voice_client:
      await ctx.send("Hey %s you are not connected to a voice channel" % (ctx.message.author.mention))
    else:
      vc: wavelink.Player = ctx.voice_client
    await vc.resume()
    await ctx.send("The music has been resumed")

def disconnect(bot):
  @bot.command()
  async def disconnect(ctx):
    if not ctx.voice_client:
      await ctx.send("Hey %s you are not connected to a voice channel" % (ctx.message.author.mention))
    else:
      vc: wavelink.Player = ctx.voice_client
    await vc.disconnect()
    await ctx.send("%s has kicked me out of the voice channel" % (ctx.message.author.mention))

def stop(bot):
  @bot.command()
  async def stop(ctx):
    if not ctx.voice_client:
      await ctx.send("Hey %s you are not connected to a voice channel" % (ctx.message.author.mention))
    elif not getattr(ctx.author.voice, "channel", None):
      await ctx.reply("You are not currently in a voice channel")
    else:
      vc: wavelink.Player = ctx.voice_client
      
    await vc.stop()
    
    await ctx.send("The music has been stopped")
