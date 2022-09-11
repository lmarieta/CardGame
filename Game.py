
from CardsStruct import Deck
from Player import Player
from CardsStruct import Hand


class Game:
    def __init__(self, path_deck:str, player1:Player):
        # Here deck is all possible cards
        self.deck = Deck(path_deck)
        self.players = player1

def play_turn(player:Player):
    action = input('Enter action to be executed (play_card, attack, draw)')
    switch_action(player=player,action=action)
        
def switch_action(player:Player, action:str):
    if(action=='play_cards'):
        names = input('Enter array of names')
        player.play_cards(names=names)
    elif(action=='attack'):
        print("Two")
    elif(action=='draw'):
        nbCards = input('Enter number of cards :')
        player.draw(nbCards=nbCards)
    else:
        raise Exception("Input not an authorized action.")


if __name__ == "__main__":
    deck = Deck.init_from_filePath('C:/Users/lucas/projet_prog/CardGame/cards.txt')
    card_in_hand = dict(Stegosaure=deck.cardsDict['Stegosaure'])
    hand = Hand(card_in_hand,1)
    p1 = Player(deck=deck,hand=hand)
    game = Game(path_deck='C:/Users/lucas/projet_prog/CardGame/cards.txt',player1=p1)
    play_turn(p1)