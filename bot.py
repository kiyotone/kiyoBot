import discord
import responses
import os
import json

times = 0
username = "NOne"
user_message = "NOne"
channel = "NONE"



if os.path.exists(os.getcwd() +"/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)
        print("NO token found")


else:
    print("NO token found")
    pass

TOKEN = configData["TOKEN"]

print(TOKEN)

async def send_messages(message,user_message,is_private):
    try :
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event

    async def on_ready():
        print(f'{client.user} is now longer running')
        # send_messages("i am running bitch")        

    @client.event
    async def on_message(message):
        global times
        global username
        global user_message
        global channel
        if message.author == client.user and times == 0:
            return
        
        if times == 0: 
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)

        

        if user_message[:2] == "--":
            for x in user_message:
                if x == " ":            
                    last = user_message.index(x)
                    str_time = user_message[2:last]
                    print(str_time)
                    times = int(str_time)
                    user_message = user_message[last+1:]
                    if times > 10 :
                        times = 10
                    break
            print(times)
        

        print(f'{username} said : "{user_message} {times}" ("{channel}") ')
        

        if times > 0:
            times-=1
        print(f'Saying {responses.handle_response(user_message)}')
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_messages(message,user_message,is_private=True)
        else:
            
            await send_messages(message,user_message,is_private=False)
        
    client.run(TOKEN)