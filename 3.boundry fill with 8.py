import pygame
import sys


def flood_fill(surface, x, y, fill_color, border_color):
    current_color = surface.get_at((x, y))
    
    if current_color != border_color and current_color != fill_color:
        surface.set_at((x, y), fill_color)
        
        
        flood_fill(surface, x, y + 1, fill_color, border_color)
        flood_fill(surface, x, y - 1, fill_color, border_color)
        flood_fill(surface, x + 1, y, fill_color, border_color)
        flood_fill(surface, x + 1, y + 1, fill_color, border_color)
        flood_fill(surface, x + 1, y - 1, fill_color, border_color)
        flood_fill(surface, x - 1, y, fill_color, border_color)
        flood_fill(surface, x - 1, y + 1, fill_color, border_color)
        flood_fill(surface, x - 1, y - 1, fill_color, border_color)


def main():
    pygame.init()
    
    
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Flood Fill Example")
    

    x = int(input("ENTER CENTER X: "))
    y = int(input("ENTER CENTER Y: "))
    r = int(input("ENTER RADIUS: "))
    
    
    pygame.draw.circle(screen, (255, 255, 255), (x, y), r)  
    pygame.display.flip()
    
    
    flood_fill(screen, x, y, (255, 0, 0), (255, 255, 255))  
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()

if __name__ == "__main__":
    main()