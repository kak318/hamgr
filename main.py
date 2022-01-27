import discord, os, random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

class words:
  powitania = ['hi', 'hello', 'cześć', 'elo', 'eluwina', 'no elo', 'no hej', 'hej', 'no cześć']
  wyzywania = ['kurwo', 'jesteś sus', 'jebany', 'pierfol sie', 'chuju', 'fack you', 'u fucking pease of shhit! You are a big fucking mistake!!1!', 'kid']
  amogus = ['sus', 'amongus', 'amogus', 'us', 'amo', 'among', 'sussy', 'baka', 'imposter', 'impostor']
  meme = ['birb', 'urmom', 'mom', 'crab', 'haha', 'yes', 'dont lie to me u sussy baka']
  komplement = ['jesteś piękny', 'ty też', 'piękny', 'piękna', 'superidol']
  unkomplement = ['nie nawidzę cię', 'u little frick', 'słaby', 'nie lubie cie']
  poke = ['jebać pikaczu', 'pikachuj', 'pikachu', 'poke', 'pokemon', 'pkmn', 'charmander', 'raticate', 'gotta catch em all', 'gotta smoke em all', 'tokemon (dont google it)', 'nuzlocke']
  nice = ['nice', '69', '420']

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.split()[0] in words.powitania:
        await message.channel.send(random.choice(words.powitania))
    if message.content.split()[0] in words.wyzywania:
        await message.channel.send(random.choice(words.wyzywania))
    if message.content.split()[0] in words.amogus:
        await message.channel.send(random.choice(words.amogus))
    if message.content.split()[0] in words.meme:
        await message.channel.send(random.choice(words.meme))
    if message.content.split()[0] in words.komplement:
        await message.channel.send(random.choice(words.komplement))
    if message.content.split()[0] in words.unkomplement:
        await message.channel.send(random.choice(words.unkomplement))
    if message.content.split()[0] in words.poke:
        await message.channel.send(random.choice(words.poke))
    if message.content.split()[0] in words.nice:
        await message.channel.send(random.choice(words.nice))

    await client.change_presence(activity=discord.Game(name="Made by JAszko"))

try: client.run(os.getenv("TOKEN"))
except: os.system('kill 1')