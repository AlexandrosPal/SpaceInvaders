import pygame
import random
import os
import sys
import logging
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)


# set up logger config
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s: %(asctime)s: %(name)s: %(message)s')

fileHandler = logging.FileHandler('main.log')
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)


# VARIABLES
FPS = 120
WIDTH, HEIGHT = 750, 600
SPACESHIP_WIDTH = 65
SPACESHIP_HEIGHT = 50


# VEL = 4
# BULLET_VEL = 7
# MAX_BULLETS = 1
# ENEMY_VEL = 2.5

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)

MENU_VEL = 1
anim_index = 0
SOUNDS = 1
MUSIC = 1
DIFFICULTY_INDEX = 2
COLOR_INDEX = 0


# LISTS
difficulty = ['Easy', 'Medi.', 'Hard']
select_color = ['Red', 'Blue', 'Yell.', 'Green', 'Purp.']


# WINDOW
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')


# IMAGES
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH+500, HEIGHT+200))

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)

BLUE_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_blue.png'))
BLUE_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(BLUE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)

GREEN_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_green.png'))
GREEN_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(GREEN_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)

PURPLE_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_purple.png'))
PURPLE_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(PURPLE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)


ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'enemy_2.png'))
ENEMY_IMAGE = pygame.transform.scale(ENEMY_IMAGE, (SPACESHIP_WIDTH+5, SPACESHIP_HEIGHT+25))
GREENENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'green_enemy.png'))
GREENENEMY_IMAGE = pygame.transform.scale(GREENENEMY_IMAGE, (75, 58))

ANIMATION = [pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'animation_1.png')), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
             pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'animation_2.png')), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
             pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'animation_3.png')), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))]


# SOUNDS
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets\\Grenade-1.wav'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets\\Gun-Silencer.wav'))
BACKGROUND_MUSIC = pygame.mixer.Sound(os.path.join('Assets\\audio.wav'))
MENU_MUSIC = pygame.mixer.Sound('Assets\\menu_music.wav')


# FONTS
SCORE_FONT = pygame.font.Font("Assets\\batmfa__.ttf", 35)
OPTIONS_FONT = pygame.font.Font("Assets\\batmfa__.ttf", 40)
WIN_FONT = pygame.font.Font("Assets\\batmfa__.ttf", 50)
MENU_FONT = pygame.font.Font("Assets\\batmfa__.ttf", 80)
MENU_BUTTONS = pygame.font.Font("aSSETS\\BATMFA__.ttf", 60)


# TEXTS
MENU_TEXT = SCORE_FONT.render('MENU', 1, WHITE)


# EVENTS
ENEMY_1_HIT = pygame.USEREVENT + 2
ENEMY_2_HIT = pygame.USEREVENT + 3
ENEMY_3_HIT = pygame.USEREVENT + 4
ENEMY_4_HIT = pygame.USEREVENT + 5
ENEMY_5_HIT = pygame.USEREVENT + 6
ENEMY_6_HIT = pygame.USEREVENT + 7
ENEMY_7_HIT = pygame.USEREVENT + 8
ENEMY_8_HIT = pygame.USEREVENT + 9
ENEMY_9_HIT = pygame.USEREVENT + 10
ENEMY_10_HIT = pygame.USEREVENT + 11
player_HIT = pygame.USEREVENT + 1




def draw_window(player, enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, player_bullets, score, COUNTDOWN, LAST_COUNT):
    global COLOR_INDEX
    
    mins, secs = divmod(COUNTDOWN, 60)
    WIN.blit(SPACE, (0, 0))
    
    if COLOR_INDEX == 0:
        WIN.blit(RED_SPACESHIP_IMAGE, (player.x, player.y))
    elif COLOR_INDEX == 1:
        WIN.blit(BLUE_SPACESHIP_IMAGE, (player.x, player.y))
    elif COLOR_INDEX == 2:
        WIN.blit(YELLOW_SPACESHIP_IMAGE, (player.x, player.y))
    elif COLOR_INDEX == 3:
        WIN.blit(GREEN_SPACESHIP_IMAGE, (player.x, player.y))
    elif COLOR_INDEX == 4:
        WIN.blit(PURPLE_SPACESHIP_IMAGE, (player.x, player.y))
    
    WIN.blit(ENEMY_IMAGE, (enemy_1.x, enemy_1.y))
    WIN.blit(ENEMY_IMAGE, (enemy_2.x, enemy_2.y))
    WIN.blit(ENEMY_IMAGE, (enemy_3.x, enemy_3.y))
    WIN.blit(ENEMY_IMAGE, (enemy_4.x, enemy_4.y))
    WIN.blit(ENEMY_IMAGE, (enemy_5.x, enemy_5.y))
    WIN.blit(ENEMY_IMAGE, (enemy_6.x, enemy_6.y))
    WIN.blit(ENEMY_IMAGE, (enemy_7.x, enemy_7.y))
    WIN.blit(GREENENEMY_IMAGE, (enemy_8.x, enemy_8.y))
    WIN.blit(ENEMY_IMAGE, (enemy_9.x, enemy_9.y))
    WIN.blit(ENEMY_IMAGE, (enemy_10.x, enemy_10.y))
    
    for bullet in player_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    score_text = SCORE_FONT.render(f'Score: {score}', 1, WHITE)
    time_text = SCORE_FONT.render('Time: {:02d}:{:02d}'.format(mins, secs), 1, WHITE)
    WIN.blit(score_text, (10, 10))
    WIN.blit(time_text, (480, 10))
    
    if COUNTDOWN == 0:
            win_text = WIN_FONT.render('YOU WON!', 1, WHITE)
            win_text2 = WIN_FONT.render(f'SCORE: {score}', 1, WHITE)

            logger.debug(f"User won, score {score}")

            WIN.blit(win_text, (WIDTH//2-150, HEIGHT/2-70))
            WIN.blit(win_text2, (WIDTH//2-135, HEIGHT/2+5))
            pygame.display.update()
            with open('Assets\\past_scores.txt', 'a') as f:
                f.write(str(score)+' ')
            pygame.time.delay(4000)
            main_menu()
    
    pygame.display.update()
    
    
def player_handle_movement(keys_pressed, player, VEL):
        if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and player.x > 0: # LEFT
            player.x -= VEL
        if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and player.x + VEL + player.width < WIDTH: # RIGHT 
            player.x += VEL
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]) and player.y > 0: # UP
            player.y -= VEL
        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]) and player.y + VEL + player.height < HEIGHT: # DOWN 
            player.y += VEL
   
def enemy_movement(enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, player, ENEMY_VEL):
    enemy_1.y += ENEMY_VEL
    enemy_2.y += ENEMY_VEL
    enemy_3.y += ENEMY_VEL
    enemy_4.y += ENEMY_VEL
    enemy_5.y += ENEMY_VEL
    enemy_6.y += ENEMY_VEL
    enemy_7.y += ENEMY_VEL
    enemy_8.y += ENEMY_VEL+1
    enemy_9.y += ENEMY_VEL
    enemy_10.y += ENEMY_VEL
    
    positions_x = [0, 100, 175, 250, 325, 400, 500, 630]
    positions_y = [-50,-100,-75,-25,-150,0,20,-125]
    random.shuffle(positions_x)
    random.shuffle(positions_y)
    
    if enemy_1.y > HEIGHT:
        enemy_1.y = positions_y[0]
        enemy_1.x = positions_x[0]
    if enemy_2.y > HEIGHT:
        enemy_2.y = positions_y[0]
        enemy_2.x = positions_x[1]
    if enemy_3.y > HEIGHT:
        enemy_3.y = positions_y[2]
        enemy_3.x = positions_x[2]
    if enemy_4.y > HEIGHT:
        enemy_4.y = positions_y[3]
        enemy_4.x = positions_x[3]
    if enemy_5.y > HEIGHT:
        enemy_5.y = positions_y[4]
        enemy_5.x = positions_x[4]
    if enemy_6.y > HEIGHT:
        enemy_6.y = positions_y[5]
        enemy_6.x = positions_x[5]
    if enemy_7.y > HEIGHT:
        enemy_7.y = positions_y[6]
        enemy_7.x = positions_x[6]
    if enemy_8.y > HEIGHT:
        enemy_8.y = positions_y[7]
        enemy_8.x = positions_x[7]
    if enemy_7.y > HEIGHT:
        enemy_7.y = positions_y[8]
        enemy_7.x = positions_x[8]
    if enemy_8.y > HEIGHT:
        enemy_8.y = positions_y[9]
        enemy_8.x = positions_x[9]
    if player.colliderect(enemy_1):
        pygame.event.post(pygame.event.Event(player_HIT))
    if player.colliderect(enemy_2):
        pygame.event.post(pygame.event.Event(player_HIT))
    if player.colliderect(enemy_3):
        pygame.event.post(pygame.event.Event(player_HIT))
    if player.colliderect(enemy_4):
        pygame.event.post(pygame.event.Event(player_HIT))
    if player.colliderect(enemy_5):
        pygame.event.post(pygame.event.Event(player_HIT))
    if player.colliderect(enemy_6):
        pygame.event.post(pygame.event.Event(player_HIT))
    if player.colliderect(enemy_7):
        pygame.event.post(pygame.event.Event(player_HIT))
    if player.colliderect(enemy_8):
        pygame.event.post(pygame.event.Event(player_HIT))
    if player.colliderect(enemy_9):
        pygame.event.post(pygame.event.Event(player_HIT))
    if player.colliderect(enemy_10):
        pygame.event.post(pygame.event.Event(player_HIT))
   
   
def handle_bullets(enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, player, player_bullets, BULLET_VEL):
    try:
        for bullet in player_bullets:
            bullet.y -= BULLET_VEL
            if enemy_1.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_1_HIT))
                player_bullets.remove(bullet)
            if enemy_2.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_2_HIT))
                player_bullets.remove(bullet)
            if enemy_3.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_3_HIT))
                player_bullets.remove(bullet)
            if enemy_4.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_4_HIT))
                player_bullets.remove(bullet)
            if enemy_5.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_5_HIT))
                player_bullets.remove(bullet)
            if enemy_6.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_6_HIT))
                player_bullets.remove(bullet)
            if enemy_7.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_7_HIT))
                player_bullets.remove(bullet)
            if enemy_8.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_8_HIT))
                player_bullets.remove(bullet)
            if enemy_9.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_9_HIT))
                player_bullets.remove(bullet)
            if enemy_10.colliderect(bullet):
                pygame.event.post(pygame.event.Event(ENEMY_10_HIT))
                player_bullets.remove(bullet)
            elif bullet.y < 0:
                player_bullets.remove(bullet)
    except ValueError:
        print('error!')
        pass


def main_menu_spaceship(BG_SPACESHIP):
    global anim_index
    BG_SPACESHIP.y -= MENU_VEL
    if anim_index >= 3:
        anim_index = 0
    WIN.blit(ANIMATION[int(anim_index)], (BG_SPACESHIP.x, BG_SPACESHIP.y))
    anim_index += 0.06
    if BG_SPACESHIP.y < -200:
        BG_SPACESHIP.y = HEIGHT+200
        BG_SPACESHIP.x = random.randint(100, WIDTH-100)


def options_menu():
    global SOUNDS
    global MUSIC
    global mins, secs
    global difficulty
    global select_color
    global COLOR_INDEX

    BACK_BUTTON = MENU_FONT.render('<', 1, WHITE)
    BACK_BUTTON_2 = MENU_BUTTONS.render('<', 1, WHITE)
    BACK_BUTTON2 = MENU_FONT.render('<', 1, BLACK)
    BACK_BUTTON_22 = MENU_BUTTONS.render('<', 1, BLACK)
    SOUND_BUTTON = pygame.transform.scale(pygame.image.load('Assets\\sound.png'), (45, 60))
    SOUND_OFF = pygame.transform.scale(pygame.image.load('Assets\\sound_off.png'), (71, 61))
    MUSIC_BUTTON = pygame.transform.scale(pygame.image.load('Assets\\music.png'), (65, 60))
    MUSIC_OFF = pygame.transform.scale(pygame.image.load('Assets\\music_off.png'), (97, 64))
    ARROW_UP = pygame.transform.scale(pygame.image.load('Assets\\arrow.png'), (50, 25))
    ARROW_DOWN = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Assets\\arrow.png'), (50, 25)), 180)
    
    TIME_TEXT1 = OPTIONS_FONT.render('TIME', 1, WHITE)
    TIME_TEXT12 = OPTIONS_FONT.render('TIME', 1, GREY)
    
    TIME_TEXT2 = OPTIONS_FONT.render('DIFF.', 1, WHITE)
    TIME_TEXT22 = OPTIONS_FONT.render('DIFF.', 1, GREY)
    
    TIME_TEXT3 = OPTIONS_FONT.render('COLOR', 1, WHITE)
    TIME_TEXT32 = OPTIONS_FONT.render('COLOR', 1, GREY)
    
    DIFFICULTY_INDEX = 2
    COLOR_INDEX = 0
    
    mins, secs = 1, 0
    
    clock = pygame.time.Clock()
    running = True
    while running:
        pygame.init()
        clock.tick(FPS)
        
        if MUSIC == 2:
            MENU_MUSIC.stop()
            
        OPTIONS_COUNTDOWN = OPTIONS_FONT.render('{:02d}:{:02d}'.format(mins, secs), 1, WHITE)
        DIFFICULTY = OPTIONS_FONT.render(difficulty[DIFFICULTY_INDEX], 1, WHITE)
        COLOR = OPTIONS_FONT.render(select_color[COLOR_INDEX], 1, WHITE)
        
        WIN.blit(SPACE, (0, 0))
        
        WIN.blit(BACK_BUTTON2, (31, 21))
        WIN.blit(BACK_BUTTON_22, (58, 34.4))
        WIN.blit(BACK_BUTTON, (30, 20))
        WIN.blit(BACK_BUTTON_2, (53, 29.4))
        
        WIN.blit(ARROW_UP, (125, 300))
        WIN.blit(ARROW_DOWN, (125, 410))
        WIN.blit(ARROW_UP, (350, 300))
        WIN.blit(ARROW_DOWN, (350, 410))
        WIN.blit(ARROW_UP, (575, 300))
        WIN.blit(ARROW_DOWN, (575, 410))
        
        WIN.blit(TIME_TEXT12, (93, 245))
        WIN.blit(TIME_TEXT1, (90, 240))
        WIN.blit(TIME_TEXT22, (326, 245))
        WIN.blit(TIME_TEXT2, (326, 240))
        WIN.blit(TIME_TEXT32, (520, 245))
        WIN.blit(TIME_TEXT3, (520, 240))
        
        WIN.blit(OPTIONS_COUNTDOWN, (90, 345))
        WIN.blit(DIFFICULTY, (310, 345))
        WIN.blit(COLOR, (548, 345))
        
        
        
        
        if SOUNDS == 1:
            WIN.blit(SOUND_BUTTON, (270, 106))
        if SOUNDS == 2:
            WIN.blit(SOUND_OFF, (249, 105))
        if MUSIC == 1:
            WIN.blit(MUSIC_BUTTON, (410, 106))
        if MUSIC == 2:
            WIN.blit(MUSIC_OFF, (400, 103))
        
        
        m_pos = pygame.mouse.get_pos() 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and (m_pos[0] in range(34, 85) and m_pos[1] in range(29, 77)):
                main_menu(DIFFICULTY_INDEX)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if m_pos[0] in range(280, 324) and m_pos[1] in range(106, 165):
                    if SOUNDS == 1:
                        SOUNDS = 2
#                         print(SOUNDS)
                        WIN.blit(SOUND_OFF, (400, 103))
                    else:
                        SOUNDS = 1
#                         print(SOUNDS)
                        WIN.blit(SOUND_BUTTON, (270, 106))
                        
                if m_pos[0] in range(413, 473) and m_pos[1] in range(106, 162):
                    if MUSIC == 1:
                        MUSIC = 2
#                         print(MUSIC)
                        WIN.blit(MUSIC_OFF, (431, 110))
                    else:
                        MUSIC = 1
#                         print(MUSIC)
                        WIN.blit(MUSIC_BUTTON, (410, 106))
                        MENU_MUSIC.play()
                        
                if m_pos[0] in range(125, 172) and m_pos[1] in range(297, 323):
                    if secs + 30 == 60:
                        mins += 1
                        secs -= 30
                    else:
                        secs += 30
                        
                if m_pos[0] in range(125, 172) and m_pos[1] in range(409, 434):
                    if secs - 30 < 0:
                        if mins - 1 < 0:
                            pass
                        else:
                            mins -= 1
                            secs += 30
                    else:
                        secs -= 30
                        
                if m_pos[0] in range(350, 400) and m_pos[1] in range(300, 325):
                    if DIFFICULTY_INDEX == len(difficulty)-1:
                        DIFFICULTY_INDEX = 0
                    else:
                        DIFFICULTY_INDEX += 1
                        
                if m_pos[0] in range(350, 400) and m_pos[1] in range(410, 435):
                    if DIFFICULTY_INDEX == 0:
                        DIFFICULTY_INDEX = len(difficulty)-1
                    else:
                        DIFFICULTY_INDEX -= 1
                        
                if m_pos[0] in range(575, 625) and m_pos[1] in range(300, 325):
                    if  COLOR_INDEX == len(select_color)-1:
                        COLOR_INDEX = 0
                    else:
                        COLOR_INDEX += 1
                
                if m_pos[0] in range(575, 625) and m_pos[1] in range(410, 435):
                    if COLOR_INDEX == 0:
                        COLOR_INDEX = len(select_color)-1
                    else:
                        COLOR_INDEX -= 1
                
        pygame.display.update()


def main_menu(DIFFICULTY_INDEX):
   BACKGROUND_MUSIC.stop()
   MENU_MUSIC.stop()
   if MUSIC == 1:
       MENU_MUSIC.play()
   BG_SPACESHIP = pygame.Rect(random.randint(100,WIDTH-100), HEIGHT+100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
   clock = pygame.time.Clock()
   running = True
   while running:
       pygame.init()
       clock.tick(FPS)
       
       if MUSIC == 2:
           MENU_MUSIC.stop()
       
       WIN.blit(SPACE, (0, 0))
       
       main_menu_spaceship(BG_SPACESHIP)
       MENU_TEXT_2 = MENU_FONT.render('MENU', 1, BLACK)
       PLAY_BUTTON_2 = WIN_FONT.render('PLAY', 1, GREY)
       OPTIONS_BUTTON_2 = WIN_FONT.render('OPTIONS', 1, GREY)
       WIN.blit(MENU_TEXT_2, (WIDTH/2-124, 77))
       WIN.blit(PLAY_BUTTON_2, (WIDTH/2-57, 206))
       WIN.blit(OPTIONS_BUTTON_2, (257, 288))
       WIN.blit(RED_SPACESHIP_IMAGE, (BG_SPACESHIP.x, BG_SPACESHIP.y))
       
       MENU_TEXT = MENU_FONT.render('MENU', 1, WHITE)
       with open('Assets\\past_scores.txt') as f:
           fread = f.readlines()
           fread = fread[0].split(' ')
           new_fread = [int(number) for number in fread if number != ''] 
       try:
           hight_score = max(new_fread)
           MENU_HIGH_SCORE = SCORE_FONT.render(f'HIGH SCORE: {hight_score}', 1, WHITE)
       except:
           MENU_HIGH_SCORE = SCORE_FONT.render(f'HIGH SCORE: -', 1, WHITE)
       
       WIN.blit(MENU_TEXT, (WIDTH/2-132, 70))
       WIN.blit(MENU_HIGH_SCORE, (WIDTH/2-170, HEIGHT-150))
       
       MENU_MOUSE_POS = pygame.mouse.get_pos()
       MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
       
       PLAY_BUTTON = WIN_FONT.render('PLAY', 1, WHITE)
       OPTIONS_BUTTON = WIN_FONT.render('OPTIONS', 1, WHITE)
       
       WIN.blit(PLAY_BUTTON, (WIDTH/2-65, 200))
       WIN.blit(OPTIONS_BUTTON, (250, 281))
       
       m_pos = pygame.mouse.get_pos()
#           print(m_pos)
       
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
               pygame.quit()
               sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if m_pos[0] in range(310, 461) and m_pos[1] in range(210, 245):
                   main(DIFFICULTY_INDEX)
               if m_pos[0] in range(250, 513) and m_pos[1] in range(290, 322):
                   options_menu()
       
       pygame.display.update()



def main(DIFFICULTY_INDEX):
    global SOUNDS
    global MUSIC
    
    MENU_MUSIC.stop()
    if MUSIC == 1:
        BACKGROUND_MUSIC.play()
    try:
        time = mins*60 + secs
    except:
        time = 60
    COUNTDOWN = time
    LAST_COUNT = pygame.time.get_ticks() 
    current_time = pygame.time.get_ticks()
    
    if DIFFICULTY_INDEX == 0:
        VEL = 6
        ENEMY_VEL = 1
        BULLET_VEL = 10
        MAX_BULLETS = 5
    
    elif DIFFICULTY_INDEX == 1:
        VEL = 7
        ENEMY_VEL = 2
        BULLET_VEL = 9
        MAX_BULLETS = 1
        
    elif DIFFICULTY_INDEX == 2:
        VEL = 5
        ENEMY_VEL = 2.5
        BULLET_VEL = 8
        MAX_BULLETS = 1
    
    player_bullets = []
    score = 0
    got_hit = 0
    positions_x = [0, 100, 175, 250, 325, 400, 500, 630, 50, 450]
    positions_y = [-40,-120,-80,-240,-160,0,40,-200, -280, -320]
    random.shuffle(positions_x)
    random.shuffle(positions_y)
    
    player = pygame.Rect(WIDTH/2-SPACESHIP_WIDTH/2, 450, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    enemy_1 = pygame.Rect(positions_x[0], positions_y[0], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-10)
    enemy_2 = pygame.Rect(positions_x[1], positions_y[1], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-30)
    enemy_3 = pygame.Rect(positions_x[2], positions_y[2], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-30)
    enemy_4 = pygame.Rect(positions_x[3], positions_y[3], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-30)
    enemy_5 = pygame.Rect(positions_x[4], positions_y[4], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-30)
    enemy_6 = pygame.Rect(positions_x[5], positions_y[5], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-30)
    enemy_7 = pygame.Rect(positions_x[6], positions_y[6], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-30)
    enemy_8 = pygame.Rect(positions_x[7], positions_y[7], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-30)
    enemy_9 = pygame.Rect(positions_x[8], positions_y[8], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-30)
    enemy_10 = pygame.Rect(positions_x[9], positions_y[9], SPACESHIP_WIDTH, SPACESHIP_HEIGHT-30)
    
    
    clock = pygame.time.Clock()
    run = True
    while run:
        pygame.init()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE  and len(player_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player.x + player.width/2, player.y, 5, 10)
                    player_bullets.append(bullet)
                    if SOUNDS == True:
                        BULLET_FIRE_SOUND.play()
            
            if event.type == ENEMY_1_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_1.y = positions_y[random.randint(0,7)]
                enemy_1.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 1
                
            if event.type == ENEMY_2_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_2.y = positions_y[random.randint(0,7)]
                enemy_2.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 1
                
            if event.type == ENEMY_3_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_3.y = positions_y[random.randint(0,7)]
                enemy_3.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 1
                
            if event.type == ENEMY_4_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_4.y = positions_y[random.randint(0,7)]
                enemy_4.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 1
            
            if event.type == ENEMY_5_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_5.y = positions_y[random.randint(0,7)]
                enemy_5.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 1
                
            if event.type == ENEMY_6_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_6.y = positions_y[random.randint(0,7)]
                enemy_6.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 1
                
            if event.type == ENEMY_7_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_7.y = positions_y[random.randint(0,7)]
                enemy_7.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 1
                
            if event.type == ENEMY_8_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_8.y = positions_y[random.randint(0,7)]
                enemy_8.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 2
                
            if event.type == ENEMY_9_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_9.y = positions_y[random.randint(0,7)]
                enemy_9.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 1
                
            if event.type == ENEMY_10_HIT:
                random.shuffle(positions_x)
                random.shuffle(positions_y)
                enemy_10.y = positions_y[random.randint(0,7)]
                enemy_10.x = positions_x[random.randint(0,7)]
                if SOUNDS == True:
                    BULLET_HIT_SOUND.play()
                score += 1
                
            
            if event.type == player_HIT:
                got_hit += 1
                break
        
        if COUNTDOWN > 0:
            count_timer = pygame.time.get_ticks()
            if count_timer - LAST_COUNT > 1000:
                COUNTDOWN -= 1
                LAST_COUNT = count_timer
                
        
            
        if got_hit > 0 :
            win_text3 = WIN_FONT.render('YOU LOST!', 1, WHITE)
            win_text4 = WIN_FONT.render(f'SCORE: {score}', 1, WHITE)

            logger.debug(f"User lost, score {score}")

            WIN.blit(win_text3, (WIDTH//2-165, HEIGHT/2-70))
            WIN.blit(win_text4, (WIDTH//2-135, HEIGHT/2+5))
            pygame.display.update()
            BACKGROUND_MUSIC.stop()
            with open('Assets\\past_scores.txt', 'a') as f:
                f.write(str(score)+' ')
            pygame.time.delay(4000)
            main_menu(DIFFICULTY_INDEX)
                
    
        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(keys_pressed, player, VEL)
        enemy_movement(enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, player, ENEMY_VEL)
        handle_bullets(enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, player, player_bullets, BULLET_VEL)
        
        draw_window(player, enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8, enemy_9, enemy_10, player_bullets, score, COUNTDOWN, LAST_COUNT)
        
    main_menu()
    
if __name__ == '__main__':
    main_menu(2)