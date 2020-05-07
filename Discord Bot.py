import random
import discord
import Bot
from discord.ext import commands


client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print("I am ready")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")     

@client.command(aliases = ["r"])
async def roll(ctx, *, dices):
    f = 0
    for i in range (len(dices)):
        d = "d"
        w = dices[i]
        if w == d:
            f += 1
    if f >= 2:
        await ctx.send("Nauč sa hádzať kockami, prečo tam máš dve d?")
    a = dices.split("d")
    x = a[0]
    if x == "":
        x = 1
    else:
        x = int(a[0])
    y = int(a[1])
    b = ["Takéto hody si mal: "]
    c = 0
    for i in range(x):
        z = random.randint(1, y)
        c += z
        b.append(str(z))
    e =""
    for i in range(len(b)):
        if b[i] == "20" and x == 20:
            e += "***__"
        if b[i] == "1":
            e += "***__"
        e += b[i]
        if b[i] == "20" and x == 20:
            e += "__***"
        if b[i] == "1":
            e += "__***"
        e += "  "
    e += "\nIch súčet je: "
    e += str(c)
    await ctx.send(e)
    


client.run("NzA3NjkzNDYzOTM5OTczMTYy.XrNIeQ.RN40fBfs28vs4eNuz6Jwo2K7wnw")