from variants import Variants
from player import Player
import random
import time

a_bet = input("Игрок Alex, сделайте Ваш выбор из вариантов: ROCK, SCISSORS или PAPER: ").upper()
if a_bet == "ROCK":
    alex = Player(Variants.ROCK, "Alex")
elif a_bet == "SCISSORS":
    alex = Player(Variants.SCISSORS, "Alex")
else:
    alex = Player(Variants.PAPER, "Alex")

var = random.choice([Variants.ROCK, Variants.SCISSORS, Variants.PAPER])
bot = Player(var, "Bot")

print('На счёт "три" покажите Ваши варианты.')


def sleepTime(wait):
    print("Один.")
    time.sleep(wait)
    print("Два.")
    time.sleep(wait)
    print("ТРИ!!!")
    print("Вариант Alex: ", a_bet)
    print("Вариант Bot: ", var.name)


sleepTime(1)

player = Player()
player.whoWins(bot, alex)
