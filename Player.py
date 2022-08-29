from CardsStruct import CardsStruct, Deck, Hand, Stack
import numpy as np

class Player: 
    # constructor  
    def __init__(self, deck, cardsonboard=CardsStruct(), nbHand=0):
        # deck is the cards you have before starting the game 
        self.deck = deck
        self.cardsonboard = cardsonboard
        if nbHand != 0:
            self.hand = Hand(self.draw(nbHand,self.deck),nbHand)
            # stack is the pile of cards you draw
            self.stack = Stack(self.deck.cardsDict,self.deck.nbtotalCards)

    def draw(self, nbCards, cardsStruct):
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

    def playCards(self, names):
        # transfer card from hand to cards on board
        self.hand.rm_cards(names)
        self.cardsonboard.add_cards(names)

if __name__ == "__main__":
    deck = Deck.init_from_filePath('C:/Users/lucas/projet_prog/CardGame/cards.txt')
    print("deck : ")
    print(deck.cardsDict)
    p1 = Player(deck=deck,nbHand=2)
    print("deck : ")
    print(p1.deck.cardsDict)
    p1.draw(2,p1.stack)
    print("stack : ")
    print(p1.stack.cardsDict)
    print("hand : ")
    print(p1.hand.cardsDict)
    print("deck : ")
    print(p1.deck.cardsDict)
