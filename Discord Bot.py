import random
import discord
from discord.ext import commands

def IsValid(Expression):
    try:
        int(Expression)
        return True
    except:
        return False

client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print("I am ready")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")     

@client.command(aliases = ["r"])
async def roll(ctx, *, dices):
    a = dices.split("d")
    x = int(a[0])
    if IsValid(x) == Flase:
        x = 1
    y = int(a[1])
    b = []
    for i in range(x):
        z = random.randint(1, y)
        b.append(str(z))
    await ctx.send(b)
    


client.run("NzA3NjkzNDYzOTM5OTczMTYy.XrMg9w.Wahl4ZINuAHTk_sh9xN491GrKJE")