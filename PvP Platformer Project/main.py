
# Modules ---------------------------------------------------------------------#
from pygame.locals import *
from sys import exit
from os import environ

import pygame

from assets.scripts.graphics import *
from assets.scripts.file_io import *
from assets.scripts.core_maths import *
from assets.scripts.projectiles import Arrow, Bullet
from assets.scripts.player import Player


# Setup / Window related ------------------------------------------------------#
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

Clock = pygame.time.Clock()


monitor_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
default_screen_size = (1000, 680)
last_screen_size = default_screen_size
environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ((monitor_size[0] - default_screen_size[0]) * 0.5, (monitor_size[1] - default_screen_size[1]) * 0.5)

zoom = 2

Screen = pygame.display.set_mode(default_screen_size, RESIZABLE)
Canvas = pygame.Surface((default_screen_size[0] // zoom, default_screen_size[1] // zoom))

pygame.display.set_caption("PvP Platformer Project", "PPPP")
pygame.display.set_icon(load_image("assets/images/game_icon.png", (127, 127, 127)))

fullscreen = False


# Player related --------------------------------------------------------------#
player_1 = Player([100, 100])
moving_left = False
moving_right = False

player_idle_animation = Animation(load_animation("assets/animations/player/idle/"), False)
player_idle_animation.active_animations.append([0, player_1.location.copy()])



while True:

    # Drawing -----------------------------------------------------------------#
    Canvas.fill((255, 255, 255))

    player_idle_animation.update_active_animations()
    player_idle_animation.draw_active_animations(Canvas, (0, 0))


    player_1.velocity = [0, 0]
    if moving_left:
        player_1.velocity[0] -= player_1.speed
    if moving_right:
        player_1.velocity[0] += player_1.speed

    player_1.velocity[1] += player_1.gravity
    player_1.gravity += 0.25
    player_1.gravity = min([player_1.gravity, 10])

    player_1.move([])

    player_idle_animation.active_animations[0][1] = player_1.location


    # Input -------------------------------------------------------------------#
    for input_event in pygame.event.get():
        if input_event.type == QUIT:
            pygame.quit()
            exit()

        if input_event.type == KEYDOWN:
            if input_event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if input_event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    Screen = pygame.display.set_mode(monitor_size, FULLSCREEN)
                else:
                    Screen = pygame.display.set_mode(last_screen_size, RESIZABLE)
                Canvas = pygame.Surface((Screen.get_width() // zoom, Screen.get_height() // zoom))
            if input_event.key == K_a:
                moving_left = True
                player_1.last_moved_direction = -1
            if input_event.key == K_d:
                moving_right = True
                player_1.last_moved_direction = 1
            if input_event.key == K_w:
                player_1.gravity = -3
        if input_event.type == KEYUP:
            if input_event.key == K_a:
                moving_left = False
            if input_event.key == K_d:
                moving_right = False

        if input_event.type == VIDEORESIZE:
            if not fullscreen:
                Screen = pygame.display.set_mode(input_event.size, RESIZABLE)
                Canvas = pygame.Surface((input_event.w // zoom, input_event.h // zoom))
                last_screen_size = input_event.size


    # Updating ----------------------------------------------------------------#
    Screen.blit(pygame.transform.scale(Canvas, Screen.get_size()), (0, 0))
    pygame.display.update()
    Clock.tick(60)