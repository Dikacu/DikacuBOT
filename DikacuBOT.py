import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk


bot = commands.Bot(command_prefix='Dkc!')

print (discord.__version__)



@bot.event
async def on_ready():
    print ("DIKACU BOT HAZIR")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_status(game=discord.Game(name='Dkc!help'))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!!")
    print ("user has pinged")




    
    
    

    

@bot.command(pass_context=True)
async def low(ctx,kisi):
    await bot.say(kisi+" tam bir low :poop:")
        
@bot.command(pass_context=True)
async def kolsuz(ctx,kisi):
    await bot.say(kisi+" tam bir kolsuz :poop:")

@bot.command(pass_context=True)
@commands.has_role("0")
async def dokkaebi(ctx,time):
    for i in range(int(time)):
      await  bot.say("@everyone")
       
      
@bot.command(pass_context=True)
@commands.has_role("0")
async def say(ctx,word,kere):
     for i in range(int(kere)):
      await  bot.say(word)
    
@bot.command(pass_context = True)
@commands.has_role("0")
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)



@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{} Hakkındakiler ".format(user.name), description="Bulabildiklerim..", color=0x00ff00)
    embed.add_field(name="Kullanıcı adı", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Durumu", value=user.status, inline=True)
    embed.add_field(name="En yüksek rol", value=user.top_role)
    embed.add_field(name="Katıldı", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Bulabildiklerim", color=0x00ff00)
    embed.set_author(name="-SERVER-")
    embed.add_field(name="Server adı", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Rol sayısı", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Uye sayısı", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("0")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Görüşmek üzere , {}. XD".format(user.name))
    await bot.kick(user)



bot.run(token)
