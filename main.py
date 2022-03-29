import os
import random


def _input():       return(input("> "))
def pause():        return(os.system('pause'))
def cls():          return(os.system('cls'))

class game():
    bg  = '    '
    pl  = '  ඞ '

    shp = 'Shop'
    hom = 'Home'
    twn = 'Town'
    frm = 'Farm'
    bos = 'Boss'
    wal = ' |  '
    bg   =   '█'
    bh   =   '░'
    BB   =   '▒'


    map = [     
                ['   0','   1','   2','   3','   4','   5','   6','   7','   8','   9','  10','  11','  12',' 13','  14','  15','  16','  17','  18','  19','  20',],
                ['   1',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['   2',    hom,    bg,    bg,    bg,    bg,    twn,   bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['   3',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['   4',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['   5',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bos,   bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['   6',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['   7',    shp,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['   8',    bg,     bg,    bg,    bg,    bg,    frm,   bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['   9',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  10',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  11',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  12',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  13',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  14',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  15',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  16',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  17',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  18',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  19',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg],
                ['  20',    bg,     bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg,   bg,    bg,    bg,    bg,    bg,    bg,    bg,    bg]

            ]

    
    commands = ["tasks"]
    
    class boss():
        def theCrackHead(): # starter, low level, boss/ first encounter.
            bossName = 'CrackHead'
            bossHP = 70
        
            attk = random.randint(20,40)
            retattk = attk - 15

            while bossHP >= 1:
                
                nameOfAttack = input('> ')
            
                if nameOfAttack in ['kick', 'punch', 'chop']:            
                    bossHP -= attk
                    #print(f'(-{attk}) the boss health is: {bossHP}')
                    #print(f'{player.name} is ({player.health}) hp, vs {bossName} is ({bossHP}) hp')
                if bossHP >= 1:
                        
                    #print(f'HAHA! IM STILL STANDING FUCKER!!!')
                    player.health -= retattk
                    
                    print(f'{player.name} is {player.health}hp, vs {bossName} is {bossHP}hp')
                    
                if bossHP <= 0:
                    print(f'{player.name} is {player.health}hp, vs {bossName} is {bossHP}hp')
                    print(F'"oooo aaaaaaaa immmmm deaaaadddd, ouhg"')
                    print('-----BOSS DEFEATED-----')
                    print(f'TIP: He maybe low level, but he could have valueable loot on him,')
                    print(f'     type "loot" after killing an enemy to gain their goods')
                    print(f'     you can also loot points of intrest on your map.')
                    return(False)
                if player.health <= 0:
                    print(f'-{retattk}hp SOOOOO BAD YOU DIED')
                    return(False)
                                 
            
            
            

    class items():
        # food and its affects on health
        food    =           ['bread',   'apple',    'steak',    'carrot']
        foodSaturation =    [12,        10,         45,         14]
        
        # Medication type + what health it restores   
        meds    =           ['iFac']
        medStats    =       [30]
        
        # Low loot name + price    
        lowLoot =           ['Paper_Plate']
        lowLootPrice    =   ['3']
        
        # medium loot name + price    
        medLoot =           ['Keyboard']
        medLootPrice    =   ['30']
        
        # high loot name + price    
        higLoot =           ['Gold_Watch']
        higLootPrice    =   ['2300']
        
        
        #   weppon name + weppon dammage per attack
        wepItem_ID  = ['Basic Wooden Sword','Kitchen Knife','Kitchen Spoon', ]
        wepItem_DMG = ['23',                '42',           '12', ]


class player():
    currentTask = 'none'
    name        = 'player1'
    health      = 100


    class stats():
        level       = 1
        total_xp    = 0
        bosses      = 0
    
    class inventory():
        _meds    = [game.items.meds         [0]]
        _weapons = [game.items.wepItem_ID   [0]]
        _food    = [game.items.food         [0]]
        _lLoot   = []
        _mLoot   = []
        _hLoot   = []
        

                
while __name__ == __name__:
    cls()
        
    print("Enter player name")
    player.name     = _input()
    
    def dispmap():
        for i in range(len(game.map)):
            print(str(game.map[i]).replace("'", " ").replace(",", "").replace("[", " ").replace("]", " ").replace(" ", ""))
            
            
    # player spawn location
    x = 14
    y = 14
    
    game.map[x][y]            =   game.pl 
    
    # game start 
    
    
    
    
    print(f'Welcome {player.name} to the hentral area!\nTalk to Streely in the clock tower if you need a job.\n\nYour task is to find Streely (goto Clock Tower)')
    player.currentTask = '"find Streely in Clock Tower"'
    
    
    
    
    while player.health <= 100:
        theInput = _input()



        if theInput in ['task','tasks']:
            print(f'Current Task: {player.currentTask}')
            
            
            
        if theInput in ['inv','inventory', 'backpack']:
            print(f'Medication  : {player.inventory._meds}')
            print(f'Wepons      : {player.inventory._weapons}')
            print(f'Food        : {player.inventory._food}')
            print(f'Low Loot    : {player.inventory._lLoot}')
            print(f'Medium Loot : {player.inventory._mLoot}')
            print(f'High Loot   : {player.inventory._hLoot}')
            
            
            
        if theInput in ['']:
            print('You got to type someting, say "help!" for help')
            
            
            
        if theInput in ['help', 'help!', 'ahhhh']:
            print('Commands:')
            print('# help, help! or ahhhh\nTo displays this.')
            print('# map or location\nTo display the map/ your location')
            print('# travel, goto, go, or run\nto move in any compass direction\nFor exsample "go left" or "go north"')
            print('# ')
            
            
            
        if theInput in ['map', 'location']:
            dispmap()

        
        if theInput.split()[0] in ['move', 'goto', 'go', 'travel', 'run']:
            cls()
            try:
                print(f'x:{x} y:{y}')
                
                if y == 4 and x == 7:
                    inArea = True
                    
                    print(f'You have found a level 2 Crackhead!\nYour level is {player.stats.level}')
                    print("The Crackhead has dealt 7hp! do you want to run or fight?")
                    
                    theInput = _input()
                    
                    if theInput.split()[0] in ['run', 'escape', 'sprint', 'getout', 'ahhhh']:
                            game.map[y][x]  =   game.bg    
                            x               =   4
                            y               =   4
                            game.map[y][x]  =   game.pl
                            
                            print(f'{player.health}hp You have fled the boss')   
                            inArea = False
                        
                    if theInput.split()[0] in ['stay', 'fight', 'attack', 'kill', 'muhahahah']:
                        cls()
                        print("you have chosen to stay! bawmmm")
                        pause()
                                                
                    while inArea == True:    
                        print('TIP: You should try, kicking punchnching or chopping this boss :D')
                        game.map[y][x]  =   game.bg  
                        game.boss.theCrackHead()
                        y = 5 
                        x = 4
                        theInput = _input()
                        if theInput in ['loot']:
                            print(f'you pillaged his corpse, and got {game.items.medLoot[0]}')
                            player.inventory._meds.append(game.items.meds[0])
                            player.inventory._mLoot.append(game.items.lowLoot[1])
                            player.stats.total_xp   +=  100
                            player.stats.level      +=  1
                        else:
                            print("leaving the area.")
                        inArea = False                      
                
                
                if theInput.split()[1] in ['up', 'north', 'n']:
                    try:    
                        game.map[y][x]  =   game.bg    
                        x               =   x
                        if y == 0:  y = 9
                        else:       y = y - 1
                        game.map[y][x]  =   game.pl
                        dispmap()
                    except:   
                        pass
                if theInput.split()[1] in ['down', 'south', 's']:
                    try:    
                        game.map[y][x]  =   game.bg    
                        x               =   x
                        if y == 9:  y = 0
                        else:       y = y + 1
                        game.map[y][x]  =   game.pl
                        dispmap()
                    except:   
                        pass
                if theInput.split()[1] in ['right', 'east', 'e']:
                    try:    
                        game.map[y][x]  =   game.bg    
                        y               =   y
                        if x == 9:  x = 0
                        else:       x = x + 1
                        game.map[y][x]  =   game.pl
                        dispmap()
                    except:   
                        pass
                if theInput.split()[1] in ['left', 'west', 'w']:
                    try:    
                        game.map[y][x]  =   game.bg    
                        y               =   y
                        if x == 0:  x = 9
                        else:       x = x - 1
                        game.map[y][x]  =   game.pl
                        dispmap()
                    except:   
                        pass
                else:
                    pass
            except:
                print("//An error occurred")