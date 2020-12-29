import pyowm
import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


bot = telebot.TeleBot("1426183022:AAEzpyz0eNyfCjOyIz7znl1CzGtWPATmBKs")

config_dict = get_default_config()
config_dict['language'] = 'uk'

owm = pyowm.OWM('34930bf7d1a20d4d25da398d87cf2698', config_dict)
config_dict = owm.configuration
mrg = owm.weather_manager()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привіт, я бот-метеоролог. Напиши, будь-ласка, своє місто😄")



@bot.message_handler(content_types=['text'])
def send_text(message):
 observation = mrg.weather_at_place( message.text )
 w = observation.weather
 mintemp = w.temperature('celsius')["temp_min"]
 temp = w.temperature('celsius')["temp"]
 maxtemp = w.temperature('celsius')["temp_max"]
 wind = w.wind()["speed"]
 humidity = w.humidity
 cloud = w.clouds 

 answer = "У місті " + message.text + " зараз😉: " + str(w.detailed_status) + "\n\n"
 answer += "Мінімальна темперетура сьогодні буде від : " + str(mintemp) + "°С" + "\n"
 answer += "Максимальна температура до : " + str(maxtemp) + "°С" + "\n"
 answer += "Температура зараз близько : " +  str(temp) +"°С" + "\n"
 if temp < 0:
    answer += "*Брррр. На дворі морозяка - одягяйся тепліше🥶*" + "\n\n" 
 elif temp < 10:
      answer += "*Прохолодно, куртка не завадить🧥🥰*" + "\n\n"
 else:
      answer += "*Температура норм - вдягай що хочеш🙃*" + "\n\n" 
 answer += "Швидкість вітру - " + str(wind) + "м/сек" + "\n"
 answer += "Вологість становить - " + str(humidity) +"%" + "\n"
 answer += "Хмарність - " + str(cloud) + "%" + "\n\n"
 bot.send_message(message.chat.id, answer)

 

bot.polling(none_stop = True)






