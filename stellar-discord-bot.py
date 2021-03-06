import discord,coinmarketcap,requests
from bs4 import BeautifulSoup
from discord.ext import commands

market = coinmarketcap.Market()

coin_name = "stellar"
coin = market.ticker(coin_name)
coin_symbol = (coin[0]["symbol"])

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Logged in as: {} with id: {} ".format(client.user.name,client.user.id))
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    if message.content.lower().startswith('!help'):

        userID = message.author.id
        await client.send_message(message.channel, "<@{}> ```Price ->> !prices\n{}/USD -> !price usd \n{}/BTC -> !price btc \nAll Time High -> !ath\nCMC RANK -> !rank\nProcent change -> !change\n24h Volume -> !volume\nMarket Cap -> !cap```".format(userID,coin_symbol,coin_symbol))

    if message.content.lower().startswith('!price btc'):
        price_btc = (coin[0]["price_btc"])
        userID = message.author.id
        await client.send_message(message.channel, "<@{}> ```{}/BTC: {}```".format(userID,coin_symbol,price_btc))

    if message.content.lower().startswith('!price usd'):
        price_usd = (coin[0]["price_usd"])
        userID = message.author.id
        await client.send_message(message.channel, "<@{}> ```{}/USD: {}```".format(userID,coin_symbol,price_usd))

    if message.content.lower().startswith('!prices'):
        price_usd = (coin[0]["price_usd"])
        price_btc = (coin[0]["price_btc"])
        userID = message.author.id
        await client.send_message(message.channel, "<@{}> ```{}/USD: {} \n{}/BTC: {}```".format(userID,coin_symbol,price_usd,coin_symbol,price_btc))

    if message.content.lower().startswith('!rank'):
        coin_rank = (coin[0]["rank"])
        userID = message.author.id
        await client.send_message(message.channel, "<@{}> ```{} is on {} place at coinmarketcap.com.```".format(userID,coin_symbol,coin_rank))

    if message.content.lower().startswith('!change'):
        change_1h = (coin[0]["percent_change_1h"])
        change_24h = (coin[0]["percent_change_24h"])
        change_7d = (coin[0]["percent_change_7d"])
        userID = message.author.id
        await client.send_message(message.channel, "<@{}> ```Last Hour: {}\n24  Hours:  {}\nLast Week: {}```".format(userID,change_1h,change_24h,change_7d))

    if message.content.lower().startswith('!cap'):
        marketcap = float(coin[0]["market_cap_usd"])
        userID = message.author.id
        await client.send_message(message.channel, "<@{}> ```{} Market cap is {:0.0f} USD.```".format(userID,coin_symbol,marketcap))

    if message.content.lower().startswith('!volume'):
        volume = float(coin[0]["24h_volume_usd"])
        userID = message.author.id
        await client.send_message(message.channel, "<@{}> ```{} 24 hour volume is {:0.0f} USD.```".format(userID,coin_symbol,volume))
    if message.content.lower().startswith('!ath'):
        url = 'https://athcoinindex.com/currencies/{}'.format(coin_name)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        ath = soup.find_all('h4')[0].get_text()
        ath_date = soup.find_all('small')[0].get_text()
        userID = message.author.id
        await client.send_message(message.channel, "<@{}> ```{} All Time High is {} USD at {}.```".format(userID,coin_symbol,ath,ath_date))
        
        
client.run("<token>")#Replace <token> with discord app bot token
        
