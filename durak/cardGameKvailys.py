import random
import data
import cardClass
import classDeck
import functions


deck = Deck()
deck.mixDeck()
computer = deck.giveHand()
player = deck.giveHand()
kozer = deck.takeCard()
gameEnded = False
usedCards = []
start = whoStart(player, computer)

while not gameEnded:

    printTable(TITLE, kozer, player, computer, player_card='', computer_card='')

    if start:
        print('Your move: rules - show RULES, put - put card')
        action = input()

        if action == 'rules':
            print(RULES)
        elif action == 'put':
            print("Write card number: ")
            player_card = player.pop(int(input()))
            printTable(TITLE, kozer, player, computer, player_card, computer_card='')

            winCard(card, komp_korta)

    else:
        computer_card = kompiuteris.pop()
        print()
        print('Open card: ')
        print(computer_card)
        print('Your move: rules - show RULES, put - put card')
        action = input()

        if action == 'rules':
            print(RULES)
        elif action == 'put':
            print("Write card number: ")
            player_card = player.pop(int(input()))
            if computer_card.suite == player_card.suite:
                winCard(player_card, computer_card)
            else:
                print('Put card of the same suite with bigger rank or kozer!')
