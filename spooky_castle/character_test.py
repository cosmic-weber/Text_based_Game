from character import Enemy
from item import Item

sword = Item("sword")
sword.set_description("to fight with")
sword.describe()
dave = Enemy("Dave", "A smelly Zombie!")
dave.describe()
dave.set_conversation("I'm Hungry for your blood!")
dave.talk()
dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
