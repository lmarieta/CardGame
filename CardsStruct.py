import Card

class CardsStruct:
    # Any structure of card, allow empty structure of cards, such as cards on 
    # board at beginning of the game
    def __init__(self, cardsDict={}, nbtotalCards=0):
        self.cardsDict = cardsDict
        self.nbtotalCards = nbtotalCards

    def add_cards(self, cards):
            for card in cards:
                if card.name in self.cardsDict:
                    self.cardsDict[card.name][1] += 1
                else:
                    self.cardsDict[card.name] = [card, 1]
                self.nbtotalCards += 1

    def rm_cards(self, cards):
        removed_cards = {}
        for card in cards:
            if card.name not in self.cardsDict:
                raise Exception('Trying to remove card not in stack.')
            if self.cardsDict[card.name][1] > 1:
                self.cardsDict[card.name][1] -= 1
            else:
                del self.cardsDict[card.name]
            if card.name in removed_cards:
                removed_cards[card.name][1] += 1
            else:
                removed_cards[card.name] = [card, 1]
            self.nbtotalCards -= 1
        return removed_cards

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
     pass

class Stack(InGameStruct):
    # Cards to draw
    pass

if __name__ == "__main__":
    deck = Deck.init_from_filePath('C:/Users/lucas/projet_prog/CardGame/cards.txt')
    dct = deck.cardsDict
    n = deck.nbtotalCards
    test = Hand(dct,n)
    diplodocus = Card.Card('diplodocus', 2, 2)

    test.add_cards([diplodocus, diplodocus])
    # print(test.nbtotalCards)
    # print(test.cardsDict)

    s = Stack(dct,n)
    # print(s.cardsDict)
    s.rm_cards([diplodocus])
    # print(s.cardsDict)
    test = Hand()
    test.add_cards([diplodocus, diplodocus])
    print(test.nbtotalCards)
    print(test.cardsDict)