from CardsStruct import Deck

class Player:
    globalDeck = Deck.init_from_filePath("cards.txt")
    
    def __init__(self, deck, hand, stack):
        self.deck = deck
        self.hand = hand
        self.stack = stack
    def draw(self, nbCards):
        pass
    def playCards(self, names):
        pass