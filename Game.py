from CardsStruct import CardsStruct, Deck
from Player import Player
from CardsStruct import Hand
import Card


def play_turn(player:Player):
    action = input('Enter action to be executed (play_card, attack, draw)')
    switch_action(player=player,action=action)
        
def switch_action(player:Player, action:str,cardsStruct=CardsStruct()):
    if(action=='play_card'):
        #TBD general dict of all possible cards to extract hp and attack
        card_name = input('Enter of name of the card :')
        hp = float(input('Enter health points of the card :'))
        attack = float(input('Enter attack points of the card :'))
        names = Card.Card(card_name, hp, attack)
        player.play_cards(names=[names])
    elif(action=='attack'):
        print("Two")
    elif(action=='draw'):
        nbCards = float(input('Enter number of cards :'))
        #TBD random or chose which card? then for loop to iterate on nb of cards
        #draw should be able to receive random cards
        player.draw(nbCards=nbCards,cardsStruct=cardsStruct)
    else:
        raise Exception("Input not an authorized action.")


if __name__ == "__main__":
    deck = Deck.init_from_filePath('C:/Users/lucas/projet_prog/CardGame/cards.txt')
    card_in_hand = dict(Martinpiqueur=deck.cardsDict['Martinpiqueur'])
    hand = Hand(card_in_hand,1)
    p1 = Player(deck=deck,hand=hand)
    play_turn(p1)
    play_turn(p1)
    print('on board:')
    print(p1.cardsonboard.cardsDict)
    print('in hand:')
    print(p1.hand.cardsDict)
