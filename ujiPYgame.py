# mencoba package untuk pygame
import pygame

## init
pygame.init()

# variable running game
isRun = True

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# object game

# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

speed = 10

while isRun:
       pygame.time.delay(20)
       # user input, data dari database
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     isRun = False

       # kita ambil semua keybaora press
       keys = pygame.key.get_pressed()

       # ambil ke kiri
       if keys[pygame.K_LEFT] and x > 0:
              x -= speed

       # ambil ke kanan
       if keys[pygame.K_RIGHT] and x < window_panjang - panjang:
              x += speed

       # ambil ke atas
       if keys[pygame.K_UP] and y > 0:
              y -= speed

       # ambil ke bawah
       if keys[pygame.K_DOWN] and y < window_lebar - lebar:
              y += speed


       # update asset
       window.fill((255,255,255))
       pygame.draw.rect(window ,(255,120,0),(x,y,panjang,lebar))
       # render ke display
       pygame.display.update()

pygame.quit()

