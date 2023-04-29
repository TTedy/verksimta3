import datetime
from uno import *
import paho.mqtt.client as mqtt
from cardclass import UnoCard
# paho code necessary for MQTT communication.
imagelink = "https://cdn.discordapp.com/attachments/1100417862994239641/1101508531372437624/image.png"
print(main(imagelink, list_of_colors))
client = mqtt.Client(userdata={})
client.connect("localhost", 1883)
client.subscribe("player1_deck")
client.subscribe("player2_deck")
client.subscribe("player1_played")
client.subscribe("player2_played")

player1_deck = 5
player2_deck = 5
cards = []
def on_message_player1(client, userdata, message):
    global player1_deck
    if message.topic == "player1_deck":
        player1_deck = int(message.payload.decode())
    elif message.topic == "player1_played":
        player1_deck -= 1

def on_message_player2(client, userdata, message):
    global player2_deck
    if message.topic == "player2_deck":
        player2_deck = int(message.payload.decode())
    elif message.topic == "player2_played":
        player2_deck -= 1

client.on_message = on_message_player1  # Set initial message handler for player 1

# Create client instances for each player and pass in their IDs as userdata.
client1 = mqtt.Client(userdata="player1")
client2 = mqtt.Client(userdata="player2")

client1.connect("localhost", 1883)
client2.connect("localhost", 1883)

run = True

while run:
    # Check if a message for player 1 or player 2 has been received and update the appropriate deck
    if client1.check_msg():
        client.on_message = on_message_player1
    elif client2.check_msg():
        client.on_message = on_message_player2


"""
#need to add this code to work with mqtt since i dont undertsand it
#add first card to list always from player 1
if player1_deck == 5:
    # gets the first card and uses uno.py to find the color and number
    


"""