import telebot
import time
import datetime
from multiprocessing import *
import schedule
API_TOKEN = '2073493631:AAGMTA4EdsHWFzuM3Dh8tkliNU7OCOjIEmo'
bot = telebot.TeleBot(API_TOKEN)
 
 ######настройка чата###############
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
 if message.text == "Привет":
    bot.send_message(message.from_user.id, "Пошел на хер")
 else:
    bot.send_message(message.from_user.id, "мне вообще похер, че ты там пишешь")
 ###############
def start_process():#Запуск Process
    p1 = Process(target=P_schedule.start_schedule, args=()).start()
 
    
class P_schedule(): # Class для работы с schedule
    def start_schedule(): #Запуск schedule
        schedule.every().day.at("20:00").do(P_schedule.send_message1)
        ######Параметры для schedule######
        ##################################
        
        while True: #Запуск цикла
            schedule.run_pending()
            time.sleep(1)
 
    ####Функции для выполнения заданий по времени  
    def send_message1():
        bot.send_message(447438559, 'Пришло время взвешиваться. Нет, серьезно, иди встань на весы!')
    ################
 
###Настройки команд telebot#########
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'че надо, мразота?')    
@bot.message_handler(commands=['ves'])
def start(message):
    bot.send_message(message.chat.id,'сколько-сколько?? офигеть...')     
#####################

    
if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass