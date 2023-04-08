from random import randint # Создает случайное число
from time import sleep # Ставит программу "на паузу"

def set_name():
    name = input('Enter your name: ')
    return name

PLAYER_NAME = set_name()
PLAYER_HP = 100
PLAYER_DMG = 10


def fight(player_hp, enemy_hp, 
          player_dmg, enemy_dmg,
          player_weapon = None,
          weapon_database = None,
          player_name=PLAYER_NAME):
    while player_hp > 0 and enemy_hp > 0:
        player_move = randint(1, 2)
        stun = True
        if player_move == 1:
            sleep(2)
            print(f'Ходит {player_name}!')
            sleep(2)
            print(f"{player_name} наносит удар!")
            if player_weapon is not None:
                enemy_hp -= player_dmg + weapon_database[weapon]
                stun_chance = 0
                if stun_chance > randint(1, 100):
                    stun = True
                else:
                    stun = False
            else:
                enemy_hp -= player_dmg
        else:
            if stun: # stun == True
                sleep(2)
                print('Враг оглушен и не может ударить!')
            else:
                sleep(2)
                print('Ходит враг!')
                sleep(2)
                print('Враг наносит удар!')
                player_hp -= enemy_dmg
            
    if player_hp > 0:
        sleep(2)
        print(f"{player_name} победил!")
    else:
        sleep(2)
        print(f"{player_name} проиграл! Гейм овер!")

            
stun_weapon_database = {'Моргенштерн' : 20,
                        'Булава' : 10,
                        'Палка' : 5}

weapon = 'Моргенштерн'
print(f'{PLAYER_NAME} встретился с бандитом!')
bandit_hp = 100
bandit_dmg = 10
sleep(2)
print('Бой неизбежен!')
fight(PLAYER_HP, bandit_hp,
      PLAYER_DMG, bandit_dmg,
      weapon, stun_weapon_database)
