import pygame
import sys
import subprocess

# from kbc import kbc
# from snake.snake import snake_game
# from toh.toh import toh  

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gaming Zone")

background_image = pygame.image.load("bg_image.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BG = (27, 198, 207)
NEON_WHITE = (200, 200, 200) 

font = pygame.font.Font(None, 50)
title_font = pygame.font.Font(None, 80)

title_text = "Gaming Zone"
game_texts = ["Rock Paper Scissor", "KBC", "Turtle Crossing" ,"Tic-Tac-Toe"]

button_positions = [
    (280, 300),
    (600, 300),
    (280, 380),
    (600, 380)
]

def render_neon_text(text, font, color, glow_color, pos, screen):

    for size in (3, 2, 1):
        glow = font.render(text, True, glow_color)
        glow_rect = glow.get_rect(center=pos)
        screen.blit(glow, glow_rect.move(size, size))

    # Render main text on top
    main_text = font.render(text, True, color)
    main_text_rect = main_text.get_rect(center=pos)
    screen.blit(main_text, main_text_rect)

def main_menu():
    running = True
    while running:
        screen.blit(background_image, (0, 0))

        render_neon_text(title_text, title_font, WHITE, NEON_WHITE, (screen_width // 2, 160), screen)

        for i, game_text in enumerate(game_texts):
            render_neon_text(game_text, font, WHITE, NEON_WHITE, button_positions[i], screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, pos in enumerate(button_positions):
                    text_rect = font.render(game_texts[i], True, WHITE).get_rect(center=pos)
                    if text_rect.collidepoint(mouse_pos):
                        if i == 0: subprocess.Popen(["python3","GUI_Rock_Paper_Scissors/rpc.py"])
                        elif i == 1: subprocess.Popen(["python3","kbc/kbc.py"])
                        elif i == 2: subprocess.Popen(["python3","python_turtle_crossing/main.py"])
                        elif i == 3: subprocess.Popen(["python3","Tic_Tac_Toe/Tic_Tac_Toe_Game.py"])

        pygame.display.flip()

main_menu()