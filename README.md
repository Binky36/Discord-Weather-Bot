# Discord Weather Bot -
#### A discord bot made in basic python
My aim here is to explain how to use the bot, and answer as many questions as possible.
If you want an explanation for the code itself, take a look at the annotations inside it - they start with a # , as is usual in all python code.

----

#### Changelog:
* The bot now responds (and doesn't throw errors) if you have a lack or excess of capitals in Arg1 and Arg2. 

---
 
#### Usage:
The only current command is '~forecast' by default, and it has 4 arguments - 
* The place 
* The country code
* The number of days in the future it is (0 for today)
* The level of detail (Basic, Detailed or Very_Detailed)

Example:  ~forecast London GB 1 detailed 

(Sample outputs are shown in another section)

Unfortunately, It doesn't yet support US states, and would give the weather data for the first city of that name (in the US) that it finds.

---
#### Installation:
As you can see, there are 2 python scripts in this repository - the only difference being the formatting.                                       
One looks like this (PlainTextWeatherBot):  

![alt text](/ExampleOutputs/PlainText.png "I agree")

And  the other like this (EmbeddedWeatherBot):   

![alt text](/ExampleOutputs/Embedded.png "Very yes")

As with all discord bots, you will need a bot token - you can find out more about that [here](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token).        
You will also need an OpenWeatherMap API key in order to use their service - you can find out more about that [here](https://openweathermap.org/price).     
You put both of them here:      
![alt text](/ExampleOutputs/Installation.png "I agree")

Now for running the bot:        
Using a command line, eg. powershell or terminal, enter `pip install -r requirements.txt`, then navigate to the folder you have the python file of your choice stored in (as in the one with the formatting you want), and then enter `python` (name of file)`.py`. You shouldn't close the command line window, as it will tell you when people use commands, and it will close the bot otherwise. If you want to stop the bot without closing the window, just press `ctrl + c`. 

---

I hope this helps you with whatever you wanted it for, and if you have a knowledge of python, feel free to contribute to the code, but if you do, please add annotations so I can understand what you have done :) 

