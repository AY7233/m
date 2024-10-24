import matplotlib.pyplot as plt

def midpoint_circle(x_center, y_center, radius):
    x = 0
    y = radius
    p = 1 - radius
    points = []

    while x <= y:
        points.extend([
            (x_center + x, y_center + y),
            (x_center - x, y_center + y),
            (x_center + x, y_center - y),
            (x_center - x, y_center - y),
            (x_center + y, y_center + x),
            (x_center - y, y_center + x),
            (x_center + y, y_center - x),
            (x_center - y, y_center - x),
        ])
        
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

    return points

def plot_circle(points):
    for x, y in points:
        plt.plot(x, y, 'bo')  # Plot each point
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.gca().invert_yaxis()
    plt.show()

def main():
    x_center = int(input("Enter x-coordinate of center: "))
    y_center = int(input("Enter y-coordinate of center: "))
    radius = int(input("Enter the radius: "))
    
    points = midpoint_circle(x_center, y_center, radius)
    plot_circle(points)

if __name__ == "__main__":
    main()
