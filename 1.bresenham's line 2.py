import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy
    
    x, y = x1, y1
    
    while True:
        points.append((x, y))
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    
    return points

def plot_line(points):
    x_vals, y_vals = zip(*points)
    plt.plot(x_vals, y_vals, marker='o')
    plt.title('Bresenham Line Drawing')
    plt.show()

def menu():
    while True:
        print("\nMenu:")
        print("1. Draw a line using Bresenham Algorithm")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                x1 = int(input("Enter x1: "))
                y1 = int(input("Enter y1: "))
                x2 = int(input("Enter x2: "))
                y2 = int(input("Enter y2: "))
                
                points = bresenham(x1, y1, x2, y2)
                print(f"Line points: {points}")
                plot_line(points)
            except ValueError:
                print("Invalid input! Please enter valid integers.")
        
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    menu()
