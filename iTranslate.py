import os
import random
import discord
from google.cloud import translate_v2
from discord.ext import commands
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\12mto\Desktop\Marina\ServiceKey.json"

translate_client = translate_v2.Client()

#Reading the webscraped file into a usable list for discord bot to use. 
quotes_as_list = []
with open("Quotes.txt", "r", encoding = 'utf-8') as quotes:
   quotes_contents = quotes.readlines()
   for quote in quotes_contents:
      quotes_as_list.append(quote)


bot = commands.Bot(command_prefix = '!')
@bot.event
async def on_ready():
    print("iTranslate is online! :)")


'''Indicates that bot is offline'''
@bot.event
async def on_disconnect():
    print("iTranslate is offline! :(")


'''Lists all functions of the discord bot'''
@bot.command(aliases = ['start'])
async def commands(ctx):
    await ctx.send(f'!languages: Lists out all languages the bot can translate to with ease. WARNING: THIS TAKES FOREVER TO DO. All languages can  be found on: https://cloud.google.com/translate/docs/languages')
    await ctx.send(f'!quote: Returns a randomized quote in any language the user specifies. ex: !quote tl returns a randomized quote in tagalog.')
    await ctx.send(f'!translate: User is able to type specified language and any string and the Google Translate API will be able to detect the language and return the translated string. ex: !translate es Hello')
    await ctx.send(f'!clear: Clears a specified amount of discord lines with default being to 5.')


'''User is able to type any string and the specified language and the Google Translate API will be able to detect the language and return the translated string.'''
@bot.command()
async def translate(ctx, text, *, user_input):
    translated_text = translate_client.translate(user_input, target_language=text)
    await ctx.send(f'Translated text: {translated_text["translatedText"]}')


'''Takes in a randomized quote out of 180 from the website I chose and can return the original + the translated version
into any language the user specifies'''
@bot.command()
async def quote(ctx,*, text):
   randomQuote = random.choice(quotes_as_list)
   translated_text = translate_client.translate(randomQuote, target_language=text)
   translated_quote = translated_text["translatedText"]
   original_quote = translated_text["input"]
   await ctx.send(f'Original quote: {original_quote} \n Translated quote: {translated_quote}')


'''Lists all languages Google's API can translate to. THIS TAKES FOREVER TO LOAD IN DISCORD.'''
@bot.command(aliases=['list'])
async def languages(ctx):
   results = translate_client.get_languages()
   for language in results:
      await ctx.send(f'Language: {language["name"]}; Symbol: {language["language"]}')


'''Clears a specified amount of discord lines with default being to 5.'''
@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)

bot.run("ODI0NzY1NDUyODc4MjE3MjQ2.YF0Irw.ooBWKGDjM3DZn5IysMnHriDazxo")