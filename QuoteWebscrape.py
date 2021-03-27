from bs4 import BeautifulSoup
import requests
import random

source = requests.get('https://wisdomquotes.com/meditation-quotes/').text

soup = BeautifulSoup(source, 'lxml')



'''Puts all webscraped quotes into a list'''
quotes = []
for blockquote in soup.find_all('blockquote'):
   quote = blockquote.p.text
   quotes.append(quote)


'''testing to see if random_quote works. Should get random quote from list of all webscraped quotes.'''
random_quote = random.choice(quotes)


'''Writing all quotes in list into a text file'''
# with open("Quotes.txt", "w", encoding = "utf-8") as f:
#     for quote in quotes:
#         f.write(quote+"\n")
#     f.close()

