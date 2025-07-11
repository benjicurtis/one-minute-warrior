import time
import random
import sys
slimeHP = 5
yourHP = 5
attack = 2
catfishHP = 8
dragonHP = 10
print("   @@@@@@           1 MINUTE WARRIOR           @@@@@@")
print("   @@@@@@@@                                   @@@@@@@@")
print("    @@@@@@                                     @@@@@@")
print("     |||                                        |||")
print("     |||                                        |||")
print("     |||                                        |||")
print("     |||                                        |||")
print("     |||                                        |||")
print("     |||              o   /   ,_)               |||")
print("    __|__            /|\ /   (o,o)             __|__")
print("   |_____|           / \     {_'_}            |_____|")

print("⚔️ 𝗠𝗜𝗡𝗨𝗧𝗘 ⚡ 𝗪𝗔𝗥𝗥𝗜𝗢𝗥 🛡️")
ready = input("🛡️ 𝗔𝗥𝗘 𝗬𝗢𝗨 𝗥𝗘𝗔𝗗𝗬 𝗙𝗢𝗥 𝗕𝗔𝗧𝗧𝗟𝗘? 1 ＝ 𝗬𝗘𝗦 2 ＝ 𝗠𝗨𝗟𝗧𝗜𝗣𝗟𝗔𝗬𝗘𝗥 ")
if ready == "1":
    name = input("𝗪𝗛𝗔𝗧’𝗦 𝗬𝗢𝗨𝗥 𝗡𝗔𝗠𝗘?")
    what_are_you = input("𝗪𝗛𝗔𝗧 𝗔𝗥𝗘 𝗬𝗢𝗨?")
    print("𝗢𝗞 𝗟𝗲𝘁’𝘀 𝗚𝗼", name, "who is a ",what_are_you, "!")

    while yourHP > 0:

        wheretogo = input("1 = forest 2 = river 3 = volcano")

        # user picks forest
        if wheretogo == "1":
            slimeHP = 5
            print("you go into the deep forest")
            print("you smell trees and fungi and weirdly...")
            time.sleep(1)
            print("slime.")
            time.sleep(1)
            print("you turn around to see a puddle slime")

            run = False

            while slimeHP > 0 and not run:
                run = False
                print("wild slime has ",slimeHP, "HP")
                slime = input("what do you do 1 = attack 2 = run")
                if slime == "1":
                    slimeHP -= attack
                    print("the slime leaps at you🦠")
                    enemy_attack = random.randint(0,2)
                    if enemy_attack == 0:
                        print("miss!")
                    else:
                        print("hit")
                    yourHP -= enemy_attack
                    print(name,"'s hp is", yourHP)
                    print("you attack with your sword")
                    if yourHP <= 0:
                        print("💀game over💀")
                        sys.exit()
                if slime == "2":
                    # get out of this inner loop
                    print ("You run away!")
                    run = True

            if slimeHP <= 0:
                print("You win")
                print("you get 0.5 attack power for your sword")
                attack += 0.5
                print("your attack power for your sword is: ", attack, "!")
                print("you also get...")
                time.sleep(1)
                print("a healing potion")
                print("you drink it")
                yourHP += 2
                print("your hp is", yourHP)

        # user picks river
        if wheretogo == "2":
            catfishHP = 8
            print("you go into the river")
            print(" you find a river with a strong current")
            print("you try to jump over it")
            time.sleep(1)
            print("𝐒𝐏𝐋𝐀𝐀𝐀𝐀𝐒𝐇!")
            time.sleep(1)
            print("as you are pulled down the river")
            print("you see a tail...")
            time.sleep(1)
            print("aaand again")
            time.sleep(1)
            print("and again")
            time.sleep(0.8)
            print("the water surges with unnatural force, spiraling… Suddenly")
            print("bang")
            print("a jet of water erupts skyward")
            print("the water splashes down")
            print("and its coming closer")
            print("you see a giant catfish with blades as fins")
            run2 = False
            while catfishHP > 0 and not run2:
                print("wild bladecatfish has ", catfishHP, "HP")
                catfish = input("what do you do 1 = attack 2 = run")
                if catfish == "1":
                    catfishHP -= attack
                    print("the catfish sprayes a water jet")
                    enemy_attack = random.randint(0, 3)
                    if enemy_attack == 0:
                        print("miss")
                    else:
                        print("hit")
                    yourHP -= enemy_attack
                    print(name,"'s hp is", yourHP)
                    print("you attack with your sword")
                    if yourHP <= 0:
                        print("💀game over💀")
                        sys.exit()
                if catfish == "2":
                    print("you run away")
                    run2 = True
                    continue
            if catfishHP == 0:
                print("You win")
                print("you get 0.5 damage for your sword")
                attack += 0.5
                print("your attack power is ", attack, "!")
                print("you also get...")
                time.sleep(1)
                print("a healing potion")
                yourHP += 4
                print("this is your hp now: ",yourHP)

        # user picks volcano
        if wheretogo == "3":
            dragonHP = 10
            print("you go into the smoldering hot volcano")
            print("you see a battleground and go into it")
            time.sleep(1)
            print("ROAR")
            time.sleep(1)
            print("the dragon breathes fire charring the battlefield")
            print("the dragon has 10 hp")
            run3 = False
            while dragonHP > 0 and not run3:
                dragon = input("what do you do 1 = attack 2 = run")
                if dragon == "1":
                    dragonHP -= attack
                    print("the dragon's hp is: ", dragonHP)
                    enemy_attack = random.randint(0,4)
                    print("the dragon swipes at you")
                    yourHP -= enemy_attack
                    if enemy_attack == 0:
                        print("miss")
                    else:
                        print("hit")
                    print(name,"'s hp is: ", yourHP)
                    print("you attack with your sword")
                    if yourHP <= 0:
                        print("💀game over💀")
                        sys.exit()
                    if dragonHP <= 0:
                        print("you have beat the boss of the game")
                        print("you get 6 HP")
                        yourHP += 6
                if dragon == "2":
                    print("you run away")
                    run3 = True
                    continue
else:
    import time
    import random
    import sys

    slimeHP = 7
    yourHP = 5
    yourHP2 = 5
    attack = 2
    catfishHP = 12
    dragonHP = 16
    print("you have selected multiplayer")
    name = input("𝗪𝗛𝗔𝗧’𝗦 p1's 𝗡𝗔𝗠𝗘?")
    what_are_you = input("𝗪𝗛𝗔𝗧 𝗔𝗥𝗘 𝗬𝗢𝗨?")
    print("𝗢𝗞 𝗟𝗲𝘁’𝘀 𝗚𝗼", name, "who is a ",what_are_you, "!")
    name2 = input("𝗪𝗛𝗔𝗧’𝗦 p2's 𝗡𝗔𝗠𝗘?")
    what_are_you2 = input("𝗪𝗛𝗔𝗧 𝗔𝗥𝗘 𝗬𝗢𝗨?")
    print("𝗢𝗞 𝗟𝗲𝘁’𝘀 𝗚𝗼", name2, "who is a ",what_are_you2, "!")
    while yourHP > 0:

        wheretogo = input("1 = forest 2 = river 3 = volcano")

        # user picks forest
        if wheretogo == "1":
            slimeHP = 7
            print(name,"'s party go into the deep forest")
            print("you smell trees and fungi and weirdly...")
            time.sleep(1)
            print("slime.")
            time.sleep(1)
            print("you turn around to see a puddle slime")

            run = False

            while slimeHP > 0 and not run:
                run = False
                print("wild slime has ",slimeHP, "HP")
                print("p1's turn")
                slime = input("what do you do 1 = attack 2 = run")
                if slime == "1":
                    slimeHP -= attack
                    print("the slime leaps at you🦠")
                    enemy_attack = random.randint(0,2)
                    if enemy_attack == 0:
                        print("miss!")
                    else:
                        print("hit")
                    yourHP -= enemy_attack
                    print(name,"'s hp is", yourHP)
                    print("you attack with your sword")
                    if yourHP <= 0:
                        print("💀game over💀")
                        sys.exit()
                    print("p2's turn")
                    print("wild slime has ", slimeHP, "HP")
                    slime = input("what do you do 1 = attack")
                    if slime == "1":
                        slimeHP -= attack
                        print("the slime leaps at you🦠")
                        enemy_attack = random.randint(0, 2)
                        if enemy_attack == 0:
                            print("miss!")
                        else:
                            print("hit")
                        yourHP2 -= enemy_attack
                        print(name2,"'s hp is", yourHP2)
                        print("you attack with your sword")
                        if yourHP2 <= 0:
                            print("💀game over💀")
                            sys.exit()
                if slime == "2":
                    # get out of this inner loop
                    print ("You run away!")
                    run = True

            if slimeHP <= 0:
                print("group win")
                print("the members get 0.5 attack power for your sword")
                attack += 0.5
                print("your attack power for your sword is: ", attack, "!")
                print("you also get...")
                time.sleep(1)
                print("a healing potions")
                print("you drink them")
                yourHP += 2
                yourHP2 += 2
                print("p1 hp is", yourHP)
                print("p2 hp is", yourHP2)

        # user picks river
        if wheretogo == "2":
            catfishHP = 12
            print("you go into the river")
            print(" you find a river with a strong current")
            print("you try to jump over it")
            time.sleep(1)
            print("𝐒𝐏𝐋𝐀𝐀𝐀𝐀𝐒𝐇!")
            time.sleep(1)
            print("as you are pulled down the river")
            print("you see a tail...")
            time.sleep(1)
            print("aaand again")
            time.sleep(1)
            print("and again")
            time.sleep(0.8)
            print("the water surges with unnatural force, spiraling… Suddenly")
            print("bang")
            print("a jet of water erupts skyward")
            print("the water splashes down")
            print("and its coming closer")
            print("you see a giant catfish with blades as fins")
            run2 = False
            while catfishHP > 0 and not run2:
                print("wild bladecatfish has ", catfishHP, "HP")
                catfish = input("what do you do 1 = attack 2 = run")
                if catfish == "1":
                    catfishHP -= attack
                    print("the catfish sprayes a water jet")
                    enemy_attack = random.randint(0, 3)
                    if enemy_attack == 0:
                        print("miss")
                    else:
                        print("hit")
                    yourHP -= enemy_attack
                    print(name,"'s hp is", yourHP)
                    print("you attack with your sword")
                    if yourHP <= 0:
                        print("💀game over💀")
                        sys.exit()
                    print("p2's turn")
                    print("wild bladecatfish has ", catfishHP, "HP!")
                    catfish = input("what do you do 1 = attack")
                    if catfish == "1":
                        catfishHP -= attack
                        print("the catfish sprayes a water jet")
                        enemy_attack = random.randint(0, 3)
                        if enemy_attack == 0:
                            print("miss!")
                        else:
                            print("hit")
                        yourHP2 -= enemy_attack
                        print(name2, "'s hp is", yourHP2)
                        print("you attack with your sword")
                        if yourHP2 <= 0:
                            print("💀game over💀")
                            sys.exit()
                if catfish == "2":
                    print("you run away")
                    run2 = True
                    continue
            if catfishHP <= 0:
                print("You win")
                print("you get 0.5 damage for your sword")
                attack += 0.5
                print("your attack power is ", attack, "!")
                print("you also get...")
                time.sleep(1)
                print("a healing potion")
                yourHP += 4
                print("this is P1's hp now: ",yourHP)
                print("this is P2's HP", yourHP2)

        # user picks volcano
        if wheretogo == "3":
            dragonHP = 16
            print("you go into the smoldering hot volcano")
            print("you see a battleground and go into it")
            time.sleep(1)
            print("ROAR")
            time.sleep(1)
            print("the dragon breathes fire charring the battlefield")
            print("the dragon has 10 hp")
            run3 = False
            while dragonHP > 0 and not run3:
                dragon = input("what do you do 1 = attack 2 = run")
                if dragon == "1":
                    dragonHP -= attack
                    print("the dragon's hp is: ", dragonHP)
                    enemy_attack = random.randint(0,4)
                    print("the dragon swipes at you")
                    yourHP -= enemy_attack
                    if enemy_attack == 0:
                        print("miss")
                    else:
                        print("hit")
                    print(name,"'s hp is: ", yourHP)
                    print("you attack with your sword")
                    if yourHP <= 0:
                        print("💀game over💀")
                        sys.exit()
                    print("p2's turn")
                    print("th dragon has ", dragonHP, "HP!")
                    dragon = input("what do you do 1 = attack")
                    if dragon == "1":
                        dragonHP -= attack
                        print("the breathes fire")
                        enemy_attack = random.randint(0, 4)
                        if enemy_attack == 0:
                            print("miss!")
                        else:
                            print("hit")
                        yourHP2 -= enemy_attack
                        print(name2, "'s hp is", yourHP2)
                        print("you attack with your sword")
                        if yourHP2 <= 0:
                            print("💀game over💀")
                            sys.exit()
                        if dragonHP <= 0:
                            print("you have beat the boss of the game")
                            print("you get 6 HP")
                            yourHP += 6
                            yourHP2 += 6
                if dragon == "2":
                    print(name,"'s party runs away")
                    run3 = True
                    continue
