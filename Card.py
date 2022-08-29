class Card:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def change_hp(self, hp):
        if self.health + hp >= 0:
            self.health += hp
        else:
            self.health = 0

if __name__ == "__main__":
    tmp = Card('stego',10,3)
    tmp.change_hp(1)
    print(tmp.health)
    tmp.change_hp(-20)
    print(tmp.health)