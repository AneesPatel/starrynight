"""
Anees Patel

Makes a scene using pygame

2/15/22
"""


import pygame, sys, random, math, time
from pygame.locals import *
pygame.init()


CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKER_GREEN = (15, 148, 86)
BLUE = (0, 0, 255)
BRIGHT_BLUE = (102, 255, 255)
DARKER_BLUE = (30, 59, 117)
GRAY = (128, 128, 128)
MOON_YELLOW = (255, 252, 204)
DARKER_DARK_BLUE = (25, 27, 60)
SHADOW = (20, 23, 50)
HOUSE_COLOR = (20, 23, 50)
LIGHT = (189, 174, 107)


def main():
    CAR_REVERSED = False
    LIGHT_CHANGED = False
    LIGHT_ON = False
    total_time = 0
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 400
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption("Drawing")
    #DISPLAYSURF.fill(DARKER_BLUE)
    current_angle_1 = 0
    current_angle_2 = 30
    car_start = 0
    y_position = 180
    y_position_2 = 180
    y_position_3 = 180
    plane_pos = WINDOW_WIDTH

    stars = []

    for x in range(50):
        current_X = random.randint(0, WINDOW_WIDTH)
        current_Y = random.randint(0, WINDOW_HEIGHT)
        stars.append([current_X, current_Y])

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        'background'
        for current_x_axis in range(WINDOW_HEIGHT):
            r = current_x_axis / (WINDOW_WIDTH - 1) * 30
            g = current_x_axis / (WINDOW_WIDTH - 1) * 59
            b = current_x_axis / (WINDOW_WIDTH - 1) * 117
            gradient = (r, g, b)
            pygame.draw.line(DISPLAYSURF, gradient, (0, current_x_axis), (WINDOW_WIDTH - 1, current_x_axis))

        'stars'
        for x in stars:
            star_x = x[0]
            star_y = x[1]
            pygame.draw.line(DISPLAYSURF, WHITE, (star_x, star_y), (star_x, star_y), 1)

        'ground'
        pygame.draw.rect(DISPLAYSURF, DARKER_DARK_BLUE, (0, 335, WINDOW_WIDTH, 100))

        'moon'
        pygame.draw.ellipse(DISPLAYSURF, MOON_YELLOW, (30, 20, 80, 80))
        #pygame.draw.ellipse(DISPLAYSURF, DARKER_BLUE, (115, 15, 80, 100))
        #pygame.draw.ellipse(DISPLAYSURF, BLACK, (90, 30, 80, 100), width=1)

        'cloud #1'
        pygame.draw.ellipse(DISPLAYSURF, WHITE, (332, 45, 30, 30))
        pygame.draw.ellipse(DISPLAYSURF, WHITE, (357, 45, 30, 30))
        pygame.draw.ellipse(DISPLAYSURF, WHITE, (382, 45, 30, 30))
        pygame.draw.ellipse(DISPLAYSURF, WHITE, (320, 60, 30, 30))
        pygame.draw.ellipse(DISPLAYSURF, WHITE, (345, 60, 30, 30))
        pygame.draw.ellipse(DISPLAYSURF, WHITE, (370, 60, 30, 30))
        pygame.draw.ellipse(DISPLAYSURF, WHITE, (395, 60, 30, 30))

        'windmill'
        pygame.draw.polygon(DISPLAYSURF, DARKER_DARK_BLUE, [[115, 350], [135, 350], [125, 125], [125, 125]], width=3)
        #pygame.draw.circle(DISPLAYSURF, DARKER_DARK_BLUE, (125, 125), 45, width=2)
        angle_1 = current_angle_1 * 0.05
        angle_2 = current_angle_2 * 0.05

        line1_x = 200/2.0*math.sin(angle_1)
        line1_y = 200/2.0*math.cos(angle_1)

        line2_x = 200/2.0*math.sin(angle_2)
        line2_y = 200/2.0*math.cos(angle_2)

        pygame.draw.line(DISPLAYSURF, DARKER_DARK_BLUE, ((125 + line1_x), (125 + line1_y)), ((125 - line1_x), (125 - line1_y)), width=4)
        pygame.draw.line(DISPLAYSURF, DARKER_DARK_BLUE, ((125 + line2_x), (125 + line2_y)), ((125 - line2_x), (125 - line2_y)), width=4)
        current_angle_1 += 1
        current_angle_2 += 1

        'house'
        pygame.draw.rect(DISPLAYSURF, HOUSE_COLOR, (345, 220, 125, 120))
        pygame.draw.polygon(DISPLAYSURF, HOUSE_COLOR, [[335, 200], [479, 200], [487, 270], [327, 270]])
        pygame.draw.polygon(DISPLAYSURF, BLACK, [[335, 200], [479, 200], [487, 270], [327, 270]], width=2)
        pygame.draw.polygon(DISPLAYSURF, BLACK, [[407, 200], [370, 268], [442, 268]], width=2)
        pygame.draw.polygon(DISPLAYSURF, HOUSE_COLOR, [[275, 290], [275, 340], [345, 340], [345, 280]])
        pygame.draw.line(DISPLAYSURF, BLACK, [270, 290], [350, 280], width=2)
        pygame.draw.line(DISPLAYSURF, HOUSE_COLOR, [370, 268], [442, 268], width=6)

        'smokestack/fireplace'
        pygame.draw.rect(DISPLAYSURF, HOUSE_COLOR, (450, 180, 20, 20))
        pygame.draw.rect(DISPLAYSURF, BLACK, (450, 180, 20, 20), width=2)

        if y_position > -20:
            pygame.draw.circle(DISPLAYSURF, GRAY, (460, y_position), 10)
            pygame.draw.circle(DISPLAYSURF, BLACK, (460, y_position), 10, width=1)
            y_position -= 1
        elif y_position < 0:
            y_position = 180

        if y_position_2 > -20:
            pygame.draw.circle(DISPLAYSURF, GRAY, (465, y_position_2 - 10), 8)
            pygame.draw.circle(DISPLAYSURF, BLACK, (465, y_position_2 - 10), 8, width=1)
            y_position_2 -= 1
        elif y_position_2 < 0:
            y_position_2 = 180

        if y_position_3 > -20:
            pygame.draw.circle(DISPLAYSURF, GRAY, (460, y_position_3 - 21), 6)
            pygame.draw.circle(DISPLAYSURF, BLACK, (460, y_position_3 - 21), 6, width=1)
            y_position_3 -= 1
        elif y_position_3 < 0:
            y_position_3 = 180

        'window lights'
        if LIGHT_CHANGED == True:
            total_time = pygame.time.get_ticks()
            LIGHT_CHANGED = False
        current_time = pygame.time.get_ticks()
        time_until_light = current_time - total_time

        if time_until_light > 8800 and LIGHT_ON == False:
            LIGHT_ON = True
            LIGHT_CHANGED = True
            pygame.draw.rect(DISPLAYSURF, LIGHT, (369, 285, 27, 27))
            pygame.draw.rect(DISPLAYSURF, LIGHT, (423, 285, 27, 27))
            pygame.draw.rect(DISPLAYSURF, LIGHT, (398, 235, 20, 20))
        elif time_until_light > 8800 and LIGHT_ON == True:
            LIGHT_ON = False
            LIGHT_CHANGED = True
            pygame.draw.rect(DISPLAYSURF, BLACK, (398, 235, 20, 20))
            pygame.draw.rect(DISPLAYSURF, BLACK, (369, 285, 27, 27))
            pygame.draw.rect(DISPLAYSURF, BLACK, (423, 285, 27, 27))

        if LIGHT_ON == True:
            pygame.draw.rect(DISPLAYSURF, LIGHT, (398, 235, 20, 20))
            pygame.draw.rect(DISPLAYSURF, LIGHT, (369, 285, 27, 27))
            pygame.draw.rect(DISPLAYSURF, LIGHT, (423, 285, 27, 27))
        else:
            pygame.draw.rect(DISPLAYSURF, BLACK, (398, 235, 20, 20))
            pygame.draw.rect(DISPLAYSURF, BLACK, (369, 285, 27, 27))
            pygame.draw.rect(DISPLAYSURF, BLACK, (423, 285, 27, 27))

        'car'
        if car_start < 250 and CAR_REVERSED == False:
            pygame.draw.rect(DISPLAYSURF, DARKER_DARK_BLUE, (car_start, 300, 50, 25))
            pygame.draw.rect(DISPLAYSURF, DARKER_DARK_BLUE, (car_start + 50, 310, 10, 15))
            pygame.draw.rect(DISPLAYSURF, GRAY, (car_start + 35, 300, 15, 10))
            pygame.draw.rect(DISPLAYSURF, MOON_YELLOW, (car_start + 59, 320, 3, 5))
            pygame.draw.circle(DISPLAYSURF, BLACK, (car_start + 7, 330), 6)
            pygame.draw.circle(DISPLAYSURF, BLACK, (car_start + 45, 330), 6)
        elif car_start > 250 and LIGHT_ON == True:
            CAR_REVERSED = True
            car_start = 275

        if car_start == -1:
            CAR_REVERSED = False

        if CAR_REVERSED == True:
            pygame.draw.rect(DISPLAYSURF, DARKER_DARK_BLUE, (car_start, 300, 50, 25))
            pygame.draw.rect(DISPLAYSURF, DARKER_DARK_BLUE, (car_start- 10, 310, 10, 15))
            pygame.draw.rect(DISPLAYSURF, GRAY, (car_start, 300, 15, 10))
            pygame.draw.rect(DISPLAYSURF, MOON_YELLOW, (car_start - 12, 320, 3, 5))
            pygame.draw.circle(DISPLAYSURF, BLACK, (car_start + 7, 330), 6)
            pygame.draw.circle(DISPLAYSURF, BLACK, (car_start + 45, 330), 6)
            car_start -= 1
        else:
            car_start += 1

        'plane'
        """
        pygame.draw.rect(DISPLAYSURF, DARKER_DARK_BLUE, (plane_pos, 15, 45, 15))
        pygame.draw.rect(DISPLAYSURF, MOON_YELLOW, (plane_pos, 15, 12, 7))
        #pygame.draw.rect(DISPLAYSURF, DARKER_DARK_BLUE, (plane_pos - 105, 15, 9, 7))
        pygame.draw.polygon(DISPLAYSURF, DARKER_DARK_BLUE, ((plane_pos + 15, 15), (plane_pos + 25, 15), (plane_pos + 25, 8)))
        pygame.draw.polygon(DISPLAYSURF, DARKER_DARK_BLUE, ((plane_pos + 15, 30), (plane_pos + 25, 30), (plane_pos + 25, 37))) 
        pygame.draw.polygon(DISPLAYSURF, DARKER_DARK_BLUE, ((plane_pos, 15), (plane_pos - 150, 30), (plane_pos - 150, 30))) 
        plane_pos -=1
        """

        pygame.display.update()
        CLOCK.tick(60)


if __name__ == '__main__':
    main()
