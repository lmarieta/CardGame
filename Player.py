from CardsStruct import CardsStruct, Deck, Hand, Stack
from array import array
import Card
import numpy as np

class Player: 
    # constructor  
    def __init__(self, deck: CardsStruct(), cardsonboard=CardsStruct(), nbHand=0, hand=Hand()):
        # deck is the cards you have before starting the game 
        # better to have two constructors?
        self.deck = deck
        self.cardsonboard = cardsonboard
        if hand!=Hand():
            self.hand = hand
        else:
            if nbHand != 0:
                self.hand = Hand(self.draw(nbHand,self.deck),nbHand)
                # stack is the pile of cards you draw
                self.stack = Stack(self.deck.cardsDict,self.deck.nbtotalCards)
            else:
                self.hand = Hand()

    def draw(self, nbCards: int, cardsStruct:CardsStruct()):
        # you draw from cardsStruct
        # you cannot draw more cards than your stack contains
        if nbCards > cardsStruct.nbtotalCards:
            nbCards = cardsStruct.nbtotalCards
        # draw a random card
        idxs_draw = np.random.default_rng().choice(cardsStruct.nbtotalCards, size=nbCards, replace=False, shuffle=False)
        idxs_draw.sort()
        idx = 0
        removed_cards = {}
        for card_name, value in list(cardsStruct.cardsDict.items())[:]:
            card, nbInstance = value
            while len(idxs_draw)>0 and idx<=idxs_draw[0]<idx+nbInstance:
                # remove the card you draw from the stack
                l_removed_card = cardsStruct.rm_cards([card])
                if card_name in removed_cards:
                    removed_cards[card_name][1] += 1
                else:
                    removed_cards[card_name] = l_removed_card[card_name]
                idx += 1
                nbInstance -= 1
                idxs_draw = idxs_draw[1:]
            else:
                idx += nbInstance
        # return removed cards so that you can add them to your hand for example
        return removed_cards

    def play_cards(self, names: array):
        # transfer card from hand to cards on board
        # exemple: 
        # diplodocus = Card.Card('diplodocus', 2, 2)
        # self.play_cards([diplodocus, diplodocus])
        # is it sufficient to check in rm_cards for non existing cards in hand?
        self.hand.rm_cards(names)
        self.cardsonboard.add_cards(names)

    def attack(self,attacker,defender):
        defender.change_hp(attacker.attack)

if __name__ == "__main__":
    deck = Deck.init_from_filePath('C:/Users/lucas/projet_prog/CardGame/cards.txt')
    card_in_hand = dict(Stegosaure=deck.cardsDict['Stegosaure'])
    hand = Hand(card_in_hand,1)
    p1 = Player(deck=deck,hand=hand)
    p2 = Player(deck=deck,nbHand=2)
    stego = Card.Card('Stegosaure', 3, 3)
    p1.play_cards([stego])
    print("cards on board : ")
    print(p1.cardsonboard.cardsDict)
