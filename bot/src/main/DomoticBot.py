import telepot
import time
from commands.Start import Start
from commands.Stop import Stop
from commands.Help import Help
from commands.Temp import Temp
from commands.Echo import Echo
from commands.Doorbell import Doorbell
#from nodebase.DomoticNodes import DomoticNodes
#from nodebase.NodePresence import NodePresence
#from nodebase.NodeDoorbell import NodeDoorbell
#from nodebase.NodeClimatization import NodeClimatization
#from nodebase.NodeDoorlock import NodeDoorlock
#from nodebase.Buzzer import Buzzer
from commands.Notify import Notify

class DomoticBot:
    def __init__(self):
        self.users = []
        BOT_TOKEN = '189752430:AAF45NDGJboBXNzqGozBetr0YLrEWE1avsU'
        self.bot = telepot.Bot(BOT_TOKEN)
        #self.domoticNodes = self.__configureDomoticNodes()
        self.handlers = [
            Start(self.bot, self.users),
            Stop(self.bot, self.users),
            Echo(self.bot, self.users)
        ]
        #    Help(self.bot),
        #    Doorbell(self.bot,self.domoticNodes),
        #    Notify(self.bot,self.domoticNodes),
        #    Temp(self.bot,self.domoticNodes)
        #    ]
        #self.bot.notifyOnMessage(self.handle_message)
        self.bot.message_loop(self.handle_message)


    def __configureDomoticNodes(self):
        nodes = DomoticNodes()
        nodes.addNode(NodePresence(23)) # gpio
        nodes.addNode(NodeDoorbell(17, 26, 1, 3000)) # gpio, gpioBuzzer, duration, frequency
        nodes.addNode(NodeClimatization(22, 24)) # gpioCooler, gpioHeater
        nodes.addNode(NodeDoorlock(18))
        nodes.initialize()
        return nodes

    def update(self):
        self.domoticNodes.update()

    def handle_message(self, message):
        print message
        responses = []
        for handler in self.handlers:
            responses.append(handler.processMessage(message))
        userId = message['from']['id']
        for response in responses:
            if response:
                self.bot.sendMessage(userId, response)


def main():
    domotic_bot = DomoticBot()
    while 1:
    #    domotic_bot.update()
	#print "updating the node"
        time.sleep(10)

if __name__ == '__main__':
    main()
