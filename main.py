import discord

# 这里 proxy 根据你自己的需要进行填写，也可以不用填
bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("机器人上线了")
 

@bot.slash_command(name = "hi", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")
    
bot.run('MTIyNDkxMjAwMzE2MDYwODc3OA.GKJSf3.ZccngdFIKPTyUrdp1ESr5tzrrj7C-MsvJbHx-o')
