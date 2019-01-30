import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='SnorWare V0.3', type = 2))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!helpmij':
        await client.send_message(message.channel,'Je kan de krant opvragen dmv !robloxdev of !snorkrant. Je kan je task opvragen dmv: !tasks (writer/editor)!')
    if message.content == '!tasks':
        await client.send_message(message.channel,'Je kan je task opvragen dmv: !tasks (writer/editor)!')
    if message.content == '!tasks writer':
        await client.send_message(message.channel,'Je role heeft op dit moment geen Task.')
    if message.content == '!tasks editor':
        await client.send_message(message.channel,'Je role heeft op dit moment geen Task.')
    if message.content == '!robloxdev':
        em = discord.Embed(description='Hier kun je alle kranten downloaden! https://mega.nz/#F!HfRBGQYD!sQWl7IemfeDFbywTVEiw3w')
        em.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIL0Shg5fh-2rxGimUmuZKNz3QAZSs0T2Df9W7G6QnwV6n150U')
        await client.send_message(message.channel, embed=em)
    if message.content == '!snorkrant':
        em = discord.Embed(description='Hier kun je alle kranten downloaden! https://mega.nz/#F!zeIlwSxL!AkEGnpAzPZuyqdH-N-H2Rw')
        em.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIL0Shg5fh-2rxGimUmuZKNz3QAZSs0T2Df9W7G6QnwV6n150U')
        await client.send_message(message.channel, embed=em)
client.run('NTM3NzE1NjMzOTgzMzI0MTc1.DzN1QA.7sxbE8RR9HLATi1kPc4dx5gdeGw')
