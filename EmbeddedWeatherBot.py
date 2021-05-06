import discord
from discord.ext import commands
import requests
import json
from datetime import datetime

# This is where you should put your api key and bot token.
openWeatherMapApiKey = 'Your OWM api key here'
discordBotToken = 'Your Discord Bot token here'


# Set the prefix for commands, therefore the forecast command is '~forecast'
bot = commands.Bot(command_prefix='~')

# Displays message when bot is ready
@bot.event
async def on_ready():
    print('')
    print(f'{bot.user.name} has connected to Discord sucessfully.')
    print('')


# This is the 'forecast' command.
@bot.command()
async def forecast(ctx, arg1, arg2, arg3, arg4):

    global openWeatherMapApiKey

    apiKey = openWeatherMapApiKey

    now = datetime.now()

    # Quality of life - allows lowercase arguments, e.g. 'london gb' instead of 'London GB'.
    capitalisedArg1 = arg1.capitalize()
    upperCaseArg2 = arg2.upper()

    # Make api requests to geocode arguments 1 and 2, so we can use the OneCall api. 
    geocodingParmeters = {'q': capitalisedArg1 + ',' + upperCaseArg2, 'appid': apiKey}
    geocodingUrl = requests.get('http://api.openweathermap.org/geo/1.0/direct', params = geocodingParmeters)

    geocodingOutput = geocodingUrl.content.decode()

    latitude = json.loads(geocodingOutput)[0]['lat']
    longditude = json.loads(geocodingOutput)[0]['lon']

    # Make api request for the weather request.
    requestParameters = {'lat': latitude, 'lon': longditude, 'exclude': 'current', 'units': 'metric', 'appid': apiKey}  
    requestUrl = requests.get('https://api.openweathermap.org/data/2.5/onecall', params = requestParameters)

    # Get json data for weather request.
    jsonOutput = requestUrl.content.decode()

    # Find useful info (with argument 3 to define day).
    weatherDescription = json.loads(jsonOutput)['daily'][int(arg3)]['weather'][0]['description']
    dayTemp = json.loads(jsonOutput)['daily'][int(arg3)]['temp']['day']#||||||||||||||||||||||||
    nightTemp = json.loads(jsonOutput)['daily'][int(arg3)]['temp']['night']#||||||||||||||||||||
    weatherIcon = json.loads(jsonOutput)['daily'][int(arg3)]['weather'][0]['icon']#|||||||||||||
    minTemp = json.loads(jsonOutput)['daily'][int(arg3)]['temp']['min']#||||||||||||||||||||||||
    maxTemp = json.loads(jsonOutput)['daily'][int(arg3)]['temp']['max']#||||||||||||||||||||||||
    PoP = json.loads(jsonOutput)['daily'][int(arg3)]['pop']#||||||||||||||||||||||||||||||||||||
    uvi =  json.loads(jsonOutput)['daily'][int(arg3)]['uvi']#|||||||||||||||||||||||||||||||||||
    pressure =  json.loads(jsonOutput)['daily'][int(arg3)]['pressure']#|||||||||||||||||||||||||
    dewPoint = json.loads(jsonOutput)['daily'][int(arg3)]['dew_point']#|||||||||||||||||||||||||
    windSpeed = json.loads(jsonOutput)['daily'][int(arg3)]['wind_speed']#|||||||||||||||||||||||
    windDirection = json.loads(jsonOutput)['daily'][int(arg3)]['wind_deg']#|||||||||||||||||||||
    timestampForSunrise = json.loads(jsonOutput)['daily'][int(arg3)]['sunrise']#||||||||||||||||
    timestampForSunset = json.loads(jsonOutput)['daily'][int(arg3)]['sunset']#||||||||||||||||||
    sunrise = datetime.fromtimestamp(timestampForSunrise)#||||||||||||||||||||||||||||||||||||||
    sunset = datetime.fromtimestamp(timestampForSunset)#||||||||||||||||||||||||||||||||||||||||


    # Determines how detailed the response should be with argument 4, and responds accordingly.
    # This one has embeds, instead of plain text

    if arg4 == 'Basic' or arg4 == 'basic':
        
        embed = discord.Embed(
        title = ' ',
        
        color = discord.Color.from_rgb(236, 110, 76))

        embed.set_author(name = 'Requested by ' + ctx.author.display_name, icon_url = ctx.author.avatar_url)
        
        embed.set_thumbnail(url = 'http://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
        
        embed.add_field(name = 'Weather Report: ', value = 'There will be **' + str(weatherDescription) + '** \nwith an average temperature of\n**' + str(dayTemp) + '°** celsius.')

        embed.set_footer(text = 'Powered by OpenWeatherMap')

        await ctx.send(embed = embed)

    elif arg4 == 'Detailed' or arg4 == 'detailed':

        embed = discord.Embed(
        title = ' ',
        
        color = discord.Color.from_rgb(236, 110, 76))

        embed.set_author(name = 'Requested by ' + ctx.author.display_name, icon_url = ctx.author.avatar_url)
        
        embed.set_thumbnail(url = 'http://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
        
        embed.add_field(name = 'Weather Report: ', value = 'There will be **' + str(weatherDescription) + '** \nwith an average temperature of **' + str(dayTemp) + '°** celsius in the day,\nand **' + str(nightTemp) + '°** in the night.\nthe minimum temperature being **' + str(minTemp) + '°** \nand the maximum temperature being **' + str(maxTemp) + '°**.\nThe probability of precipitation is **' + str(PoP) + '**.\nThe sun will rise at **' + str(sunrise) + '** \nand set at **' + str(sunset) + '**.')

        embed.set_footer(text = 'Powered by OpenWeatherMap')

        await ctx.send(embed = embed)

    elif arg4 == 'Very_Detailed' or arg4 == 'Very_detailed' or arg4 == 'very_detailed':

        embed = discord.Embed(
        title = ' ',

        color = discord.Color.from_rgb(236, 110, 76))

        embed.set_author(name = 'Requested by ' + ctx.author.display_name, icon_url = ctx.author.avatar_url)
        
        embed.set_thumbnail(url = 'http://openweathermap.org/img/wn/' + weatherIcon + '@2x.png' )
        
        embed.add_field(name = 'Weather Report: ', value = 'There will be **' + str(weatherDescription) + '** \nwith an average temperature of\n**' + str(dayTemp) + '°** celsius in the day,\nand **' + str(nightTemp) + '°** in the night.\nthe minimum temperature being **' + str(minTemp) + '°** \nand the maximum temperature being **' + str(maxTemp) + '°**.\nThe probability of precipitation is **' + str(PoP) + '**.\nThe sun will rise at **' + str(sunrise) + '** \nand set at **' + str(sunset) + '**.\nThere is a uvi of **' + str(uvi) + '**,\na dew point of **' + str(dewPoint) + '°**\nand pressure of **' + str(pressure) + '** atm.\nThe wind speed is **' + str(windSpeed) + '** m/s,\nand the wind direction is **' + str(windDirection) + '°**.')

        embed.set_footer(text = 'Powered by OpenWeatherMap')

        await ctx.send(embed = embed)

    # Prints the commands that someone has done to the terminal window, with the time. eg.    12:30  -  Username#1111 ran the command '~forecast test test 1 basic'.
    print(now.strftime('%H:%M') + '  -  ' + str(ctx.message.author) + ' ran the commmand \'' + str(ctx.message.content) + '\'')
    print('')

# This runs the bot with the token that you put in near the top.
bot.run(discordBotToken)