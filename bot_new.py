
import discord
from discord.ext import commands
import speech_recognition as sr
import asyncio
from pytube import YouTube
import os
from dotenv import load_dotenv

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

recognizer = sr.Recognizer()

# Variable to store the last transcribed text
last_transcribed_text = ""

# Hardcoded channel ID where the message will be sent
target_channel_id = 1226836362947334184  # Replace with the actual channel ID

# Control flags
listening = True
stop_listening = False

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')

    except Exception as e:
        print(e)

@bot.tree.command(name='join', description='Makes the Bot join a VC')
async def join(interaction: discord.Interaction):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        await channel.connect()
        await interaction.response.send_message("I joined the VC")

        # Start the listening loop
        await listen_loop(interaction)
    else:
        await interaction.response.send_message("You need to be in a voice channel to use this command.")

@bot.tree.command(name='leave', description='Makes the Bot leave a VC')
async def leave(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("Left the voice channel!")
    else:
        await interaction.response.send_message("I'm not in a voice channel.")

@bot.tree.command(name='stopmusic', description='Makes the Bot stop playing music')
async def leave(interaction: discord.Interaction):
    for guild in bot.guilds:
        if interaction.guild.voice_client:
            voice_client = discord.utils.get(bot.voice_clients, guild=guild)
            voice_client.stop()
            await interaction.response.send_message("Stopped the music!")
        else:
            await interaction.response.send_message("I'm not in a voice channel.")

async def listen_loop(interaction):
    global last_transcribed_text, listening, stop_listening
    while not stop_listening:
        if listening:
            # Check if the bot is in a voice channel
            for guild in bot.guilds:
                voice_client = discord.utils.get(bot.voice_clients, guild=guild)
                if voice_client:
                    # Listen for speech
                    with sr.Microphone() as source:
                        print("Listening...")
                        try:
                            audio_data = recognizer.listen(source)
                        except sr.WaitTimeoutError:
                            continue  # Handle timeout and continue listening

                    # Use Google Web Speech API to transcribe audio
                    try:
                        text = recognizer.recognize_google(audio_data)
                        print("Transcribed text:", text)
                        last_transcribed_text = text
                        
                        # Check for different commands to play specific songs
                        if "do a funny" in text.lower():
                            await play_music1(interaction)

                        elif "music two" in text.lower() or "music 2" in text.lower():
                            await play_music2(interaction)

                        elif "music three" in text.lower() or "music 3" in text.lower():
                            await play_music3(interaction)

                        elif "do you know who i am" in text.lower():
                            await play_music4(interaction)

                        elif "music 5" in text.lower() or "music five" in text.lower():
                            await play_music5(interaction)

                        elif "leave vc" in text.lower():
                            await interaction.guild.voice_client.disconnect()
                            await interaction.response.send_message("Left the voice channel!")

                        else:
                            await send_heard_message(text, interaction)

                        await send_heard_message(text, interaction)
                        
                    except sr.UnknownValueError:
                        pass  # Handle unknown value error if needed
                    except sr.RequestError as e:
                        print(f"Could not request results from Google Web Speech API; {e}")
                        last_transcribed_text = "Sorry, there was an error processing your request."
                
                # Pause listening while music is playing
                while voice_client.is_playing():
                    await asyncio.sleep(1)  # Wait for 1 second
                
                # Resume listening after music stops
                await asyncio.sleep(1)  # Ensure a small delay before resuming to avoid race conditions

async def send_heard_message(text, interaction):
    target_channel = bot.get_channel(target_channel_id)
    if target_channel:
        await target_channel.send(last_transcribed_text)

async def play_music1(interaction: discord.Interaction):
    try:
        url1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        yt = YouTube(url1)
        stream = yt.streams.filter(only_audio=True).first()
        
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the file name
        file_name = f"{yt.title}.mp3"

        # Construct the relative file path
        file_path = os.path.join(current_dir, file_name)
        
        # Download the file to the specified location
        stream.download(output_path=current_dir, filename=file_name)

        # Play the downloaded file
        voice_client = interaction.guild.voice_client
        voice_client.play(discord.FFmpegPCMAudio(file_path, executable='ffmpeg.exe'))
        
    except Exception as e:
        print(e)
        
async def play_music2(interaction: discord.Interaction):
    try:
        url2 = "https://www.youtube.com/watch?v=tsmPCi7NKrg"
        yt = YouTube(url2)
        stream = yt.streams.filter(only_audio=True).first()
        
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the file name
        file_name = f"{yt.title}.mp3"

        # Construct the relative file path
        file_path = os.path.join(current_dir, file_name)
        
        # Download the file to the specified location
        stream.download(output_path=current_dir, filename=file_name)

        # Play the downloaded file
        voice_client = interaction.guild.voice_client
        voice_client.play(discord.FFmpegPCMAudio(file_path, executable='ffmpeg.exe'))
        
    except Exception as e:
        print(e)

async def play_music3(interaction: discord.Interaction):
    try:
        url3 = "https://www.youtube.com/watch?v=3II2q2CA654"
        yt = YouTube(url3)
        stream = yt.streams.filter(only_audio=True).first()
        
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the file name
        file_name = f"{yt.title}.mp3"

        # Construct the relative file path
        file_path = os.path.join(current_dir, file_name)
        
        # Download the file to the specified location
        stream.download(output_path=current_dir, filename=file_name)

        # Play the downloaded file
        voice_client = interaction.guild.voice_client
        voice_client.play(discord.FFmpegPCMAudio(file_path, executable='ffmpeg.exe'))
        
    except Exception as e:
        print(e)

async def play_music4(interaction: discord.Interaction):
    try:
        url4 = "https://www.youtube.com/watch?v=qRz6S7pi8O0"
        yt = YouTube(url4)
        stream = yt.streams.filter(only_audio=True).first()
        
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the file name
        file_name = f"{yt.title}.mp3"

        # Construct the relative file path
        file_path = os.path.join(current_dir, file_name)
        
        # Download the file to the specified location
        stream.download(output_path=current_dir, filename=file_name)

        # Play the downloaded file
        voice_client = interaction.guild.voice_client
        voice_client.play(discord.FFmpegPCMAudio(file_path, executable='ffmpeg.exe'))
        
    except Exception as e:
        print(e)

async def play_music5(interaction: discord.Interaction):
    try:
        url5 = "https://www.youtube.com/watch?v=MuTgX_A52Eo"
        yt = YouTube(url5)
        stream = yt.streams.filter(only_audio=True).first()
        
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the file name
        file_name = f"{yt.title}.mp3"

        # Construct the relative file path
        file_path = os.path.join(current_dir, file_name)
        
        # Download the file to the specified location
        stream.download(output_path=current_dir, filename=file_name)

        # Play the downloaded file
        voice_client = interaction.guild.voice_client
        voice_client.play(discord.FFmpegPCMAudio(file_path, executable='ffmpeg.exe'))
        
    except Exception as e:
        print(e)
load_dotenv('TOKEN.env')

RUNTOKEN = os.getenv("TOKEN")

try:
    bot.run(RUNTOKEN)
except KeyboardInterrupt:
    print("Bot interrupted by user")