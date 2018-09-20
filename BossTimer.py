import discord
from discord.ext import commands
import asyncio
import datetime
from datetime import datetime
import pytz

BotToken = "" #TODO Replace with your own bot token
serverID = 0000000000 #TODO Replace with your serverID
ChanID = 0000000000 #TODO Replace with your ChanID

# Variables
version = "v1.0"

# Boss Variables
# Boss Names
Co = "Conquest Wars"
Ka = "Karanda"
Ku = "Kutum"
Kz = "Kzarka"
Ma = "Maintenance"
Mu = "Muraka"
No = "Nouver"
Of = "Offin"
Qu = "Quint"
Ve = "Vell"

# Boss Spawns
firstSpawn = secondSpawn = thirdSpawn = fourthSpawn = fifthSpawn = sixthSpawn = seventhSpawn = eighthSpawn = "None"

# Spawn Time Counters
h1 = h2 = h3 = h4 = h5 = h6 = h7 = h8 = 0
m1 = m2 = m3 = m4 = m5 = m6 = m7 = m8 = 0

# Create Bot
bot = commands.Bot(command_prefix='!', description='A bot that counts down to boss spawns for Black Dessert Online')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def getSpawnNames(day):
    global firstSpawn
    global secondSpawn
    global thirdSpawn
    global fourthSpawn
    global fifthSpawn
    global sixthSpawn
    global seventhSpawn
    global eighthSpawn

    if day is 0:
        firstSpawn = Ku
        secondSpawn = Kz
        thirdSpawn = Kz
        fourthSpawn = No
        fifthSpawn = Ku
        sixthSpawn = No
        seventhSpawn = Kz
        eighthSpawn = Ka
    elif day is 1:
        firstSpawn = Ka
        secondSpawn = Kz
        thirdSpawn = Ku
        fourthSpawn = Of
        fifthSpawn = No
        sixthSpawn = Ka
        seventhSpawn = No + " and " + Kz
        eighthSpawn = Ku
    elif day is 2:
        firstSpawn = Ku
        secondSpawn = Ma
        thirdSpawn = Ka
        fourthSpawn = No
        fifthSpawn = Kz
        sixthSpawn = Ku
        seventhSpawn = Ka + " and " + Kz
        eighthSpawn = No
    elif day is 3:
        firstSpawn = No
        secondSpawn = Kz
        thirdSpawn = Ku
        fourthSpawn = No
        fifthSpawn = Ku
        sixthSpawn = Of
        seventhSpawn = Ka
        eighthSpawn = Kz
    elif day is 4:
        firstSpawn = Of
        secondSpawn = Ka
        thirdSpawn = Ku
        fourthSpawn = Ka
        fifthSpawn = No
        sixthSpawn = Kz
        seventhSpawn = Ku + " and " + Kz
        eighthSpawn = Ka
    elif day is 5:
        firstSpawn = Kz
        secondSpawn = No
        thirdSpawn = Ku
        fourthSpawn = No
        fifthSpawn = Qu + " and " + Mu
        sixthSpawn = Kz + " and " + Ka
        seventhSpawn = Co
        eighthSpawn = No + " and " + Ku
    elif day is 6:
        firstSpawn = Ka
        secondSpawn = Ku
        thirdSpawn = No
        fourthSpawn = Kz
        fifthSpawn = Ve
        sixthSpawn = Ka
        seventhSpawn = Kz + " and " + No
        eighthSpawn = Ku

async def getSpawnTimes(currentTime):
    global h1
    global h2
    global h3
    global h4
    global h5
    global h6
    global h7
    global h8

    global m1
    global m2
    global m3
    global m4
    global m5
    global m6
    global m7
    global m8

    if currentTime.hour == 0:
        h1 = h2 = h3 = h4 = h5 = h6 = h7 = h8 = 24
    else:
        h1 = h2 = h3 = h4 = h5 = h6 = h7 = h8 = currentTime.hour

    m1 = m2 = m3 = m4 = m5 = m6 = m7 = m8 = currentTime.minute

    h1 = 24 - h1
    h2 = 3 - h2
    h3 = 7 - h3
    h4 = 10 - h4
    h5 = 14 - h5
    h6 = 17 - h6
    h7 = 20 - h7
    h8 = 22 - h8

    m1 = 60 - m1
    m2 = 60 - m2
    m3 = 60 - m3
    m4 = 60 - m4
    m5 = 60 - m5
    m6 = 60 - m6
    if currentTime.minute > 15:
        m7 = 60 - m7
        m8 = 60 - m8
        if m7 > 60:
            m7 = m7 - 60
            m8 = m8 - 60
    else:
        m7 = 15 - m7
        m8 = 15 - m8


async def display_timer():
    await bot.wait_until_ready()
    channel = bot.get_channel(ChanID)
    while bot.is_ready:
        tZone = pytz.timezone("Etc/GMT+6")
        cTime = datetime.now(tZone)
        await getSpawnNames(cTime.weekday())
        await getSpawnTimes(cTime)
        embed = discord.Embed()
        message = ''
        if h2 > -1:
            message = message + secondSpawn + " will spawn in " + str(h2) + "h" + str(m2) + "m\n"
        if h3 > -1:
            message = message + thirdSpawn + " will spawn in " + str(h3) + "h" + str(m3) + "m\n"
        if h4 > -1:
            message = message + fourthSpawn + " will spawn in " + str(h4) + "h" + str(m4) + "m\n"
        if h5 > -1:
            message = message + fifthSpawn + " will spawn in " + str(h5) + "h" + str(m5) + "m\n"
        if h6 > -1:
            message = message + sixthSpawn + " will spawn in " + str(h6) + "h" + str(m6) + "m\n"
        if h7 > -1:
            message = message + seventhSpawn + " will spawn in " + str(h7) + "h" + str(m7) + "m\n"
        if h8 > -1:
            message = message + eighthSpawn + " will spawn in " + str(h8) + "h" + str(m8) + "m\n"
        if h1 > -1:
            message = message + firstSpawn + " will spawn in " + str(h1) + "h" + str(m1) + "m\n"
        embed.add_field(name="Today's remaining World Boss spawn times:", value=message)
        embed.set_footer(text="Version " + version)
        await channel.send(embed=embed)
        await asyncio.sleep(60)
        await channel.purge()
    pass

bot.loop.create_task(display_timer())
bot.run(BotToken)