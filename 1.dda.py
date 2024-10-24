import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    x_increment = dx / steps
    y_increment = dy / steps
    
    x = x1
    y = y1
    points = []
    
    for i in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment
    
    return points

def plot_line(points):
    x_vals, y_vals = zip(*points)
    plt.plot(x_vals, y_vals, marker='o')
    plt.title('DDA Line Drawing')
    plt.show()

def menu():
    while True:
        print("\nMenu:")
        print("1. Draw a line using DDA Algorithm")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                x1 = int(input("Enter x1: "))
                y1 = int(input("Enter y1: "))
                x2 = int(input("Enter x2: "))
                y2 = int(input("Enter y2: "))
                
                points = DDA(x1, y1, x2, y2)
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
