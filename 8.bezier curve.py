import numpy as np
import matplotlib.pyplot as plt
import math  

def bezier_curve(control_points, num_points=100):
    n = len(control_points) - 1
    curve_points = []

    for t in np.linspace(0, 1, num_points):
        point = np.array([0.0, 0.0])
        for i in range(n + 1):
            binomial_coefficient = math.comb(n, i)  # Use math.comb
            bernstein_polynomial = binomial_coefficient * (t ** i) * ((1 - t) ** (n - i))
            point += bernstein_polynomial * control_points[i]
        curve_points.append(point)

    return np.array(curve_points)

def plot_curve(control_points, curve_points):
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
    plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Bézier Curve')
    plt.title("Bézier Curve")
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def user_input():
    num_points = int(input("Enter the number of control points (minimum 2): "))
    points = []
    for i in range(num_points):
        x = float(input(f"Enter x-coordinate of point {i + 1}: "))
        y = float(input(f"Enter y-coordinate of point {i + 1}: "))
        points.append([x, y])
    return np.array(points)

def menu():
    print("Menu:")
    print("1. Generate a Bézier Curve")
    print("2. Exit")
    return int(input("Enter your choice: "))

def main():
    while True:
        choice = menu()
        if choice == 1:
            control_points = user_input()
            curve_points = bezier_curve(control_points)
            plot_curve(control_points, curve_points)
        elif choice == 2:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
