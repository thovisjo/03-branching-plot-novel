#!/usr/bin/python3

import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

inventory = []

deadWoodsman = 0

def word_check(guess, word):
        if str.lower(guess) == str.lower(word):
                return 1
        else:
                return 0

def options3():
        while True:
                threeoptionchoice = input("Please enter your choice: ")
                if (threeoptionchoice != (("1"))) and (threeoptionchoice != ("2")) and (threeoptionchoice != ("3")) and (threeoptionchoice !=("q") and (threeoptionchoice != ("inv"))) :
                        print("Please choose one of the available options.")
                elif threeoptionchoice.lower() == "q":
                        quit()

                elif threeoptionchoice.lower()== "inv":
                        print(inventory)
                else:
                        return threeoptionchoice

def options2():
        while True:
                twooptionchoice = input("Please enter your choice: ")
                if (twooptionchoice != (("1"))) and (twooptionchoice != ("2")) and (twooptionchoice !=("q")) and (twooptionchoice != ("inv")):
                        print("Please choose one of the available options.")

                elif twooptionchoice == "q":
                        quit()
                elif twooptionchoice.lower()== "inv":
                        print(inventory)
                else:
                        return twooptionchoice

def check_inv(item):
        global inventory
        for i in inventory:
                if str.lower(item) == str.lower(i):
                        return True 
        return False

def game_over():
        print("GAME OVER")
        quit()

def kitchen():
        print("You are in a linoleum covered kitchen. Mother has left you alone and told you not to stick your hand in the cookie jar.")
        print("Your options are: [1] Climb the fridge and raid the cookie jar; [2] Wait Patiently. Type [inv] to check inventory. Press [q] to quit.")
        check = options2()
        if check == "1":
                portal()
        elif check == "2":
                print("You wait another hour for your mother.")
                kitchen()

def portal():
        print("You climb the fridge, reaching for the cookie jar. You reach and reach, and barely touch the cookie jar before falling to the floor. Moving from your slight touch, the cookie jar falls onto the floor next to you, shattering into a million pieces.")
        print("A portal opens on the kitchen floor, pulling you in instantaeously. You feel an intense sugar rush as you fall endlessy in a rainbow of colors. Finally,  you land on something soft.")
        sugar_desert()

def sugar_desert():
        global inventory
        havecook = check_inv("Chocolate Chip Cookie")
        if havecook == 0:
                print("A pile of... sand? No... You stick your finger into the pile and lick your finger. Sugar. Mountains topped with snow are in the distance. A chocolate chip cookie has rolled away from the landing site. You pick it up.")
                print("Chocolate chip cookie added to inventory!")
                inventory.append("Chocolate Chip Cookie")
        else:
                print("You have arrived at the Dessert Desert. It has an empty vastness, a horizon broken only by the sugary dunes. There are mountains in the distance.")
        print("Your options are: [1] Eat as much sugar as possible; [2] Walk Towards the Mountains; [3] Look for civilization. Type [inv] to check inventory.  Press [q] to quit.")
        check = options3()
        if check == "1":
                sugar_coma()
        elif check == "2":
                forest()
        elif check == "3":
                dessert_village()

def sugar_coma():
        print("You swallow scoop after scoop of sugar into your mouth. After about 20 minutes, you pass out and enter a sugar coma.")
        game_over()

def forest():
        global inventory
        global deadWoodsman
        havecane = check_inv("Candy Cane")
        print("You arrive at a forest made of candy canes. A dilapadated sign reads: \"Welcome to Sweetserland!\"\nJolly though it should be, a sheer darkness eminates from it and a chill permeates your skin.")
        if deadWoodsman == 0:
                print("Far ahead of you, you see a tall figure cloaked in darkness. He stands atop long legs, fifteen feet high, swinging an ax and chopping down candy canes. His appearance makes you shiver.")
                if havecane == 0:
                        print("Your options are: [1] Arm yourself with a candy cane on the ground. [2] Approach the figure. [3] Return to the desert. Type [inv] to check inventory.  Press [q] to quit.")
                        check = options3()
                        if check == "1":
                                print("Candy Cane added to inventory!")
                                inventory.append("Candy Cane")
                                forest()
                        elif check == "2":
                                greataxe_death()
                        elif check == "3":
                                sugar_desert()
                if havecane == 1:
                        print("Your options are: [1] Approach the figure, now armed with the candy cane. [2] Return to the desert. Type [inv] to check inventory.  Press [q] to quit.")
                        check = options2()
                        if check == "1":
                                combat_woodsman()
                        elif check == "2":
                                sugar_desert()
        elif deadWoodsman == 1:
                print("Your options are: [1] Continue to the mountains. [2] Return to the desert. Type [inv] to check inventory.  Press [q] to quit.")
                check = options2()
                if check == "1":
                        icing_icecaps()
                elif check == "2":
                        sugar_desert()

def greataxe_death():
        print("Unarmed, you approach the woodsman. You raise your hands in the universal symbol for unarmed. A clicking noise fills you ears as the woodsman detects you and turns his long legs towards you. The last thing you see is his great ax comes down from his far away shoulders and crashes down upon you, killing you instantly.")
        game_over()

def combat_woodsman():
        print("Holding you cane, tall as you, you approach the clearing in which the Woodsman stands. A key of gold is around his neck. A clicking noise fills your ears as the woodsman turns his long legs towards you. Sinister eyes of orange, the only thing visible of the monster's face, seem to focus on you.")
        print("Your options are: [1] Use you cane on his legs. [2] Cane his weapon once he strikes. [3] Run away. Type [inv] to check inventory. Press [q] to quit.")
        check = options3()
        if check == "1":
                fallen_woodsman()
        elif check == "2":
                broken_cane()
        elif check == "3":
                forest()

def broken_cane():
        print("The woodsmans great ax, in a chorus of clicks and whirs, comes down upon your cane and shatters it. With one more swing, the tall man removes your head from your body, killing you instantly.")
        game_over()

def fallen_woodsman():
        global inventory
        global deadWoodsman
        print("The woodsman is lying on his back, his true from reveal. The darkness falls from his body to reveal a clockwork skeleton, whirring and clicking. He is unable to move, stuck to the ground. A key rests around his neck.")
        print("Your options are: [1] Say a witty one-liner. [2] Take the key. Type [inv] to check inventory.  Press [q] to quit.")
        check = options2()
        if check == "1":
                print("\"The bigger they are, the harder they fall...\", you whisper to yourself.")
                fallen_woodsman()
        if check == "2":
                print("You take the golden key from his neck. You return to the start of the forest.")
                inventory.append("Woodsman's Key")
                deadWoodsman = 1
                forest()

def dessert_village():
        print("You arrive at a desserted village, crafted from gingerbread. The walls are crumbling, and sand... rather, sugar, blows into town. In the center of town, a manhole is slightly ajar.")
        print("Your options are: [1] Return to the desert. [2] Go into the manhole.")
        check = options2()
        if check == "1":
                sugar_desert()
        elif check == "2":
                if check_inv("Queen's Key"):
                        rebel_camp2()
                else:
                        rebel_camp1()

def rebel_camp1():
        print("You climb down the ladder in the manhole, and fall into a sewage system. Standing once again, there is busling around you. Beings of all shapes and sizes, made entirely from candy, are armed with blades of steel, moving around with the haste of a military camp. A woman made of gingerbread appears to be directing most of the actions, but then sees you.")
        print("\"Child of man!\" she says, her confident voice filling the room. All action stops around you, and you are surrounded by eyes watching you. Silence follows. You notice that there is no other human among the crowd.")
        print("Your options are: [1] \"Uhhhh...\" [2] \"Me?\"")
        check = options2()
        queen_talk()
        
def queen_talk():
        global inventory
        print("You are brought before the woman. You are standing in front of a large table, and across from you she stands.")
        print("\"Child of man, we have been waiting many years for your arrival. You are the prophesized saviour of Sweetserland, I am Queen Lollipop, last of the true heirs to the Sweetserland throne. Many years ago, the evil Count Caramel stole the throne from me, and destroyed the land. The desert around was caused by his policies of intentional drought. It won't be long before our people are lost. Will you join us?")
        print("Your options are: [1] \"Yes.\" [2] \"No.\" Type [inv] to check inventory.  Press [q] to quit.")
        check = options2()
        if check == "1":
                print("Thank you, child of man. To bring the fight to the Count, you'll need the three keys to get into the castle. I have the first key, but the other two are held by the Count's minions, the Woodsman and the Dragon.")
                print("You can take mine. To reach the castle, you'll have to go through the twizzling tunnels in icing icecaps, past the forest. I wish you luck.")
                inventory.append("Queen's Key")
                rebel_camp2()
        elif check == "2":
                print("Very well, I hope you change your mind.")
                dessert_village()

def rebel_camp2():
        print("You are in the rebel camp. The rebels are bustling about.")
        print("Your options are: [1] Return to the village. [2] Review goals. Type [inv] to check inventory.  Press [q] to quit.")
        check = options2()
        if check == "1":
                dessert_village()
        elif check == "2":
                print("Your goal is to defeat the evil Count Caramel, who has driven Sweetserland to ruin. To do this, you must first collect three keys: the Queen's, the Woodsman's, and the Dragon's.")
                rebel_camp2()

def icing_icecaps():
        if not check_inv("Dragon's Key"):
                print("You finally pass the forest, arriving at a tall mountain range, topped with icing. At the top, curling around the mountain, is a great gummy snake, 100 feet long. It slithers down the mountain to meet you.")
                print("Your options are: [1] Stand your ground. [2] Return to the forest. Type [inv] to check inventory.  Press [q] to quit.")
                check = options2()
                if check == "1":
                        snake_intro()
                elif check == "2":
                        forest()
        else:
                print("You are at the bottom of the ice caps. You can see a cave about halfway up, most likely the the Twizzling Tunnels.")
                print("Your options are: [1] Enter the twizzling tunnels. [2] Return to the forest. Type [inv] to check inventory.  Press [q] to quit.")
                check = options2()
                if check == "1":
                        twizzling_tunnels()
                elif check == "2":
                        forest()

def snake_intro():
        print("\"Very brave of you, child of man,\" rasps the snake, as it slowly encircles you. \"Though I would have ex-ssspected as much from ssssomeone who could besssst the Woods-sssman. I know when the tide-sss of change are washing me away. You'll need more than brawn to beat the Count, friend. If you prove you have the brains, you can have my key to the castle. If you lose, I eat you whole. Deal?\"")
        print("Your options are: [1] \"Deal.\" [2] \"No deal.\" Type [inv] to check inventory.  Press [q] to quit.")
        check = options2()
        if check == "1":
                snake_riddle()
        elif check == "2":
                constrictor()

def constrictor():
        print("\"It appearsssss you do not have the brainssss for ssssuch a riddle. Goodbye, Child of Man.\"")
        print("The snake has been surrounding you from the beginning. Its circle grows smaller and smaller, and you are constricted and killed by asphyxiation.")
        game_over()

def snake_riddle():
        print("\"Exc-sssss-ellent. Here is my riddle.\n\n")
        print("\"The word \'Candy\' can be spelled with just two letters. Which two?\"")
        print("Please input your answer: ")
        check = input()
        if word_check(check, "C And Y"):
                dragon_key()
        else:
              constrictor()  

def dragon_key():
        global inventory
        print("\"Well done, child of man. Here is my key. I will be leaving now, for another land. Goodbye.\"")
        inventory.append("Dragon's Key")
        icing_icecaps()

def twizzling_tunnels():
        print("At the entrance of the cave, you realize this is your last chance to go back. Make sure you have all three keys to open the gate to the castle!")
        print("Your options are: [1] Press on. [2] Return to the base of the mountain. Type [inv] to check inventory.  Press [q] to quit.")
        check = options2()
        if check == "1":
                castle()
        elif check == "2":
                icing_icecaps()

def castle():
        print("You make your way through the tunnels, and at the exit you are placed directly in front of a candy cane gate leading to a grand castle. Behind you, you can hear the tunnels collapsing and rearranging. There is no turning back.")
        print("Your options are: [1] Open the gate. [2] Wait. Type [inv] to check inventory.  Press [q] to quit.")
        check = options2()
        if check == "1":
                gardens()
        if check == "2":
                starve()

def starve():
        print("You starve to death.")
        game_over()

def gardens():
        if( check_inv("Dragon's Key") and check_inv("Woodsman's Key") and check_inv("Queen's Key")):
                    print("You open the great gates with the three keys you have collected along your journey. Before you, an anthropomorphic dog in fine clothing stands.")
                    count_caramel()
        else:
                    starve()


def count_caramel():
        print("\"Ah, finally,\" says the dog, turning to face you. \"A child of man. You have come to kill me, I assume? The Queen sent you to do her dirty work? I am Count Caramel. Let's not waste time.\" He draws a long, sharp blade.")
        print("Your options are: [1] Use an item in your inventory. [2] Refuse to fight the Count.")
        check = options2()
        if check == "1":
                    death_of_count()
        elif check == "2":
                    print("\"Foolish child.\" The count runs you through with his rapier and leaves you to bleed out on the ground.")
                    game_over()

def death_of_count():
        while True:
                print("Which item would you like to use?")
                print(inventory)
                check = input()
                if not check_inv(check):
                        print("Please use an item in your inventory.")
                else:
                        if word_check(check, "Chocolate chip cookie"):
                                chocolate_death()
                                break
                        else:
                                stabbed()
                                break

def stabbed():
        print("The count defeats you and your chose weapon, with apparent decades of sword training taking him through. He runs you through and leaves you to bleed out.")
        game_over()

def chocolate_death():
        print("You throw the cookie at the Count.\n\"Oooo, don't mind if I do!\" says the Count, munching down the cookie. He finishes, but then...\n\n\"Is this... chocolate?\"")
        print("He collapses, poisoned to death. Dogs can't eat chocolate, after all.")
        print("You have successfully beaten the Count and saved Sweetserland. Well done! However, your mom does not believe you and is still disappointed that you broke the cookie jar.")


kitchen()
