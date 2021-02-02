import discord
import time
import pyautogui
import datetime
import asyncio
import time

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as', client.user)
    channel = client.get_channel(796976003971809305) #change channel id
    await channel.send('Bot has logged on - Enjoy :)')
    client.loop.create_task(main()) #Loop main

async def main():
    await client.wait_until_ready()
    channel = client.get_channel(796976003971809305) #change channel id
    await channel.send('Bot is getting screenshots')
    while not client.is_closed():
        i=0
        while(True):
            try:
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r'C:\Users\Calvin\Documents\Screenshots\ss1.png') #location to save screenshot
                print('screenshot taken')
                await channel.send(file=discord.File(r'C:\Users\Calvin\Documents\Screenshots\ss1.png')) #send screenshot
                print('screenshot sent')
                await asyncio.sleep(60) # Change timer for repeat cycle e.g 60 = 60 seconds

            except IOError: #handle error
                time.sleep(1)
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r'C:\Users\Calvin\Documents\Screenshots\ss1.png') #location to save screenshot
                print('screenshot taken')
                await channel.send(file=discord.File(r'C:\Users\Calvin\Documents\Screenshots\ss1.png')) #send screenshot
                print('screenshot sent')
                await asyncio.sleep(60) # Change timer for repeat cycle e.g 60 = 60 seconds
            i+=1

client.run('<enter bot id here>') #Remove arrows & enter your bot ID


