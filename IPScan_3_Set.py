from time import sleep
import yaml
import networkscan
#import datetime
#import timedelta
import telebot

token ='5746884924:AAEiRmmjh0CA_9wm3t2V0OfiZaR6iIX7YE4'
bot = telebot.TeleBot(token)
chat_id = '747767787'


my_network = "192.168.2.0/24"
my_scan = networkscan.Networkscan(my_network)
my_scan.run()


with open("111.txt", "r", encoding="utf-8") as f:  #исчитал список из файла
    for line in f:
        Ip_file = line.split()   #построчно


Ip_file = set(Ip_file)  #конвертация  списка в вножество
print(f"Ip_file = {Ip_file}")

while True :
    Ip_scan = set()  #создал пустое множество
    for i in my_scan.list_of_hosts_found: #сканироване
        Ip_scan.add(i)  #добавление в множество Ip_scan

    New_device = Ip_scan - Ip_file
    Device_disconnected = Ip_file - Ip_scan

    print(f"Ip_scan = {Ip_scan}")
    print(f"New Device {New_device}")  #новые  уст-ва которых нету в списке

    print(f"Device disconect  {Device_disconnected}") #отключенные устройства

    if len(Device_disconnected) > 0:
        try:
            bot.send_message(chat_id, f"Device disconect {Device_disconnected}")  # отправляем сообщение в бот
        except BaseException:
            print('except disconnect')
        print('отправил в бота сооббщение Device disconect')

    if len(New_device) > 0:
        try:
            bot.send_message(chat_id, f"New device {New_device}")  # отправляем сообщение в бот
        except BaseException:
            print('except New device ')
        print('отправил в бота сооббщение New device')

    print('_________________________________')
    sleep(40)








