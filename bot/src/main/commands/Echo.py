import telepot

class Echo:
    def __init__(self, bot, users):
        self.bot = bot
        self.users = users

    def processMessage(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)

        if content_type == 'text' and message['text'] == '/echo':
            actualUser = message['from']['username']
            actualId = message['from']['id']
            self.users.append({actualId: actualUser})
            return message['text']        
