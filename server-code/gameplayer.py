import datetime
from uno import *
import paho.mqtt.client as mqtt
from cardclass import UnoCard
# paho code necessary for MQTT communication.
imagelink = "https://i.pinimg.com/236x/67/41/03/6741031cf4c5e06ff944d98f13131415.jpg"
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
    # runs main function to get first card and adds it to list
    firstcard1 = main(imagelink, list_of_colors)
    #uses cardclass on card
    firstcard1 = UnoCard(firstcard1[0], firstcard1[1])
    cards.append(firstcard1)
    #if only one card in cards pass turn to player 2
    if len(cards) == 1:
        client.publish("player2_turn", "True")
        client.publish("player1_turn", "False")
    #runs main function on player 2's card and adds it to list
    elif len(cards) == 2:
        firstcard2 = main(imagelink, list_of_colors)
        cards.append(firstcard2)
    #compares the two cards by color and number
    if cards[0].color == cards[1].color or cards[0].number == cards[1].number: #need to add it to cardclass.py to work
        #if they are the same pass turn to player 1
        client.publish("player1_turn", "True")
        client.publish("player2_turn", "False")
    else:
        #if they are not the same pass turn to player 2
        client.publish("player2_turn", "True")
        client.publish("player1_turn", "False")
    #after 3rd card is added to list remove the first one
    if len(cards) == 3:
        cards.pop(0)




"""