# UnoGame

UnoGame is a project using python that allows you to play Uno with Raspberry Pis using cameras and azure image identification. The project consists of a set of Python scripts.

## Team

- Þorvaldur
- Erlandas

## Apis and Workflow
We used Azure api to identify the cards, Imgbb api to upload images, and pastebin to get the links for the images.
We used GitHub for version control and collaboration. Each team member worked on their own branch and submitted pull requests for code reviews. We also used GitHub Issues to track bugs and feature requests.
It was intended to work as follows:
each player has half a deck of cards and plays one card, to play a card he pushes a button and the camera on slave1 takes an image and processes it using imgbb and sends it over to pastebing along with a boolean value of Player1 = True, Uno = False and draw = false.
The server processes the image from the pastebin using azure api and puts it in a format of B6,R5,Etc... using a class called card.
Boolean values get stored to be checked in the gameloop.
The main gameloop goes through which player played and compares it to the last card, we used a list to store the cards and each time it went above 2 cards we removed the oldest one leaving 2 cards in the list at all times.
Once compared it sends the Value of the card to both slaves and the slaves add a .png extension to it to be able to display it.
each card has a sprite and another set of sprites that have a checkmark or a cross to indicate the turn, there is also a count to note how many cards each player has.
Once you press the draw button the count increases and passes turn to other player.
Eventually when a player is down to one card they press the "uno" button to set the boolean of saiduno to true.
if false player is prompted with a screen that makes him draw 3 cards once the draw button has a count of 3 the game continues.


## Technology Stack

- 1x Raspberry Pi 4
- 2x Raspberry pi zero
- Python 3.x
- 2x Cameras
- 2x Adafruit matrix displays
- ssh pprotocol
- a deck of uno cards

## Challenges

One of the biggest challenges we faced during the development of this project was dealing with connectivity issues, and other kinds of technical issues including The matrix skipping out pixels, not rendering correctly, pi's not connecting to the internet, the time we took configuring internet on these things took up a big part of our time and left us frustrated.

## Conclusion

Overall it was a fun project and even though we failed, we tried and connected socially while doing so.

## Images

![Uno card sprite](https://media.discordapp.net/attachments/1100417862994239641/1102974281094266890/yes.png)
Uno card sprite
![erlandasandthor](https://media.discordapp.net/attachments/1019581625832575007/1106586769606058094/FF3BF49B-A442-4D5F-AA00-291E10628DF2.jpg?width=317&height=564)
Erlandas and Þorvaldur
![setup](https://media.discordapp.net/attachments/1019581625832575007/1106586769346019459/CECDBE7E-40A0-4EBD-974B-843D1F57E95C.jpg?width=317&height=564)
Setup
![Matrix](https://media.discordapp.net/attachments/1019581625832575007/1106586803244372038/95120AA2-B1F6-4CA9-A4DA-2443D55C25B6.jpg?width=317&height=564)
The matrix displaying an image
![Firstattempt](https://media.discordapp.net/attachments/1100417862994239641/1101507397392023552/image.png)
First attempt using machine learning
