import telebot
import requests
import json

bot=telebot.TeleBot("tg_id")
weather_api="api_id"

@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.send_message(message.chat.id,"Привет друг!напиши название города:")

@bot.message_handler(content_types=["text"])
def get_weather(message):
    city=message.text.strip().lower()
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric')
    if res.status_code==200:
       data=json.loads(res.text)
       temperatura=data["main"]["temp"]
       bot.reply_to(message, f'Сейчас погода в этом городе:{temperatura}')
    else:
        bot.send_message(message.chat.id,"Город указан не верно")



bot.polling(none_stop=True)