from CardsStruct import Deck, Hand, Stack
import numpy as np

class Player:    
    def __init__(self, deck, nbHand=0):
        self.deck = deck
        if nbHand != 0:
            self.hand = Hand(self.draw(nbHand,self.deck),nbHand)
            self.stack = Stack(self.deck.cardsDict,self.deck.nbtotalCards)
            self.deck = None

    def draw(self, nbCards, cardsStruct):
        if nbCards > cardsStruct.nbtotalCards:
            nbCards = cardsStruct.nbtotalCards
        idxs_draw = np.random.default_rng().choice(cardsStruct.nbtotalCards, size=nbCards, replace=False, shuffle=False)
        idxs_draw.sort()
        idx = 0
        removed_cards = {}
        for card_name, value in list(cardsStruct.cardsDict.items())[:]:
            card, nbInstance = value
            while len(idxs_draw)>0 and idx<=idxs_draw[0]<idx+nbInstance:
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
        return removed_cards

    def playCards(self, names):
        pass

if __name__ == "__main__":
    deck = Deck.init_from_filePath('C:/Users/lucas/projet_prog/CardGame/cards.txt')
    p1 = Player(deck,1,2)
    print(p1.deck.cardsDict)
    p1.draw(2,p1.deck)
    # print(p1.deck.cardsDict)
