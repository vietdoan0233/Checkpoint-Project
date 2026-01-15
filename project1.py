#Player's hp depends on class
#Turn based
#ALSO PLEASE CHOOSE WITHIN THE GIVEN OPTIONS OTHERWISE THE GAME WILL CRASH
#As of 13/01, my course has only covered variables and loops thus far. Therefore, only one floor will be completed.
#14/01: I wanna give the wyvern a stun skill. I gave claude my code and asked it to clean everything up and i lowk kinda lost interest bc it doesnt look like my work anymore.



# Patch 1.0
# Summary of Changes

# This update introduces:

# New class mechanics (Berserker rage, Vampire lifesteal).

# Fixes to indentation, logic, and repeated code issues.

# Improved defend mechanics with strategic options.

# Correct restart functionality and turn-based tracking.
# https://docs.google.com/document/d/11VD5qGOb0LWsq8ArprH46ClcwIeqbwxwbJk7Fc62TWU/edit?usp=sharing

#Patch 2.0
#https://docs.google.com/spreadsheets/d/1ceerTIKLw5XTq7itciPFY9TJRm-N_fCpBWfD6cgPaik/edit?usp=sharing

#Patch 2.1
#https://docs.google.com/document/d/1VUTwrVzDsoTzpBsPPTuq2KTO-3cU6LbgvGPOh4WyU_I/edit?usp=sharing



print('-----Dungeon Demo-----')

import random 

regressor_level = 0
while True:
    # Greeting and username
    print("\n\nBrave hero, welcome to the abyss.")
    print("Before you an adversary that will challenge your courage, skill, and resolve.") 
    print("Step forth, hero, and carve your legend into the darkness.")
    print("May fortune favour your courage, and may your spirit remain unbroken.")

    username = input('What is your name? ')
    print(f'\nWelcome, {username}.')
    print('May the goddess\'s blessings be with you.')
    print('Choose your class: ')

    # Classes
    classes = ['Knight', 'Berserker', 'Assassin', 'Mage', 'Vampire', '???']
    special_class = 'Regressor'
    if regressor_level >= 1:
        random_class = random.sample(classes, 3) + [special_class]
    else:
        random_class = random.sample(classes, 4)
    
    for i, option in enumerate(random_class, start=1):
        print(f'{i}) {option}')

    print('Beware, brave hero: your chosen class will shape the path that lies ahead. Choose wisely, for your fate depends on it.')

    # User's class selection
    while True:
        try:
            user_input = input('I shall choose... ')
            userclass = int(user_input) - 1
            if userclass < 0 or userclass >= len(random_class):
                print(f'Dear hero, enter a number between 1 and {len(random_class)}.')
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    chosen_class = random_class[userclass]
    if chosen_class == '???':
        print('Interesting choice...')
    elif chosen_class == 'Regressor':
        print('\nDo not fail us again...')
        print(f'Regression: {regressor_level}.')
    else:
        print(f'A wise choice. So be it. Henceforth, you shall walk the path of a {chosen_class}')

    # Class stats
    skill = None  # Initialize skill
    if chosen_class == 'Knight':
        hp = 300  
        atk_min, atk_max = 25, 75
        stamina = 105
        skill = 'Aegis'
        #passive: None
    elif chosen_class == 'Berserker':
        hp = 200
        atk_min, atk_max = 40, 90
        stamina = 90
        #passive: Rage mode
    elif chosen_class == 'Assassin':
        hp = 135
        atk_min, atk_max = 20, 50
        stamina = 75
        #passive: Increased dodge chance, double attack
    elif chosen_class == 'Mage':
        hp = 120
        atk_min, atk_max = 70, 130
        skill = 'Hellfire'
        stamina = 75
        #passive: Reduced LF consumption
    elif chosen_class == 'Vampire':
        hp = 120
        atk_min, atk_max = 50, 110
        stamina = 75
        #passive: Lifesteal
    elif chosen_class == 'Regressor':
        hp = 80
        atk_min, atk_max = 20, 40
        stamina = 999
        skill = 'Rewind'
        hp += int(hp * 0.2 * regressor_level)
        #passive: powerup via regression
    else:  # ??? class
        hp = random.randrange(1, 501, 5)  
        atk_min, atk_max = 0, 200
        stamina = 50
        

    print(f"Chosen class: {chosen_class}.")
    print(f"HP: {hp}, Life Force: {stamina}")

    # Monsters
    name_1 = 'Goblin Chief'
    monster_hp = random.randint(400, 700)
    name_2 = 'Wyvern'
    monster_hp_2 = random.randint(700, 1000)
    #Howl stuns
    
    # Floor tracking
    floor = 1
    userchoice = None  # Initialize userchoice

    # Floor 1: Goblin Chief
    if floor == 1:
        print('\nYou are currently within the premises of the first floor.')
        print('Here lies the infamous Goblin Chief.')
        print('Task: Defeat the Goblin Chief.')

        turn = 1
        if chosen_class == 'Assassin':
            numatk = 2
        elif chosen_class == 'Regressor':
            atk_min += int(atk_min*regressor_level * 0.25)
            atk_max += int(atk_max*regressor_level * 0.25)
        else:
            numatk = 1

        oghp = int(hp)
        ogstam = int(stamina)
        rage_mode = False
        aegis = False
        
        while hp > 0 and monster_hp > 0:
            if stamina <= 0:
                stamina = 0
                hp = 0
                break
            
            print(f'\n\n---Monster: {name_1}, HP: {monster_hp}---')
            print(f'\nTurn {turn}')
            print(f'Life force: {stamina}')
            print("\n1) Attack")
            print("2) Rest")
            print("3) Run away")
            if chosen_class in ['Mage', 'Knight', 'Regressor']:
                print(f"4) {skill}")

            if stamina <= 0.25 * ogstam:
                userchoice = 2
                print('\n\n--WARNING--')
                print('Your life force is critically low.')
                print('You will die once your life force runs out.')
                print('Resting.')
            else:
                while True:
                    try:
                        userchoice = int(input('What will you do? '))
                        if userchoice < 1:
                            print('Dear hero, please enter a valid number.')
                            continue
                        if chosen_class in ['Mage', 'Knight', 'Regressor']:
                            if userchoice > 4:
                                print('Dear hero, please enter a valid number.')
                                continue
                            if userchoice == 4:
                                if chosen_class == 'Knight' and stamina < 76:
                                    print('Not enough life force to use Aegis!')
                                    continue
                                elif chosen_class == 'Mage' and stamina < 36:
                                    print('Not enough life force to use Hellfire!')
                                    continue
                                elif chosen_class == 'Regressor' and stamina < 555:
                                    print('Not enough life force to use Rewind!')
                                    continue
                        else:
                            if userchoice > 3:
                                print('Dear hero, please enter a valid number.')
                                continue
                        break
                    except ValueError:
                        print('Dear hero, please enter a valid number.')

            if userchoice in [1, 3]:  # attack or skill
                if chosen_class == 'Mage':
                    stamina -= 10
                else:
                    stamina -= 15

            if userchoice == 1:
                dodge = random.randint(0, 4) if chosen_class == 'Assassin' else random.randint(0, 6)
                monster_atk = 0 if dodge == 1 else random.randint(25, 60)
                
                print(f'\n{username} chooses to attack {name_1}.')
                for i in range(numatk):
                    if chosen_class == 'Berserker' and hp <= oghp * 0.3 and not rage_mode:
                        rage_mode = True
                        print('\nYour HP has dropped below 30%.')
                        print('Rage mode activated.')
                    
                    if chosen_class == 'Berserker' and rage_mode:
                        atk = atk_max + 20 
                        stamina -= 10
                        print(f'Current damage output: {atk}\n')
                    else:
                        atk = random.randrange(atk_min, atk_max + 1, 5)
                    
                    if chosen_class == 'Vampire':
                        lifesteal = int(atk * 0.2)
                        hp += lifesteal
                        print(f'You have stolen {lifesteal} HP from {name_1}')
                        if hp > oghp:
                            print ('HP limit reached.')
                        hp = min(hp, oghp)
                        
                    
                    monster_hp -= atk
                    print(f'You dealt {atk} damage.')
                    monster_hp = max(0, monster_hp)
                    print(f'{name_1}\'s remaining HP: {monster_hp}')
                
                if monster_hp == 0:
                    print(f'{name_1} has been slain by {username}')
                else:
                    print(f'\n{name_1} attacks {username}!')
                    hp -= monster_atk
                    hp = max(0, hp)
                    if monster_atk == 0:
                        print(f'You have dodged {name_1}\'s attack.')
                    else:
                        print(f'The attack dealt {monster_atk} damage.')
                    print(f'Your remaining HP: {hp}')
                    turn += 1

            elif userchoice == 2:
                dodge = random.randint(0, 4) if chosen_class == 'Assassin' else random.randint(0, 6)
                monster_atk = 0 if dodge == 1 else random.randint(25, 60)
                
                print(f'\n{username} retreats.')
                defend_chance = random.randint(1, 2)
                if defend_chance == 1:
                    print(f'20% of {username}\'s HP has been returned.')
                    hp += int(0.2 * oghp)
                else:
                    print(f'40% of {username}\'s life force has been returned.')
                    stamina = min(stamina + int(0.4 * ogstam), ogstam)
                
                print(f'\n{name_1} attacks {username}!')
                hp -= monster_atk
                hp = max(0, hp)
                if monster_atk == 0:
                    print(f'You have dodged {name_1}\'s attack.')
                else:
                    print(f'The attack dealt {monster_atk} damage.')
                print(f'Your remaining HP: {hp}')
                turn += 1

            elif userchoice == 3:
                print('\nYou have run away.')
                print('...')
                print('Coward. Begone.')
                exit()
                
            elif userchoice == 4:
                monster_atk = random.randint(25, 60)
                
                if chosen_class == 'Knight':
                    print(f'{username} has used Aegis.')
                    aegis = True
                    stamina -= 75
                elif chosen_class == 'Mage':
                    print(f'{username} has used Hellfire.')
                    atk = 1.3 * atk_max
                    monster_hp -= atk
                    print(f'You dealt {atk} damage.')
                    monster_hp = max(0, monster_hp)
                    print(f'{name_1}\'s remaining HP: {monster_hp}')
                    stamina -= 35
                elif chosen_class == 'Regressor':
                    print(f'{username} has used Rewind.')
                    hp = oghp + 50
                    print(f'You\'ve rewound time! Restored HP: {oghp + 50}')
                    stamina -= 555

                if monster_hp == 0:
                    print(f'{name_1} has been slain by {username}')
                else:
                    print(f'\n{name_1} attacks {username}!')
                    
                    if aegis:
                        print(f'Aegis converts {monster_atk} damage into health!')
                        hp += monster_atk
                        hp = min(hp, oghp)
                        aegis = False
                        monster_atk = 0
                    else:
                        hp -= monster_atk
                    
                    hp = max(0, hp)
                    if monster_atk == 0:
                        print(f'You have dodged {name_1}\'s attack.')
                    else:
                        print(f'The attack dealt {monster_atk} damage.')
                    print(f'Your remaining HP: {hp}')
                    turn += 1

        if monster_hp == 0:
            print('\n\n\n---Congratulations on defeating the Goblin Chief---')
            print('\nYou have accomplished a great feat')
            print('Your stats have increased')
            hp = oghp
            stamina = ogstam
            hpmultiplier = random.uniform(1.1, 1.6)
            atkmultiplier = random.uniform(1.1, 1.6)
            hp = int(hp * hpmultiplier)
            oghp = int(hp)  
            stamina += 30
            ogstam = int(stamina)
            atk_min = int(atk_min * atkmultiplier)
            atk_max = int(atk_max * atkmultiplier)
            print(f'Current HP: {hp}')
            print(f'Current damage threshold: {atk_min} - {atk_max}')
            print('\nBefore you lies 3 doors')
            print('\n1) Left')
            print('2) Middle')
            print('3) Right')
            
            while True:
                try:
                    movement = int(input('Which door will you pass through? '))
                    if movement in [1, 2, 3]:
                        break
                    else:
                        print('Dear hero, please choose a number between 1 and 3.')
                except ValueError:
                    print('Dear hero, please choose a number between 1 and 3.')
            
            if movement == 1:
                print("\nYou step through the left door...")
                print("The path ahead feels familiar.")
                print("You descend further into the abyss, reaching Floor 2.")
                floor = 2
            elif movement == 2 or movement == 3:
                print("\nYou step through the door")
                if regressor_level >= 1:
                    print('You recognise this place.')
                    print('You should not have entered, dear Regressor...')
                print("Your vision goes black.")
                print("A presence beyond your comprehension crushes you instantly.")
                hp = 0
        
        if hp == 0:
            print('\nYou have died.')
            print('...')
            print('How pitiful.')
            gameend = input('\n\nDo you want to play again? (y/n) ')
            if gameend == 'y':
                print('\nDo not fail this time...')
                regressor_level += 1
                if regressor_level == 1: 
                    print('You have acquired a new title: Regressor\n\n')
                else:
                    print('You have regressed.\n\n')
                continue
            else:
                print('\nFarewell.')
                exit()

    # Floor 2: Wyvern
    if floor == 2:
        print('\nYou have moved on to the second floor.')
        print('Within this cave lies a Wyvern')
        print('Task: Defeat the Wyvern.')

        turn = 1
        if chosen_class == 'Assassin':
            numatk = 2
        elif chosen_class == 'Regressor':
            atk_min += int(atk_min*regressor_level * 0.25)
            atk_max += int(atk_max*regressor_level * 0.25)
        else:
            numatk = 1
        
        oghp = int(hp)
        ogstam = int(stamina)
        rage_mode = False
        aegis = False
        
        while hp > 0 and monster_hp_2 > 0:
            howl_chance = random.randint(1,10)
            if howl_chance == 1:
                numatk = 0
            else:
                numatk = 2 if chosen_class == 'Assassin' else 1
            if stamina <= 0:
                stamina = 0
                hp = 0
                break
            
            print(f'\n\n---Monster: {name_2}, HP: {monster_hp_2}---')
            print(f'\nTurn {turn}')
            print(f'Life force: {stamina}')
            print('\n1) Attack')
            print('2) Rest')
            print('3) Run away')
            if chosen_class in ['Mage', 'Knight', 'Regressor']:
                print(f"4) {skill}")

            if stamina <= 0.25 * ogstam:
                userchoice = 2
                print('\n\n--WARNING--')
                print('Your life force is critically low.')
                print('You will die once your life force runs out.')
                print('Resting.')
            else:
                while True:
                    try:
                        userchoice = int(input('What will you do? '))
                        if userchoice < 1:
                            print('Dear hero, please enter a valid number.')
                            continue
                        if chosen_class in ['Mage', 'Knight', 'Regressor']:
                            if userchoice > 4:
                                print('Dear hero, please enter a valid number.')
                                continue
                            if userchoice == 4:
                                if chosen_class == 'Knight' and stamina < 76:
                                    print('Not enough life force to use Aegis!')
                                    continue
                                elif chosen_class == 'Mage' and stamina < 36:
                                    print('Not enough life force to use Hellfire!')
                                    continue
                                elif chosen_class == 'Regressor' and stamina < 556:
                                    print('Not enough life force to use Rewind!')
                                    continue
                        else:
                            if userchoice > 3:
                                print('Dear hero, please enter a valid number.')
                                continue
                        break
                    except ValueError:
                        print('Dear hero, please enter a valid number.')

            # Process player action
            if userchoice in [1, 3]:  # attack or skill
                if chosen_class == 'Mage':
                    stamina -= 10
                else:
                    stamina -= 15


            if userchoice == 1:
                dodge = random.randint(0, 4) if chosen_class == 'Assassin' else random.randint(0, 6)
                monster_atk = 0 if dodge == 1 else random.randint(50, 110)
                
                print(f'\n{username} chooses to attack {name_2}.')
                for i in range(numatk):
                    if chosen_class == 'Berserker' and hp <= oghp * 0.3 and not rage_mode:
                        rage_mode = True
                        print('\nYour HP has dropped below 30%.')
                        print('Rage mode activated.')
                    
                    if chosen_class == 'Berserker' and rage_mode:
                        atk = atk_max + 20 
                        stamina -= 10
                        print(f'Current damage output: {atk}\n')
                    else:
                        atk = random.randrange(atk_min, atk_max + 1, 5)
                    
                    if chosen_class == 'Vampire':
                        lifesteal = int(atk * 0.2)
                        hp += lifesteal
                        print(f'You have stolen {lifesteal} HP from {name_2}')
                        if hp > oghp:
                            print ('HP limit reached.')
                        hp = min(hp, oghp)
                    
                    monster_hp_2 -= atk
                    print(f'You dealt {atk} damage.')
                    monster_hp_2 = max(0, monster_hp_2)
                    print(f'{name_2}\'s remaining HP: {monster_hp_2}')
                
                if monster_hp_2 == 0:
                    print(f'{name_2} has been slain by {username}')
                else:
                    if numatk == 0:
                        print(f'\n{name_2} howls!')
                        print('You have been stunned.')
                    print(f'\n{name_2} attacks {username}!')
                    hp -= monster_atk
                    hp = max(0, hp)
                    if monster_atk == 0:
                        print(f'You have dodged {name_2}\'s attack.')
                    else:
                        print(f'The attack dealt {monster_atk} damage.')
                    print(f'Your remaining HP: {hp}')
                    turn += 1

            elif userchoice == 2:
                dodge = random.randint(0, 4) if chosen_class == 'Assassin' else random.randint(0, 6)
                monster_atk = 0 if dodge == 1 else random.randint(50, 110)
                
                print(f'\n{username} retreats.')
                defend_chance = random.randint(1, 2)
                if defend_chance == 1:
                    print(f'20% of {username}\'s HP has been returned.')
                    hp += int(0.2 * oghp)
                else:
                    print(f'40% of {username}\'s life force has been returned.')
                    stamina = min(stamina + int(0.4 * ogstam), ogstam)
                
                print(f'\n{name_2} attacks {username}!')
                hp -= monster_atk
                hp = max(0, hp)
                if monster_atk == 0:
                    print(f'You have dodged {name_2}\'s attack.')
                else:
                    print(f'The attack dealt {monster_atk} damage.')
                print(f'Your remaining HP: {hp}')
                turn += 1

            elif userchoice == 3:
                print('\nYou have run away.')
                print('...')
                print('I see. Farewell, hero.')
                exit()
                
            elif userchoice == 4:
                monster_atk = random.randint(50, 110)
                
                if chosen_class == 'Knight':
                    print(f'{username} has used Aegis.')
                    aegis = True
                    stamina -= 75
                elif chosen_class == 'Mage':
                    print(f'{username} has used Hellfire.')
                    atk = 1.3 * atk_max
                    monster_hp_2 -= atk
                    print(f'You dealt {atk} damage.')
                    monster_hp_2 = max(0, monster_hp_2)
                    print(f'{name_2}\'s remaining HP: {monster_hp_2}')
                    stamina -= 35
                elif chosen_class == 'Regressor':
                    print(f'{username} has used Rewind.')
                    hp = oghp + 50
                    print(f'You\'ve rewound time! Restored HP: {oghp + 50}')
                    stamina -= 555

                if monster_hp_2 == 0:
                    print(f'{name_2} has been slain by {username}')
                else:
                    print(f'\n{name_2} attacks {username}!')
                    
                    if aegis:
                        print(f'Aegis converts {monster_atk} damage into health!')
                        hp += monster_atk
                        hp = min(hp, oghp)
                        aegis = False
                        monster_atk = 0
                    else:
                        hp -= monster_atk
                    
                    hp = max(0, hp)
                    if monster_atk == 0:
                        print(f'You have dodged {name_2}\'s attack.')
                    else:
                        print(f'The attack dealt {monster_atk} damage.')
                    print(f'Your remaining HP: {hp}')
                    turn += 1

        if monster_hp_2 == 0:
            print('\n\n\n---Congratulations on defeating the Wyvern---')
            print('\nYou\'ve achieved something truly unprecedented.')
            print("Few have dared to reach this far, and even fewer have triumphed.")
            print("Your courage and skill have grown beyond imagination.")
            print("Your stats surge with newfound power, readying you for what lies deeper in the abyss.")
            print("Before you lies the next challenge... if you dare to continue.")
            
        elif hp == 0:
            print("\nYou have fallen in battle...")
            print("But reaching this far is no small feat.")
            print("The abyss has tested your courage, and you survived longer than most.")
            print("Your efforts thus far are greatly appreciated.")
            gameend = input('\n\nDo you want to play again? (y/n) ')
            if gameend == 'y':
                print('\nGood luck, hero...')
                regressor_level += 1
                if regressor_level == 1: 
                    print('You have acquired a new title: Regressor\n\n')
                else:
                    print('You have regressed.\n\n')
                continue
            else:
                print('\nI see. Farewell.')
                exit()

            # print('Your stats have increased')
            # hp = oghp
            # stamina = ogstam
            # hpmultiplier = random.uniform(1.1,1.6)
            # atkmultiplier = random.uniform(1.1,1.6)
            # hp = int(hp * hpmultiplier)
            # oghp = int(hp)
            # atk_min = int(atk_min * atkmultiplier)
            # atk_max = int(atk_max * atkmultiplier)
            # print(f'Current HP: {hp}')
            # print(f'Current damage threshold: {atk_min} - {atk_max}')
            # print('\n Before you lies 3 doors')
            # print('\n\n 1) Left')
            # print('2) Middle')
            # print('3) Right')
            # movement = int(input('Which door will you pass through?'))
            # if movement == 1:
            #     print("\nYou step through the left door...")
            #     print("The path ahead feels familiar.")
            #     print("You descend further into the abyss, reaching Floor 2.")
            #     floor += 1 
            # elif movement == 2 or movement == 3:
            #     print("\nYou step through the door")
            #     if regressor_level >= 1:
            #         print('You recognise this place.')
            #         print('You should not have entered, dear Regressor...')
            #     print("Your vision goes black.")
            #     print("A presence beyond your comprehension crushes you instantly.")
            #     hp = 0  
#floor 3: Boss Concept: “Necromancer”
# Start of battle LF Drain: Instantly reduces the player’s LF to 1% at the very first turn.
#No dodging in floor 3 just to spite assassins
