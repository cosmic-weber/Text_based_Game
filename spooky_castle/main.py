from room import Room
from character import Enemy
from character import Character
from character import Friend
from rpginfo import RPGInfo
from item import Item

backpack = []

spooky_castle = RPGInfo("The Spooky Castle Game!")
spooky_castle.welcome()
RPGInfo.info()

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

dining_hall = Room("dining_hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "north")
ballroom.link_room(dining_hall, "east")

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

cheese = Item("cheese")
cheese.set_description("A large ad smelly block of cheese")
ballroom.set_item_name(cheese)

book = Item("book")
book.set_description("A really good book entitled 'How to sleep for 8 hrs in 3 hrs'")
dining_hall.set_item_name(book)

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

sarah = Friend("Sarah", "A 10 year's old girl hiding under her study table")
sarah.set_conversation("Please help me I'm so scared! Here is a Zombie in dining_hall and i don't know  what to do next.")
ballroom.set_character(sarah)

current_room = kitchen
dead = False

while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    weapon = current_room.get_item_name()

    if inhabitant is not None:
        inhabitant.describe()

    if weapon is not None:
        weapon.describe()

    command = input("> ")
    if command == "exit":
        break

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "take":
        if weapon is not None:
            print("You put the " + weapon.get_name() + " in your backpack")
            backpack.append(weapon.get_name())
            current_room.set_item_name(None)

    elif command == "talk":

        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":

        if inhabitant is not None and isinstance(inhabitant, Enemy):

            print("What item would you like to fight with?")
            fight_with = input()

            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)

                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True

                else :
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True

            else:
                print("You don't have a " + fight_with)

        else:
            print("There is no one here to fight with")

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")


RPGInfo.credits()
