import random

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Hai fatto l\\'accesso come {bot.user}")

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot ecologico, che consiglio ecofriendly posso darti? se vuoi consigli riguardo il riciclaggio dei rifiuti scrivi: rifiuti {bot.user}')



@bot.command()
async def rifiuti(ctx):
    await ctx.send(f'Ok ecco dei consigli: Ricicla materiali asciutti e puliti, riduci il volume degli imballaggi, dividi gli imballaggi composti da più materiali, gli imballaggi in legno vanno portati nelle isole ecologiche comunali {bot.user}')
    
    
   
    

@bot.command()
async def mem(ctx):
    with open('meme.jpg', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)



bot.run("MTIxMDYzMjMwNDEwMDI0OTYyMA.GWYa-c.jmwm6_v2dwZwYwREQ-QCwQqQw3pXnaMyQJGeZs")



