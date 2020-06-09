import json
import paho.mqtt.client as mqtt


broker_address = input('Enter the address of the broker you want to use: ')
topic = 'lamp_control'

controller = mqtt.Client('Controller')


controller.connect(broker_address, 1883, 60)
controller.loop_start()

controlling = True
while controlling:
    do_next = {}
    lamp = input('What is the indentificator of the lamp you want change the state of? Identificator: ')
    do_next['id'] = lamp
    command = input('Command here (turn_on / turn_of): ')
    do_next['command'] = command
    do_next = json.dumps(do_next)
    controller.publish(do_next)
    if input('Stop controlling (yes / no)? Answer: ') == 'yes':
        controlling = False

controller.loop_stop()
