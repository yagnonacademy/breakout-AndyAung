#----------------------------------------------------------------------------
#                       Chapter 10 Homework: Breakout
#
#       Created by: Andy
#       Created on: Feburary 10, 2020
#
#----------------------------------------------------------------------------

import sys
import pygame

#Define some colors
BLACK = (0, 0, 0)
PURPLE = (192, 19, 187)
BLUE = (18, 229, 226)
YELLOW = (228, 243, 4)
ORANGE = (243, 178, 4)
RED = (250,0,0)

#Draw blocks
def draw_block(screen, x, y):
    pygame.draw.rect(screen, YELLOW, (x, y, 125, 20))
        
def main():
    pygame.init()

    #Set the width and height of the screen [width,height]
    size = [800, 700]
    screen = pygame.display.set_mode(size)

    #Font
    myfont = pygame.font.SysFont("BREAKOUT", 30)
    myfont2 = pygame.font.SysFont("BREAKOUT", 30)

    #Used to manage how fast the screen updates
    fps = 60
    fpsClock = pygame.time.Clock()

    #Hide the mouse cursor
    pygame.mouse.set_visible(0)

    #Speed in pizels per frame
    xspeed = 10
    yspeed = 10

    #Draw ball
    ball_position = [200,300]

    #Draw blocks
    pos_list = [[20,50], [180,50], [340,50], [500,50], [660,50], [20,100], [180,100], [340,100], [500,100], [660,100], [20,150], [180,150], [340,150], [500,150], [660,150]]

    #Score & Life
    score = 0
    life = 3
   
    #Loop until the user clicks the close button
    done = False

    #Main Program Loop
    while not done:
      screen.fill(PURPLE)

      #Event Processing
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      
      #Ball Movement
      ball_position[1] += yspeed
      ball_position[0] += xspeed

      if ball_position[0] >= 760 or ball_position[0] <= 20:
          xspeed = -xspeed

      if ball_position[1] >= 770 or ball_position[1] <= 20:
          yspeed = -yspeed


      #Mouse Movement
      pos = pygame.mouse.get_pos()
      mouse_x = pos[0]
      mouse_y = pos[1]

      if mouse_x >= 645:
          mouse_x = 645

      if mouse_x <= 30:
          mouse_x = 30

      pygame.mouse.set_visible(False)


      #Game Over
      if ball_position[1] >= 675:
          life -= 1
          ball_position = [200,300]
          yspeed = -yspeed
          
      if life == 0:    
          done = True
          pygame.mouse.set_visible(True)
          game_over = myfont2.render("GAME OVER! You have lost.", False, RED)
          screen.blit(game_over, (300,300))

      if score == 15:    
          done = True
          pygame.mouse.set_visible(True)
          game_over = myfont2.render("CONGRATULATIONS! You've won", False, RED)
          screen.blit(game_over, (225,300))


      #paddle collision
      paddle_x1 = mouse_x
      paddle_x2 = mouse_x + 125
      paddle_y = 550
      if paddle_x1 < ball_position[0] < paddle_x2 and  ball_position[1] == paddle_y:
          yspeed = -yspeed

      #Draw borders & circle
      pygame.draw.circle(screen, RED, ball_position, 10)

      for i in range(len(pos_list)):
          draw_block(screen, pos_list[i][0], pos_list[i][1])
      
      #Block position
      for i in range(len(pos_list)):

          #Ball collision
          if 20 + pos_list[i][0] < ball_position[0] < 20 + pos_list[i][0] + 95 and ball_position[1] == pos_list[i][1] + 20:
              yspeed = -yspeed
              del pos_list[i]
              score += 1
              break

      score_font = myfont.render("Score: "+ str(score), False, BLUE)
              
      for i in range(len(pos_list)):
          draw_block(screen, pos_list[i][0], pos_list[i][1])   


      #Draw paddle
      pygame.draw.rect(screen, ORANGE, (mouse_x, 570, 120, 20))

      #Write text
      screen.blit(score_font, (690,600))

      life_font = myfont.render("Lives Remaining: "+ str(life), False, BLUE)
      screen.blit(life_font, (10, 600)) 
      
      #Set caption
      pygame.display.set_caption("Breakout")
      pygame.display.flip()
      fpsClock.tick(fps)
      
    #Loop again
    while True:
        screen.fill(PURPLE)
      
    for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

from pygame.locals import *

main()  

