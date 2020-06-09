import json
import paho.mqtt.client as mqtt


class Lamp:
    def __init__(self, idenitificator):
        self.idenitificator = idenitificator
        self.turned_on = False

    def swith_on(self):
        self.turned_on = True

    def switch_off(self):
        self.turned_on = False


broker_address = input('Enter the address of the broker you want to use: ')
topic = 'lamp_control'

lamp = Lamp(input('Lamps_id: '))
client = mqtt.Client(lamp.idenitificator)


def on_message(client, userdata, message):
    message = json.loads(message.payload.decode('utf-8'))
    if lamp.idenitificator == message.id and message.command == 'turn_on':
        lamp.swith_on()
    elif lamp.idenitificator == message.id and message.command == 'turn_off':
        lamp.switch_off()


client.on_message = on_message
client.connect(broker_address, 1883, 60)
client.subscribe(topic)
client.loop_start()
controlled_remotely = True
while controlled_remotely:
    print('If you want to set the lamp into the manual mode type "stop".')
    typed_in = input(": ")
    if typed_in == 'stop':
        controlled_remotely = False
client.loop_stop()
