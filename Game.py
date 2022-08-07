
from CardsStruct import Deck


class Game:
    def __init__(self, path_deck, players):
        self.deck = Deck(path_deck)
        self.players = players

deckplayer = 1
all_cards = 1