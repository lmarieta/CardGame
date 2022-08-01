import Card

class CardsStruct:
    def __init__(self, cardsDict, nbtotalCards):
        self.cardsDict = cardsDict
        self.nbtotalCards = nbtotalCards

class Deck(CardsStruct):
    @classmethod
    def init_from_filePath(cls, filePath):
        # cardsDict = name -> (Card, maxNbInstance)
        cardsDict = {}
        nbtotalCards = 0

        with open(filePath,'r') as cards:
            # read the file with a for loop
            for card in list(cards)[1:]:
                name, health, attack, maxNbInstance = card.strip().split()
                cardsDict[name] = (Card.Card(name, health, attack), maxNbInstance)
                nbtotalCards += int(maxNbInstance)
        return cls(cardsDict, nbtotalCards)
    @classmethod
    def init_from_dict(cls, cardsDict):
        nbtotalCards = 0
        for cardName in cardsDict:
            nbtotalCards += cardsDict[cardName][1]
        return cls(cardsDict, nbtotalCards)


print(Deck.init_from_filePath("cards.txt").nbtotalCards)