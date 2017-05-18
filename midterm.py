import telegram
from telegram.ext import Updater
updater = Updater(token = '374184704:AAELIlwd-NzwMtxoOBlx8JQtGcsVp8b5VeU')
dispatcher = updater.dispatcher

def say_start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = "Let's go !")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', say_start)
dispatcher.add_handler(start_handler)

def weather_almaty(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = 'http://kazhydromet.kz/ru/almaty'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
	degree = wtext[:-12].replace("Сейчас",'')
	if int(degree) < 0:
		wtext1 = "Одевайтесь тепло, на улицах вашего города прохладно"
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext1)
	elif int(degree) > 0:
		wtext2 = "На улицах вашего города тепло, нет нужды надевать зимние вещи"
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext2)


from telegram.ext import CommandHandler
weather_handler1 = CommandHandler('almaty', weather_almaty)
dispatcher.add_handler(weather_handler1)	

def weather_astana(bot, update):
	import requests
	from bs4 import BeautifulSoup
	url = 'http://kazhydromet.kz/ru/astana'
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	wtext = soup.select(".w_map span")[0].text
	bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
	degree = wtext[:-12].replace("Сейчас",'')
	if int(degree) < 0:
		wtext3 = "Одевайтесь тепло, на улицах вашего города прохладно"
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext3)
	elif int(degree) > 0:
		wtext4 = "На улицах вашего города тепло, нет нужды надевать зимние вещи"
		bot.sendMessage(chat_id = update.message.chat_id, text = wtext4)
		

from telegram.ext import CommandHandler
weather_handler2 = CommandHandler('astana', weather_astana)
dispatcher.add_handler(weather_handler2)	



def whattowear(bot, update):
	custom_keyboard = [['/almaty', '/astana']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.sendMessage(chat_id = update.message.chat_id, text = "Choose your city", reply_markup = reply_markup)

from telegram.ext import CommandHandler
whattowear_handler = CommandHandler('whattowear', whattowear)
dispatcher.add_handler(whattowear_handler)

updater.start_polling()	