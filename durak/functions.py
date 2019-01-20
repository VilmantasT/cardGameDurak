from data import *
import random

def whoStart(player, computer, kozer):
    player_koz = [RANK_NR[i.rank] for i in player if i.suite == kozer.suite]
    computer_koz = [RANK_NR[j.rank] for j in computer if j.suite == kozer.suite]
    player_koz.sort(reverse=True)
    computer.sort(reverse=True)
    if len(player_koz) > 0 and len(computer_koz) > 0:
        return player_koz[0] < computer_koz[0]
    else:
        return random.choice([True, False])

def printCards(cards):
    for i in range(len(cards)):
        print(str(i) + ':', end=' ')
        print(cards[i], end=' ')

def printTable(title, kozer, player, computer):
    print(title)
    print("Kozer: ")
    print(kozer)
    print('*' * 40)
    print('Player cards: ')
    print_cards(player)
    print('*' * 40)
    print('Computer cards: ')
    print_cards(computer)


def winCard(player_card, com_card):
    global start
    if start:
        if com_card < player_card:
            computer.append(player_card)
            print("Computer took {}".format(player_card))
        else:
            usedCards.append(player_card)
            usedCards.append(com_card)
            print('Cards {} and {} was taken to "used cards deck" '.format(player_card, com_card))
            start = False
    else:
        if com_card < player_card:
            usedCards.append(player_card)
            usedCards.append(com_card)
            print('Is zaidimo ismesta {} ir {} kortos'.format(player_card, com_card))
            start = True
        else:
            player.append(com_card)
            print("Jus pasiemete korta {}".format(com_card))
