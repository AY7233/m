import numpy as np
import matplotlib.pyplot as plt

def plot_polygon(points, color='blue'):
    points = np.vstack([points, points[0]])
    plt.plot(points[:, 0], points[:, 1], color=color)
    plt.fill(points[:, 0], points[:, 1], color=color, alpha=0.5)

def translate(points, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    translated_points = points_homogeneous @ translation_matrix.T
    return translated_points[:, :2]

def scale(points, sx, sy):
    scaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    scaled_points = points_homogeneous @ scaling_matrix.T
    return scaled_points[:, :2]

def rotate(points, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta), np.cos(theta), 0],
                                [0, 0, 1]])
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    rotated_points = points_homogeneous @ rotation_matrix.T
    return rotated_points[:, :2]

def main():
    square = np.array([[1, 1],
                       [1, -1],
                       [-1, -1],
                       [-1, 1]])

    while True:
        print("\nMenu:")
        print("1. Translate")
        print("2. Scale")
        print("3. Rotate")
        print("4. Combined Transformations")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            tx = float(input("Enter translation in x (tx): "))
            ty = float(input("Enter translation in y (ty): "))
            transformed_square = translate(square, tx, ty)
            plt.figure()
            plot_polygon(transformed_square, color='green')
            plt.title(f'Translated Square by ({tx}, {ty})')
            plt.xlim(-3, 3)
            plt.ylim(-3, 3)
            plt.axhline(0, color='black', linewidth=0.5, ls='--')
            plt.axvline(0, color='black', linewidth=0.5, ls='--')
            plt.show()

        elif choice == '2':
            sx = float(input("Enter scaling factor in x (sx): "))
            sy = float(input("Enter scaling factor in y (sy): "))
            transformed_square = scale(square, sx, sy)
            plt.figure()
            plot_polygon(transformed_square, color='red')
            plt.title(f'Scaled Square by ({sx}, {sy})')
            plt.xlim(-3, 3)
            plt.ylim(-3, 3)
            plt.axhline(0, color='black', linewidth=0.5, ls='--')
            plt.axvline(0, color='black', linewidth=0.5, ls='--')
            plt.show()

        elif choice == '3':
            angle = float(input("Enter rotation angle (in degrees): "))
            transformed_square = rotate(square, angle)
            plt.figure()
            plot_polygon(transformed_square, color='orange')
            plt.title(f'Rotated Square by {angle}°')
            plt.xlim(-3, 3)
            plt.ylim(-3, 3)
            plt.axhline(0, color='black', linewidth=0.5, ls='--')
            plt.axvline(0, color='black', linewidth=0.5, ls='--')
            plt.show()

        elif choice == '4':
            tx = float(input("Enter translation in x (tx): "))
            ty = float(input("Enter translation in y (ty): "))
            sx = float(input("Enter scaling factor in x (sx): "))
            sy = float(input("Enter scaling factor in y (sy): "))
            angle = float(input("Enter rotation angle (in degrees): "))
            transformed_square = translate(scale(rotate(square, angle), sx, sy), tx, ty)
            plt.figure()
            plot_polygon(transformed_square, color='purple')
            plt.title('Combined Transformations')
            plt.xlim(-3, 3)
            plt.ylim(-3, 3)
            plt.axhline(0, color='black', linewidth=0.5, ls='--')
            plt.axvline(0, color='black', linewidth=0.5, ls='--')
            plt.show()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
