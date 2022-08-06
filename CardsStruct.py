import Card

class CardsStruct:
    # Any structure of card
    def __init__(self, cardsDict, nbtotalCards):
        self.cardsDict = cardsDict
        self.nbtotalCards = nbtotalCards

class Deck(CardsStruct):
    # Available cards before starting the game
    @classmethod
    def init_from_filePath(cls, filePath):
        # cardsDict = name -> [Card, maxNbInstance]
        cardsDict = {}
        nbtotalCards = 0

        with open(filePath,'r') as cards:
            # read the file with a for loop
            for card in list(cards)[1:]:
                name, health, attack, maxNbInstance = card.strip().split()
                cardsDict[name] = [Card.Card(name, health, attack), int(maxNbInstance)]
                nbtotalCards += int(maxNbInstance)
        return cls(cardsDict, nbtotalCards)
    @classmethod
    def init_from_dict(cls, cardsDict):
        nbtotalCards = 0
        for cardName in cardsDict:
            nbtotalCards += cardsDict[cardName][1]
        return cls(cardsDict, nbtotalCards)

class InGameStruct(CardsStruct):
    # Structure of cards used in-game
    pass

class Hand(InGameStruct):
    # cardsDict = name -> [Card, nbInstance]
     def add_cards(self, cards):
            for card in cards:
                if card.name in self.cardsDict:
                    self.cardsDict[card.name][1] += 1
                else:
                    self.cardsDict[card.name] = [card, 1]
                self.nbtotalCards += 1

class Stack(InGameStruct):
    # Cards to draw
    def rm_cards(self, cards):
            for card_name in cards:
                if card_name not in self.cardsDict:
                    raise Exception('Trying to remove card not in stack.')

                if self.cardsDict[card_name][1] > 1:
                    self.cardsDict[card_name][1] -= 1
                else:
                    del self.cardsDict[card_name]
                self.nbtotalCards -= 1

deck = Deck.init_from_filePath('C:/Users/lucas/projet prog/card game/cards.txt')
dct = deck.cardsDict
n = deck.nbtotalCards
test = Hand(dct,n)
diplodocus = Card.Card('diplodocus', 2, 2)

test.add_cards([diplodocus, diplodocus])
# print(test.nbtotalCards)
# print(test.cardsDict)

s = Stack(dct,n)
print(s.cardsDict)
s.rm_cards(['diplodocus'])
print(s.cardsDict)