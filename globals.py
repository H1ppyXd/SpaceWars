now_boss_flag = False
movement = 0

flag = 0
# Флаг и счетчик для "телепортации"
teleportation = -1
tp_flag = True

enemys = ['front_shot', 'triple_shot']
snipers = ['shot']


def enemy_kill():
    global hero_cooldown, enemys_killed
    if enemys_killed != 45:
        enemys_killed += 1
    if enemys_killed == 45:
        hero_cooldown = 15

    elif enemys_killed >= 35:
        hero_cooldown = 25

    elif enemys_killed >= 25:
        hero_cooldown = 35

    elif enemys_killed >= 15:
        hero_cooldown = 45

    elif enemys_killed < 15:
        hero_cooldown = 50

    if enemys_killed < 0:
        enemys_killed = 0


def nem_movement(x):
    global movement
    if x == 0:
        movement = 0
    elif x == 1:
        movement = 1
    elif x == 2:
        movement = 2


hero_cooldown = 50
enemys_killed = 0