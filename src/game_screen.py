import pygame
from sys import exit
def g_screen():
    pygame.init()
    screen=pygame.display.set_mode((800,400))
    pygame.display.set_caption('BATTLESHIPS')
    clock=pygame.time.Clock()
    test_surface= pygame.Surface((750,350))
    test_surface.fill('Black')
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(test_surface,(25,25) )
        blockSize = 50 
        for x in range(50, 300, blockSize):
            for y in range(50, 300, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen,"Green", rect, 2)

        blockSize = 50 
        for x in range(400, 650, blockSize):
            for y in range(50, 300, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen,"Green", rect,2)
        

        pygame.display.update()
        clock.tick(60)

def text_ip():
    pass

def main():
    screen = pygame.display.set_mode((640, 480))
    font=pygame.font.SysFont('Corbel',35)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('green')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
main()