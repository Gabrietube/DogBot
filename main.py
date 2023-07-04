import discord
from bot_logic import gen_pass
from bot_logic import gen_image

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
        await message.channel.send("how are you?")
    elif message.content.startswith('$bye'):
        await message.channel.send("good bye friend")
        await message.channel.send(":cry:")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$help'):
        await message.channel.send(""" DogBot Commands:
        -$hello 
        -$bye 
        -$pass 
        """)
    elif message.content.startswith("$what is your name?"):
        await message.channel.send("My name is DogBot and i'm a puppy")
        await message.channel.send("https://assets.puzzlefactory.com/puzzle/428/505/original.jpg")
    elif message.content.startswith("$good"):
        await message.channel.send("I'm glad you're well")
    elif message.content.startswith("$Image"):
        await message.channel.send(gen_image())
    elif message.content.startswith("$"):
        await message.channel.send("¡ERROR 404!")
        await message.channel.send("Comando no existente")
    else:
        #await message.channel.send(message.content)
        pass

client.run("Tu TOKEN")
