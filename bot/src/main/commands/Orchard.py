import telepot
import requests


class Orchard:
    def __init__(self, bot, users):
        self.bot = bot
        self.users = users

    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text' and message['text'] == '/datos':
            actualUser = message['from']['username']
            actualId = message['from']['id']
            self.users.append({actualId: actualUser})
            
            data = requests.get('http://localhost:5000/current/').json()
            retval = 'time: ' + str(data['time']) + '\n' + \
                     'Temperatura: ' + str(data['tmp']) + '\n' + \
                     'Humedad Relativa: ' + str(data['hr']) + '\n' + \
                     'Humedad en Tierra: ' + str(data['ht']) + '\n' + \
                     'Luz: ' + str(data['luz']) + '\n' + \
                     'Distancia: ' + str(data['distancia']) + '\n'


            return retval
