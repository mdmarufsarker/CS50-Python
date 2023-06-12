from random import choice
from random import randint
from random import shuffle

coin = choice(["Heads", "Tails"])
print(coin)

dice = randint(1, 6)
print(dice)

cards = ["Jack", "Queen", "King", "Ace"]
shuffle(cards)

for card in cards:
    print(card, end=" ")

print()