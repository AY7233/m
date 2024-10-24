import matplotlib.pyplot as plt
import numpy as np

grid_size = 20
grid = np.ones((grid_size, grid_size))

def putpixel(x, y, color):
    if 0 <= x < grid_size and 0 <= y < grid_size:
        grid[y, x] = color

def getpixel(x, y):
    if 0 <= x < grid_size and 0 <= y < grid_size:
        return grid[y, x]
    return -1

def flood_fill(x, y, fill_color, target_color):
    if getpixel(x, y) == target_color:
        putpixel(x, y, fill_color)
        flood_fill(x + 1, y, fill_color, target_color)
        flood_fill(x - 1, y, fill_color, target_color)
        flood_fill(x, y + 1, fill_color, target_color)
        flood_fill(x, y - 1, fill_color, target_color)

def plot_grid():
    plt.imshow(grid, cmap='gray', origin='lower')
    plt.axis('off')
    plt.show()

def main():
    for x in range(5, 15):
        putpixel(x, 5, 0)
        putpixel(x, 15, 0)
    for y in range(5, 16):
        putpixel(5, y, 0)
        putpixel(15, y, 0)

    plot_grid()

    seed_x = 10
    seed_y = 10
    flood_fill(seed_x, seed_y, 0.5, 1)

    plot_grid()

if __name__ == "__main__":
    main()
